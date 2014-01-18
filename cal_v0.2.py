#cal.py version:0.2

#coding=UTF-8

a = raw_input("输入八位的组织机构代码:")
n = int(raw_input("输入需要的组织机构代码个数:"))

dic_key = { '0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,\
            'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,\
            'W':32,'X':33,'Y':34,'Z':35 }
			
dic_weight = { '0':3, '1':7, '2':9, '3':10, '4':5, '5':8, '6':4, '7':2 }
a1 = a[0:2]
a2 = int(a[2:])
x = []

for i in range(0,n):
	x.append(a1 + str(a2 + i))
	
for j in x:
	sum = 0
	for i in range(0,8):
		sum += dic_key[j[i]] * dic_weight[str(i)]
	b = 0
	b = 11 - sum % 11
	if (b == 10):
		b = 'X';print j + b
	elif (b == 11):
		b = '0';print j + b
	else:
		print j + str(b)



