import os
import pathlib
import sys
import glob
import h5py
import numpy as np
import torch
import json
import wget

# url = 'http://patientfiles.clearbos.com/201701180001/Data3/m201701180001.cbm'
# wget.download(url)
# path = "C:\\Users\\xuzih\\Downloads"

# wget.download(url,path)

dir_path = 'C:\\Users\\xuzih\\Downloads\\cbm'

url_head = 'http://patientfiles.clearbos.com'

name_list_file = 'C:\\Users\\xuzih\\Desktop\\kids.txt'
name_list = []

with open(name_list_file, 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        name_list.append(str(line))

total_num = len(name_list)

for i in range(total_num):
    tmp_path = url_head + '/' + name_list[i]
    for j in range(10, 0, -1):
        final_path = tmp_path + '/Data{0}'.format(j) + '/m{0}.cbm'.format(name_list[i])
        try:
            print('try to download Data{0}'.format(j))
            wget.download(final_path, dir_path)
            break
        except:
            print('{0} not exist'.format(final_path))
            continue

    print("{0} / {1} finished".format(i + 1, total_num))

# url = 'http://patientfiles.clearbos.com/201701180001/Data3/m201701180001.cbm'
#
# print(wget.detect_filename('http://patientfiles.clearbos.com/201701180001/Data3'))

import urllib3

# wget.download()
