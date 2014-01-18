# -* - coding: UTF-8 -* -
import ConfigParser

conf = ConfigParser.ConfigParser()
conf.read("c:/test/test.conf")

start = conf.get("info","start")
end = conf.get("info","end")
next_start = conf.get("info","next_start")


print "临时组织机构代码段的范围："
print start + "--------" + end
print
print '未使用的临时码开始段: ' + next_start
print
a = raw_input("请输入临时码的前八位:")
print



dic_key = { '0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,\
	    'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,\
	    'W':32,'X':33,'Y':34,'Z':35 }
			
dic_weight = { '0':3, '1':7, '2':9, '3':10, '4':5, '5':8, '6':4, '7':2 }
a1 = a[0:2]
a2 = int(a[2:])
x = []

if a2 > int(end[2:]) or a2 < int(start[2:]):
	print "输入的代码段不在范围内"
else:
	n = int(raw_input("输入需要的组织机构代码个数:"))
	print
	print
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
	print
	print
	next_start = a1 + str(a2 + n)
	conf.set("info","next_start",next_start)
	conf.write(open("c:/test/test.conf",'w'))
