# POCP
## 计算两个细菌基因组之间的核心蛋白相似性
参考文献:

题目：[《A Proposed Genus Boundary for the Prokaryotes Based on Genomic Insights》](https://jb.asm.org/content/196/12/2210) 

链接: http://pdfs.semanticscholar.org/cd47/994ff226f6f26874c9c731a82320e3e27476.pdf

---

## 2019-11-12

使用预配置好的安装包 computePOCP_v*.zip, 可在 windows 系统平台下直接使用解压之后 运算脚本 JustRunThis.R; 

在该脚本中调用了可在 Windows 系统下运行的 [prodigal](https://github.com/hyattpd/Prodigal/releases) 和 [diamond](https://github.com/bbuchfink/diamond/releases) 两个软件; 同时, 在 R 中导入了两个分析包 data.table 和 seqinr, 如果之前没有预安装过, 可使用 install.packages(c("data.table", "seqinr")) 安装相应的分析包. 

prodigal -- 仅用于预测基因的氨基酸序列; diamond -- 用于蛋白之间的两两比对计算相似性

使用须知: 仅需要提供细菌基因组 fasta 格式的核酸序列, 文件的命名参考 "Genus_species_strain.fasta", 使用下划线连接字符.

**If cite, please reference: https://github.com/2015qyliang/POCP**

---

第一篇引用该工作的研究 [Geomonas oryzae gen. nov., sp. nov., Geomonas edaphica sp. nov., Geomonas ferrireducens sp. nov., Geomonas terrae sp. nov., Four Ferric-Reducing Bacteria Isolated From Paddy Soil, and Reclassification of Three Species of the Genus Geobacter as Members of the Genus Geomonas gen. nov.; Front. Microbiol., 25 September 2019](https://doi.org/10.3389/fmicb.2019.02201)
