#cal.py version:0.1

a = raw_input("type 8 numbers:")
b =  11 - ( 223 + int(a[2]) * 9 + int(a[3]) * 10 + int(a[4]) * 5 + int(a[5]) * 8 + int(a[6]) * 4 + int(a[7]) * 2 ) % 11
if (b == 10):
    b = 'X';print a + b
else:
    print a + str(b)


