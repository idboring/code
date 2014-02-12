#coding=utf-8
import sqlite3
import re
import os
import shutil
import glob
import stat
import sys
import time
import zipfile
import zlib

localtime = time.localtime()
ctime = time.strftime("%Y%m%d%H%M%S",localtime)

database_path = "c:/test/ec_zzs.db"
ecimage_path = "c:/test/EconomicCensus/"
temp_path = "c:/test/temp"

cu = sqlite3.connect(database_path)
cx = cu.cursor()

cx.execute("select _id from retailer_census_record")
id_one = cx.fetchone()
device_num = re.sub('^0','',filter(str.isdigit,str(id_one)))
device_num = device_num[0:16]

cx.execute("select img_path from company_census where data_status = 2")
company_img_path = cx.fetchall()

img_path = []
img_path = company_img_path

cx.execute("select save_path from retailer_census_record where data_status = 2")
retailer_img_path = cx.fetchall()

img_path.extend(retailer_img_path)

img_path_number = []
for i in img_path:
	d = filter(str.isdigit,str(i))
	e = re.sub('^0','',d)
	img_path_number.append(e)
os.mkdir(temp_path)

	
for i in img_path_number:
	if os.path.exists(ecimage_path + i):
		os.chdir(ecimage_path + i)
		pic_list = []
		pic_list = glob.glob('*orign.jpg')
		for j in pic_list:
			shutil.copy(ecimage_path + i + '/' + j ,temp_path)

os.chdir(temp_path)
index = open(ecimage_path + 'index.txt','w')
for root,dirs,files in os.walk(temp_path):
	for name in files:
		c_name = re.sub('_orign','',name)
		os.rename(name,c_name)
		size = 0
		size = os.path.getsize(os.path.join(root,c_name))
		index_item = c_name + ',' + str(size)
		index.write(index_item + '\r\n')

index.close()
shutil.copy(ecimage_path + 'index.txt',temp_path)

output_zip = zipfile.ZipFile("c:/test/" + 'PICTURE_' + device_num + ctime + '.zip' ,'w',zipfile.ZIP_DEFLATED)
for root,dirs,files in os.walk(temp_path):
        for name in files:
                output_zip.write(name)

output_zip.close()
shutil.rmtree(temp_path,ignore_errors=True)
os.chdir(ecimage_path)
os.rmdir(temp_path)

print "sucess"
