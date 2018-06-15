# coding： utf-8
# copyright: qyliang
# time: 06-15-2018

import os
import pandas as pd
from collections import OrderedDict

# 定义获取每个物种的总蛋白数量
def Total(filename):
	os.chdir(rawFilePath)
	file = open(filename)
	text = file.read()
	proteinTotal = text.count('>')
	file.close()
	return proteinTotal

# 定义计算每个物种注释的蛋白含有的氨基酸个数
def aaTotal(filename):
	os.chdir(rawFilePath)
	file = open(filename)
	text = file.read()
	file.close()
	ltsp = text.split('>')
	aaDict = OrderedDict()
	for line in ltsp:
		if line != '':
			firstBreakIndex = line.index('\n')
			key = line[:firstBreakIndex].split(' ')[0]
			aaDict[key] = len(line[firstBreakIndex:])
		else:
			pass
	return aaDict

# 定义构建数据库函数
def creatdb():
	os.chdir(scriptPath)
	proc1 = r'.\makeblastdb.exe -dbtype prot -parse_seqids -in .\Rawdata\\'
	proc2 = r' -out .\Database\\'
	for fn in fnlist:
		process = proc1 + fn + proc2 + fn.split('.')[0]
		print('='*10,process)
		os.system(process)

# 定义流程化blastp函数
def blast():
	proc1 = r'.\blastp.exe -evalue 1e-5 -max_target_seqs 1 -outfmt 6'
	proc2 = r' -query .\Rawdata\\'
	proc3 = r' -db .\Database\\'
	proc4 = r' -out .\Result\\'
	for fn in fnlist:
		os.chdir(scriptPath)
		index = fnlist.index(fn)
		if index != len(fnlist)-1:
			A = fn
			B = fnlist[index + 1]
			# A2B
			processAB = proc1 + proc2 + A + proc3 + B.split('.')[0] + proc4 + A.split('.')[0] + 'TO' + B.split('.')[0] + '.tab'
			# B2A
			processBA = proc1 + proc2 + B + proc3 + A.split('.')[0] + proc4 + B.split('.')[0] + 'TO' + A.split('.')[0] + '.tab'
			print('='*10,processAB)
			os.system(processAB)
			print('='*10,processBA)
			os.system(processBA)
			os.chdir(resultPath)
			resultFileName1 = A.split('.')[0] + 'TO' + B.split('.')[0] + '.tab'
			resultFileName2 = B.split('.')[0] + 'TO' + A.split('.')[0] + '.tab'
			dframe1 = pd.read_csv(resultFileName1, sep = '\t')
			dframe2 = pd.read_csv(resultFileName2, sep = '\t')
			D1 = aaTotal(A)
			for i in range(dframe1.shape[0]):
				dframe1.iloc[i,11] = (dframe1.iloc[i,3])/(D1[dframe1.iloc[i,0]])
			cdframe1 = dframe1[dframe1.iloc[:,2] > 40]
			cdframe11 = cdframe1[cdframe1.iloc[:,11] > 0.5]
			C1 = cdframe11.shape[0]
			D2 = aaTotal(B)
			for i in range(dframe2.shape[0]):
				dframe2.iloc[i,11] = (dframe2.iloc[i,3])/(D2[dframe2.iloc[i,0]])
			cdframe2 = dframe2[dframe2.iloc[:,2] > 40]
			cdframe22 = cdframe2[cdframe2.iloc[:,11] > 0.5]
			C2 = cdframe22.shape[0]
			T1 = Total(A)
			T2 = Total(B)
			POCP = (C1 + C2)/(T1 + T2)
			pocpResult.append(A.split('.')[0] + '\t' + B.split('.')[0] + '\t' + str(POCP) + '\n')
		else:
			pass

# 路径部分需要根据自己的安装的情况调整
rawFilePath = r'E:\POCP\Rawdata'
scriptPath = r'E:\POCP'
resultPath = r'E:\POCP\Result'
fnlist = os.listdir(rawFilePath)
pocpResult = []
creatdb()
blast()
os.chdir(scriptPath)
with open('POCP.txt','w') as file:
	for line in pocpResult:
		file.write(line)
	file.close()
print('='*50)
