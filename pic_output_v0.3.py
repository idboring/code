# coding=UTF-8
import glob
import os
import re
import sqlite3
import shutil
import stat
import sys
import time
import zipfile
import zlib



#定义数据库，图片及临时文件夹的路径
path = os.getcwd()
sep = os.path.sep
database_path = path + sep + 'database' + sep + 'ec.db'
ecimage_path = path + sep + 'EconomicCensus'
temp_path = path + sep + 'temp' + sep


cu = sqlite3.connect(database_path)
cx = cu.cursor()

#提取14位普查区代码
cx.execute("select taskID from task")
taskid_tuple = cx.fetchall()
taskid = []

for i in taskid_tuple:
    taskid.append(str(i[0]))

for i in taskid:

    taskid_output = i
    
    #获得单位表中所有状态为上报，保存及强制保存单位的图片文件夹名称
    cx.execute("select img_path from company_census where task_id = ? and data_status = 2",[taskid_output])
    company_img_path = cx.fetchall()

    img_path = []
    img_path = company_img_path
    
    #获得个体表中所有状态为上报，保存及强制保存个体的图片文件夹名称
    cx.execute("select save_path from retailer_census_record where task_id = ? and data_status = 2",[taskid_output])
    retailer_img_path = cx.fetchall()

    img_path.extend(retailer_img_path)

    #标准化数据库获取的图片文件夹名

    img_path_number = []

    for i in img_path:
        d = filter(str.isdigit,str(i))
        e = re.sub('^0','',d)
        img_path_number.append(e)

    os.mkdir(temp_path)

    #查找EconomicCensus中需要导出的图片并改名（去掉_orign),并拷贝到临时文件夹中
    for i in img_path_number:
        if os.path.exists(ecimage_path + sep + i):
            os.chdir(ecimage_path + sep + i)
            pic_list = []
            pic_list = glob.glob('*orign.jpg')
            for j in pic_list:
                shutil.copy(ecimage_path + sep + i + sep + j ,temp_path)

    #生成索引文件index.txt，格式为图片文件名加逗号，加图片文件的大小（字节值）
    os.chdir(temp_path)
    index = open(ecimage_path + sep + 'index.txt','w')
    for root,dirs,files in os.walk(temp_path):
        for name in files:
            c_name = re.sub('_orign','',name)
            os.rename(name,c_name)
            size = 0
            size = os.path.getsize(os.path.join(root,c_name))
            index_item = c_name + ',' + str(size)
            index.write(index_item + '\n')

    index.close()

    #index.txt复制到导出文件夹
    shutil.copy(ecimage_path + sep + 'index.txt',temp_path)

    #获取系统时间，并转换成14位的格式
    localtime = time.localtime()
    ctime = time.strftime("%Y%m%d%H%M%S",localtime)

    #获取普查小区代码
    cx.execute("select pcxqDeviceNo from task where taskID = ?",[taskid_output])
    pcxqDeivceNo = str(cx.fetchone()[0])


    #压缩包含图片及index.txt的文件夹，压缩后的文件名为前缀:PICTURE_ + 14位taskid + 2位普查小区代码+ 当前系统时间:ctime + 后缀：.zip
    output_zip = zipfile.ZipFile(path + sep + 'PICTURE_' + taskid_output + pcxqDeivceNo + ctime + '.zip' ,'w',zipfile.ZIP_DEFLATED)

    for root,dirs,files in os.walk(temp_path):
        for name in files:
            output_zip.write(name)


    #删除临时文件夹
    output_zip.close()
    shutil.rmtree(temp_path,ignore_errors=True)
    os.chdir(ecimage_path)
    os.rmdir(temp_path)


cu.close()
print 'sucess'
    



