import os
from vedo import *


filepath = "C:\\Users\\xuzih\\Desktop\\downsample"
outpath = "C:\\Users\\xuzih\\Desktop\\pre_train\\17class_104sample_downsample"
count = 1



tmplist = os.listdir(filepath)
namelist = []
for item in tmplist:
    namelist.append(item)

for name in namelist:
    objpath = os.path.join(filepath, name)
    mesh = load(objpath)

    label = mesh.getCellArray('Label')
    mesh_f = mesh.clone(deep=True).mirror("x")
    label_f = mesh_f.getCellArray('Label')
    for i in range(1, 17):
        if len(label_f == i) > 0:
            label_f[label == i] = 17 - i  # 1 -> 16, 2 -> 15, ..., 16 -> 1

    write(mesh, os.path.join(outpath, 'Sample_0{0}_d.vtp'.format(count)))
    write(mesh_f, os.path.join(outpath, 'Sample_0{0}_d.vtp'.format(count + 1000)))
    count += 1

