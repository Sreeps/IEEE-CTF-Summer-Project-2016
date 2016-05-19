#!/usr/bin/python

names = ['Sripathi','Arunraj','Ranjith','Jeshventh','Rohan','Tarun','Suraj','Samvid','Swathi','Swati','Natasha','Prabhanjan','Yuvraj','Chinmay'];


for i in range(len(names)-1):
	for j in range(i,len(names)):
		if  names[j]<names[i]:
			temp=names[i];
			names[i]=names[j];
			names[j]=temp;

print(names);

