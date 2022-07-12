from torch.utils.data import Dataset
import pandas as pd
import torch
import numpy as np
from vedo import *
# import numpy
from scipy.spatial import distance_matrix




# g = load(dataurl+'250.vtk')
# show(g)

#
# N = mesh.NCells()
# print(N)
#
# points = vtk2numpy(mesh.polydata().GetPoints().GetData())
# ids = vtk2numpy(mesh.polydata().GetPolys().GetData()).reshape((N, -1))[:,1:]
# cells = points[ids].reshape(N, 9).astype(dtype='float32')
#
# v1 = np.zeros([mesh.NCells(), 3], dtype='float32')
# v2 = np.zeros([mesh.NCells(), 3], dtype='float32')
# # print(v1)
# # print(v2)
# v1[:, 0] = cells[:, 0] - cells[:, 3]
# v1[:, 1] = cells[:, 1] - cells[:, 4]
# v1[:, 2] = cells[:, 2] - cells[:, 5]
# v2[:, 0] = cells[:, 3] - cells[:, 6]
# v2[:, 1] = cells[:, 4] - cells[:, 7]
# v2[:, 2] = cells[:, 5] - cells[:, 8]
#
# # print(cells[0])
# print(mesh.centerOfMass())


# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# print(device)

# conv1 = torch.nn.Conv1d(4, 8, 1)
# print(conv1)
# input = torch.randn(4,5)
# print(input)
# output = conv1(input)
# print(output)

# x = torch.randn(4,5)
# print(x)
# print(x.view(1,5,4))

# mesh = load(['C:\\Users\\DELL\\Desktop\\l.stl'])
# show(mesh)
# # labels = mesh.getCellArray('Label').astype('int32').reshape(-1, 1)
# # print(labels)
# N = mesh.NCells()
# print(N)
# points = vtk2numpy(mesh.polydata().GetPoints().GetData())
# print(points[0:5])
# ids = vtk2numpy(mesh.polydata().GetPolys().GetData()).reshape((N, -1))[:,1:]
# labels = mesh.getCellArray('Label').astype('int32').reshape(-1, 1)
# cells = points[ids].reshape(N, 9).astype(dtype='float32')
# print(ids[0:10])
# print(cells[0:10])

# print("hello, world")

# mesh = load(["C:\\dev\\MeshSegNet\\outputs\\tmp\\l_201911070015_predicted_refined.vtp"])
# show(mesh)

# mesh = load(["C:\\dev\\MeshSegNet\\outputs\\new\\l_predicted_refined.vtp"])
# show(mesh)

# mesh = load(["C:\\Users\\DELL\\Desktop\\STL_2\\201911070015\\l_201911070015.stl"])
# show(mesh)

# mesh = load(["C:\\dev\\MeshSegNet\\outputs\\final\\l_202006060009_predicted_refined.vtp"])
# show(mesh)

# mesh = load(["C:\\dev\\MeshSegNet\\l_202006080008.stl"])
# show(mesh)

# mesh = load(["C:\\dev\\MeshSegNet\\outputs\\test\\u_201911070015_predicted_refined.vtp"])
# a = mesh.getCellArray('Label')
# print(max(a))

# import utils
# global plotter
# model_name = "test"
# plotter = utils.VisdomLinePlotter(env_name=model_name)
#
# n = 10
# epoch = 0
# for i in range(n):
#     plotter.plot('Loss', 'train', 'class Loss', epoch, 0.5*i)
#     plotter.plot('DSC', 'train', 'asDSC', epoch, 0.5*i + 1)
#     # plotter.plot('SEN', 'train', 'asSEN', epoch, i)
#     # plotter.plot('PPV', 'train', 'asPPV', epoch, i + 1)
#     plotter.plot('Loss', 'val', 'class Loss', epoch, 0.5*i + 2)
#     # plotter.plot('DSC', 'val', 'DSC', epoch, 0.5*i + 2)
#     # plotter.plot('SEN', 'val', 'SEN', epoch, i + 2)
#     # plotter.plot('PPV', 'val', 'PPV', epoch, i + 3)
#     epoch += 1

# mesh = load(["C:\\dev\\MeshSegNet\\outputs\\test\\l_201911070015_new_predicted_refined_n.vtp"])
# labels = mesh.getCellArray('Label').astype('int32')
# N = mesh.NCells()
# points = vtk2numpy(mesh.polydata().GetPoints().GetData())
# ids = vtk2numpy(mesh.polydata().GetPolys().GetData()).reshape((N, -1))[:,1:]
# cells = points[ids].reshape(N, 9).astype(dtype='float32')
# memo = {}
# for item in labels:
#     if item not in memo:
#         memo[item] = 0
#     else:
#         memo[item] += 1
# print(memo)
# print(N)
# print(len(cells))
# print(len(points))

# show(mesh)
# print(labels)
# print(type(labels))


# mesh = load(["C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos\\202007270042\\test\\new_test.vtp"])
# show(mesh)


# mesh = load(["C:\\dev\\MeshSegNet\\outputs\\test\\l_201911070015_new_predicted_refined_n.vtp"])
# mesh = load(["C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos\\202007270042\\test\\new_test.vtp"])
# labels = mesh.getCellArray('Label').astype('int32').reshape(-1, 1)
# N = mesh.NCells()
# points = vtk2numpy(mesh.polydata().GetPoints().GetData())
# ids = vtk2numpy(mesh.polydata().GetPolys().GetData()).reshape((N, -1))[:,1:]
# cells = points[ids].reshape(N, 9).astype(dtype='float32')
# tmp = vtk2numpy(mesh.polydata().GetPolys().GetData()).reshape((N, -1))[:,1:]
# print(tmp)


