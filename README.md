## 2023-09-06

使用更间接；在windows平台下计算 核心蛋白相似性(POCP)和平均氨基酸相似性(average amino acid identity, AAI); 借助 diamond 计算 POCP和AAI. 

其中 AAI 的计算公式参考 [comparem](https://github.com/dparks1134/CompareM).

---

## 2020-07-28

在windows平台下计算 核心蛋白相似性(POCP)和平均氨基酸相似性(average amino acid identity, AAI); 借助 diamond 计算 POCP和AAI, 借助 blastp (2.9.0+) 计算 AAI. 

其中 AAI 的计算公式参考 [comparem](https://github.com/dparks1134/CompareM).

---

## POCP
## 计算两个细菌基因组之间的核心蛋白相似性
参考文献:

题目：[《A Proposed Genus Boundary for the Prokaryotes Based on Genomic Insights》](https://jb.asm.org/content/196/12/2210) 

链接: http://pdfs.semanticscholar.org/cd47/994ff226f6f26874c9c731a82320e3e27476.pdf

**If cite this process, please: https://github.com/2015qyliang/POCP**

---

## 2019-12-07

add **>> Just One Step <<**

**解放双手 ==>> To Think!!!**

仅需在 windows 系统平台下运行 **startRun.bat** 即可; 使用者仅仅提供已完成基因组测序细菌基因组核酸序列即可, 将其存放在 **GenomeFiles** 文件夹中, 序列文件的命名需要使用下划线将物种名进行连接, 同时文件的后缀为 .fasta, 文件名示例: **Bdellovibrio_bacteriovorus_109J.fasta**

下载可运行的脚本和程序 **==>>** https://github.com/2015qyliang/POCP/releases

---

## 2019-11-12

使用预配置好的安装包 computePOCP_v*.zip, 可在 windows 系统平台下直接使用解压之后 运算脚本 JustRunThis.R; 

在该脚本中调用了可在 Windows 系统下运行的 [prodigal v2.6.3](https://github.com/hyattpd/Prodigal/releases) 和 [diamond v0.9.28](https://github.com/bbuchfink/diamond/releases) 两个软件; 同时, 在 R 中导入了两个分析包 data.table 和 seqinr, 如果之前没有预安装过, 可使用 install.packages(c("data.table", "seqinr")) 安装相应的分析包; 万事俱备之后, 直接运行 **JustRunThis.R** 即可...

prodigal -- 仅用于预测基因的氨基酸序列; diamond -- 用于蛋白之间的两两比对计算相似性

使用须知: 仅需要提供细菌基因组 fasta 格式的核酸序列, 文件的命名参考 "Genus_species_strain.fasta", 使用下划线连接字符.

---

第一篇引用该工作的研究 [Geomonas oryzae gen. nov., sp. nov., Geomonas edaphica sp. nov., Geomonas ferrireducens sp. nov., Geomonas terrae sp. nov., Four Ferric-Reducing Bacteria Isolated From Paddy Soil, and Reclassification of Three Species of the Genus Geobacter as Members of the Genus Geomonas gen. nov.; Front. Microbiol., 25 September 2019](https://doi.org/10.3389/fmicb.2019.02201)
