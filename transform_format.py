import os
import numpy as np
import torch
import torch.nn as nn
from meshsegnet import *
import vedo

filepath = "C:\\Users\\xuzih\\Desktop\\tmp_test_vtp\\u"
outpath = "C:\\Users\\xuzih\\Desktop\\ds"
count = 1


tmplist = os.listdir(filepath)
namelist = []
for item in tmplist:
    namelist.append(item)

for name in namelist:
    print('starting {}'.format(name))
    objpath = os.path.join(filepath, name)
    mesh = vedo.load(objpath)
    labels = mesh.getCellArray("Label")

    if not os.path.exists(outpath + '/tmp'):
        os.mkdir(outpath + '/tmp')

    tmp_path = os.path.join(outpath + '/tmp', 'tmp_{}.stl'.format(name[:-4]))
    vedo.write(mesh, tmp_path)

    mesh_n = vedo.load(tmp_path)
    mesh_n.addCellArray(labels, 'Label')
    vedo.write(mesh_n, os.path.join(outpath, '{0}.vtp'.format(name[:-4])))
    print('{} finished'.format(count))
    count += 1

print('all finished')

    #     tmp_path = os.path.join(outpath + '/tmp', 'tmp_{}.stl'.format(count))
    #     vedo.write(mesh_d, tmp_path)
    #
    #     mesh_n = vedo.load(tmp_path)
    #     mesh_n.addCellArray(fine_labels, 'Label')
    #
    #     vedo.write(mesh_n, outpath, 'downsample_{}.vtp'.format(count))
    #     print('{} finished'.format(count))
    #     count += 1
    #
    # print('all finished')