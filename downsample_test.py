import os
import numpy as np
import torch
import torch.nn as nn
from meshsegnet import *
import vedo
import pandas as pd
from losses_and_metrics_for_mesh import *
from scipy.spatial import distance_matrix
import scipy.io as sio
import shutil
import time
# from sklearn.svm import SVC # uncomment this line if you don't install thudersvm
# from thundersvm import SVC # comment this line if you don't install thudersvm
from sklearn.neighbors import KNeighborsClassifier
from pygco import cut_from_graph


# mesh = vedo.load("C:\\dev\\MeshSegNet\\tmp_test_2.vtp")
#
# refine_labels = mesh.getCellArray("Label").reshape([-1, 1])
#
#
#
# print('\tDownsampling...')
# target_num = 10000
# ratio = target_num/mesh.NCells() # calculate ratio
# mesh_d = mesh.clone()
# mesh_d.decimate(fraction=ratio)
#
# # get fine_cells
# cells = np.zeros([mesh.NCells(), 9], dtype='float32')
# for i in range(len(cells)):
#     cells[i][0], cells[i][1], cells[i][2] = mesh.polydata().GetPoint(
#         mesh.polydata().GetCell(i).GetPointId(0))  # don't need to copy
#     cells[i][3], cells[i][4], cells[i][5] = mesh.polydata().GetPoint(
#         mesh.polydata().GetCell(i).GetPointId(1))  # don't need to copy
#     cells[i][6], cells[i][7], cells[i][8] = mesh.polydata().GetPoint(
#         mesh.polydata().GetCell(i).GetPointId(2))  # don't need to copy
#
# fine_cells = cells
#
# barycenters = mesh.cellCenters()  # don't need to copy
# fine_barycenters = mesh_d.cellCenters()  # don't need to copy
#
# neigh = KNeighborsClassifier(n_neighbors=3)
# # train KNN
# #neigh.fit(mesh2.cells, np.ravel(refine_labels))
# #fine_labels = neigh.predict(fine_cells)
#
# neigh.fit(barycenters, np.ravel(refine_labels))
# fine_labels = neigh.predict(fine_barycenters)
# fine_labels = fine_labels.reshape(-1, 1)
#
# mesh_d.addCellArray(fine_labels, 'Label')
# vedo.write(mesh_d, './downsample_test_2.vtp')




filepath = "C:\\Users\\xuzih\\Desktop\\u_27_trans"
outpath = "C:\\Users\\xuzih\\Desktop\\u_27_downsample"
count = 1



tmplist = os.listdir(filepath)
namelist = []
for item in tmplist:
    namelist.append(item)

for name in namelist:
    objpath = os.path.join(filepath, name)
    mesh = vedo.load(objpath)

    # label = mesh.getCellArray('Label')
    # mesh_f = mesh.clone(deep=True).mirror("x")
    # label_f = mesh_f.getCellArray('Label')
    # for i in range(1, 17):
    #     if len(label_f == i) > 0:
    #         label_f[label == i] = 17 - i  # 1 -> 16, 2 -> 15, ..., 16 -> 1
    #
    # write(mesh, os.path.join(outpath, 'Sample_0{0}_d.vtp'.format(count)))
    # write(mesh_f, os.path.join(outpath, 'Sample_0{0}_d.vtp'.format(count + 1000)))
    # count += 1

    refine_labels = mesh.getCellArray("Label").reshape([-1, 1])

    print('\tDownsampling...{0}'.format(count))
    target_num = 10000
    ratio = target_num / mesh.NCells()  # calculate ratio
    mesh_d = mesh.clone()
    mesh_d.decimate(fraction=ratio)

    # get fine_cells
    cells = np.zeros([mesh.NCells(), 9], dtype='float32')
    for i in range(len(cells)):
        cells[i][0], cells[i][1], cells[i][2] = mesh.polydata().GetPoint(
            mesh.polydata().GetCell(i).GetPointId(0))  # don't need to copy
        cells[i][3], cells[i][4], cells[i][5] = mesh.polydata().GetPoint(
            mesh.polydata().GetCell(i).GetPointId(1))  # don't need to copy
        cells[i][6], cells[i][7], cells[i][8] = mesh.polydata().GetPoint(
            mesh.polydata().GetCell(i).GetPointId(2))  # don't need to copy

    fine_cells = cells

    barycenters = mesh.cellCenters()  # don't need to copy
    fine_barycenters = mesh_d.cellCenters()  # don't need to copy

    neigh = KNeighborsClassifier(n_neighbors=3)
    # train KNN
    # neigh.fit(mesh2.cells, np.ravel(refine_labels))
    # fine_labels = neigh.predict(fine_cells)

    neigh.fit(barycenters, np.ravel(refine_labels))
    fine_labels = neigh.predict(fine_barycenters)
    fine_labels = fine_labels.reshape(-1, 1)

    mesh_d.addCellArray(fine_labels, 'Label')
    vedo.write(mesh_d,  os.path.join(outpath, '{}.vtp'.format(name[:-4])))
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