# tstr = "m123123_l"
#
# print(tstr[1:-2])

# filepath = "C:\\Users\\xuzih\\Desktop\\cbm_out"
# tmplist = os.listdir(filepath)
# namelist = []
# for item in tmplist:
#     namelist.append(item[1:-4])
# namelist = list(set(namelist))
#
# tmpname = 'abc'
#
# test = os.path.join(filepath, 'm{}.obj'.format(tmpname))
#
# print(test)

# import vedo
# # mesh = vedo.load("C:\\dev\\MeshSegNet\\outputs\\final\\l_201911070015_predicted_refined.vtp")
# # mesh = vedo.load("C:\\dev\\MeshSegNet\\downsample_test.vtp")
# # mesh = vedo.load("C:\\dev\\MeshSegNet\\downsample_test_2.vtp")
# # mesh = vedo.load("C:\\dev\\MeshSegNet\\A0_Sample_026_d.vtp")
# # mesh2 = vedo.load("C:\\dev\\MeshSegNet\\tmp_test.stl")
# # mesh = vedo.load("C:\\Users\\xuzih\\Desktop\\cbm_out\\m202203050057_l.obj")
# mesh = vedo.load("C:\\Users\\xuzih\\Desktop\\trans\\new_3.vtp")
#
# n = mesh.NCells()
# m = mesh.NPoints()
#
# print(n, m)


# label = mesh.getCellArray("Label")
# mesh2.addCellArray(label, 'Label')
#
#
# vedo.write(mesh2, "./tmp_test_2.vtp")


# mesh = load(["C:\\dev\\MeshSegNet\\outputs\\test\\l_201911070015_new_predicted_refined_n.vtp"])
#
# print(mesh.polydata())


# filepath = "C:\\Users\\xuzih\\Desktop\\valid_set\\normal\\u"
# # # filepath = "C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos"
# #
# tmplist = os.listdir(filepath)
# namelist = []
# for item in tmplist:
#     namelist.append(item)
#
# print(namelist)


# full_list = ['202202220056', '202203150047', '202204030045', '202204040016', '202204070023', '202204090007', '202204090035', '202204110020', '202204130002', '202204140012', '202204150022', '202204150024', '202204160040', '202204170001', '202204170028', '202204170034', '202204170048', '202204180001', '202204180011', '202204180051', '202204180058', '202204190004', '202204200007', '202206060063']
#
# filepath = "C:\\Users\\xuzih\\Desktop\\valid_set\\kids\\l"
# tmplist = os.listdir(filepath)
# rest = []
# for item in full_list:
#     if item + "_l.vtp" not in tmplist:
#         rest.append(item)
#
# print(rest)
import torch.nn as nn
from meshsegnet import *
import vedo
import pandas as pd
from losses_and_metrics_for_mesh import *
from scipy.spatial import distance_matrix
import scipy.io as sio
import shutil
import time
from sklearn.svm import SVC # uncomment this line if you don't install thudersvm
# from thundersvm import SVC # comment this line if you don't install thudersvm
from sklearn.neighbors import KNeighborsClassifier
from pygco import cut_from_graph


# sample = "C:\\Users\\xuzih\\Desktop\\valid_set\\normal\\l\\202204180007_l.vtp"
#
# mesh = vedo.load(sample)
# refine_labels = mesh.getCellArray("Label").reshape([-1, 1])
#
# print('\tDownsampling...{0}')
# target_num = 10000
# ratio = target_num / mesh.NCells()  # calculate ratio
# mesh_d = mesh.clone()
# mesh_d.decimate(fraction=ratio)
# # mesh_d.decimate(fraction=ratio, method='pro', boundaries=True)
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
# # neigh.fit(mesh2.cells, np.ravel(refine_labels))
# # fine_labels = neigh.predict(fine_cells)
#
# neigh.fit(barycenters, np.ravel(refine_labels))
# fine_labels = neigh.predict(fine_barycenters)
# fine_labels = fine_labels.reshape(-1, 1)
#
# mesh_d.addCellArray(fine_labels, 'Label')
# vedo.write(mesh_d, "C:\\Users\\xuzih\\Desktop\\d_t\\202204180007_l_test_ori.vtp")

# import vedo
# #
mesh = vedo.load('C:\\dev\\MeshSegNet\\outputs_17_l\\final\\201910080029_l_predicted_refined.vtp')

vedo.write(mesh, 'C:\\Users\\xuzih\\Desktop\\201910080029_l.obj')
# n = mesh.NCells()
# pn = mesh.NPoints()
# labels = mesh.getCellArray('Label')
# print(n)
# print(pn)
# print(len(labels))


f = mesh.faces()

print(f)

f = mesh.faces()
print(len(f))
labels = mesh.getCellArray('Label')

file = open('C:\\Users\\xuzih\\Desktop\\test.seg', 'w')
for i in range(len(f)):
    for _ in range(3):
        file.write(str(labels[i]) + '\n')
for _ in range(2):
    for label in labels:
        file.write(str(label) + '\n')

file.close()

# memo = {}
# count = 0
# with open("C:\\Users\\xuzih\\Desktop\\test\\m201910080029_l.seg", 'r') as f:
#     for line in f.readlines():
#         count += 1
#         if count > 263538 and count < 351384:
#         # if count > 351384:
#             line = line.strip('\n')
#             if line not in memo:
#                 memo[line] = 1
#             else:
#                 memo[line] += 1
#
# print(memo)
# print(count)