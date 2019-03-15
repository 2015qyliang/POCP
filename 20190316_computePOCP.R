library(seqinr)

if (!dir.exists('Database')) {
  dir.create('Database')
}

if (!dir.exists('Result')) {
  dir.create('Result')
}

genome.files <- list.files('Rawdata')

# makeblastdb
for (gn in genome.files) {
  header.file <- strsplit(gn,'.',fixed = T)[[1]][1]
  commond.makedb <- paste0('makeblastdb.exe -dbtype prot -parse_seqids -in Rawdata/',
                           gn, ' -out Database/', header.file)
  system(commond.makedb)
}

# pair blast
genome.comn <- combn(genome.files,2)
blast.comm1 <- 'blastp.exe -evalue 1e-5 -max_target_seqs 1 -outfmt 6 -query Rawdata/'
blast.comm2 <- ' -db Database/'
blast.comm3 <- '  -out Result/'
pocp.vector <- c()
for (i in (1:dim(genome.comn)[2]) ) {
  a.genome <- genome.comn[,i][1]
  b.genome <- genome.comn[,i][2]
  a.header <- strsplit(a.genome,'.',fixed = T)[[1]][1]
  b.header <- strsplit(b.genome,'.',fixed = T)[[1]][1]
  a.genome.seq <- read.fasta(paste0('Rawdata/', a.genome),'AA')
  b.genome.seq <- read.fasta(paste0('Rawdata/', b.genome),'AA')
  a.total <- length(a.genome.seq)
  b.total <- length(b.genome.seq)
  str(a.genome.seq)
  str(b.genome.seq)
  a.seq.list <- names(a.genome.seq)
  b.seq.list <- names(b.genome.seq)
  a.seq.length <- c()
  for (nm in a.seq.list) {
    tmp.len <- length(a.genome.seq[[which(a.seq.list == nm)]])
    a.seq.length <- append(a.seq.length, tmp.len)
  }
  b.seq.length <- c()
  for (nm in b.seq.list) {
    tmp.len <- length(b.genome.seq[[which(b.seq.list == nm)]])
    b.seq.length <- append(b.seq.length, tmp.len)
  }
  a.seq.df <- data.frame(a.seq.list, a.seq.length)
  colnames(a.seq.df) <- c('V1','length')
  b.seq.df <- data.frame(b.seq.list, b.seq.length)
  colnames(b.seq.df) <- c('V1','length')
  
  print('-- Blasting: ',a.header,' - VS - ',b.header)
  # blast forward
  result.forward <- paste0(a.header,'_VS_',b.header,'.tab')
  system(paste0(blast.comm1, a.genome, 
                blast.comm2, b.header, 
                blast.comm3, result.forward))
  df.forward <- read.table(paste0('Result/',result.forward),
                           header = F,sep = '\t',
                           stringsAsFactors = F)
  df.forward <- merge(df.forward, a.seq.df, by = 'V1', all.x = T)
  df.forward$align <- df.forward$V4 / df.forward$length
  df.forward <- df.forward[which(df.forward$V3 > 40 & df.forward$align > 0.5 & df.forward$V11 < 1e-5),]
  C1 <- dim(df.forward)[1]
  
  # blast backward
  result.backward <- paste0(b.header,'_VS_',a.header,'.tab')
  system(paste0(blast.comm1, b.genome, 
                blast.comm2, a.header, 
                blast.comm3, result.backward))
  df.backward <- read.table(paste0('Result/',result.backward),
                            header = F,sep = '\t',
                            stringsAsFactors = F)
  df.backward <- merge(df.backward, b.seq.df, by = 'V1', all.x = T)
  df.backward$align <- df.backward$V4 / df.backward$length
  df.backward <- df.backward[which(df.backward$V3 > 40 & df.backward$align > 0.5 & df.backward$V11 < 1e-5),]
  C2 <- dim(df.backward)[1]
  pocp <- (C1 + C2)/(a.total + b.total)
  pocp.vector <- append(pocp.vector, paste0(a.header,'\t',b.header,'\t',pocp))
  print(paste0('-- Pair blast done: ',a.header,' - VS - ',b.header))
  print(paste0('-- The POCP : ', pocp))
  print('----------------------------------')
}

write(pocp.vector, 'resultPOCP.txt')

unlink("Database", recursive = TRUE)
unlink("Result", recursive = TRUE)
dir.create('Database')
dir.create('Result')
