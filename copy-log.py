import os
import sys
import shutil

source_dir = r'Z:\Data-month-statistics'
target_dir = r'C:\Users\chensq\Desktop\copyfile'
file_format = '.log'

with open('input.txt') as a:
    file_waiting_copy = a.readlines()
    file_waiting_copy = [x.strip()+file_format for x in file_waiting_copy if x != '\n']
    a.close()

for file in file_waiting_copy:
    print(file)
    a = file.split('-')[0]
    a = str(a)
    a = a[0:4]
    if a[2:4] == '12':
        b = str(int(a[0:2])+1)+'01'
    else:
        b = int(a) + 1
        b = str(b)
    source_dir_1 = source_dir + '/20' + a
    source_dir_2 = source_dir + '/20' + b
    for dirpath, dirnames, filenames in os.walk(source_dir_1):
        if file in filenames:
            source_path = str(dirpath) + r'/' + str(file)
            shutil.copy(source_path, target_dir)
            print(file + '复制完成1')
    for dirpath, dirnames, filenames in os.walk(source_dir_2):
        if file in filenames:
            source_path = str(dirpath) + r'/' + str(file)
            shutil.copy(source_path, target_dir)
            print(file + '复制完成2')
input('输入任意内容继续')