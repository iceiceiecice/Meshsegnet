from vedo import *
import os

# normal
# src = "C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos\\202007270042\\test\\m202007270042_l.seg"
# mesh = load(["C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos\\202007270042\\test\\m202007270042_l.obj"])
# # mesh = load(["C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos\\202007270042\\test\\new.vtp"])
# N = mesh.NCells()
# points = vtk2numpy(mesh.polydata().GetPoints().GetData())
# ids = vtk2numpy(mesh.polydata().GetPolys().GetData()).reshape((N, -1))[:,1:]
# cells = points[ids].reshape(N, 9).astype(dtype='float32')
# print(N)
# print(len(points))
# print(len(ids))
# print(len(cells))
# filea = open(src)
# tmp = []
# for line in filea:
#     a = line.strip()
#     tmp.append(int(a))
# # print(tmp)
# print(len(tmp))
# labels = np.zeros([len(cells), 1], dtype=np.int32)
#
# for i in range(len(cells)):
#     labels[i] =tmp[i+214062]
#
# mesh.addCellArray(labels, 'Label')
#
# write(mesh, "C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos\\202007270042\\test\\new_test.vtp")

filepath = "C:\\Users\\xuzih\\Desktop\\tmp_test_out"
outpath = "C:\\Users\\xuzih\\Desktop\\tmp_test_vtp"
count_l = 1
count_u = 1

def getlist():
    global filepath
    tmplist = os.listdir(filepath)
    namelist = []
    for item in tmplist:
        namelist.append(item[1:-4])
    namelist = list(set(namelist))
    return namelist

# trans
def trans(name):
    global filepath
    global outpath
    global count_l
    global count_u
    src = os.path.join(filepath, 'm{}.seg'.format(name))
    objpath = os.path.join(filepath, 'm{}.obj'.format(name))
    mesh = load(objpath)
    # src = "C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos\\202204170063\\m202204170063_l.seg"
    # mesh = load(["C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos\\202204170063\\m202204170063_l.obj"])
    # mesh = load(["C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos\\202007270042\\test\\new.vtp"])
    N = mesh.NCells()
    points = vtk2numpy(mesh.polydata().GetPoints().GetData())
    ids = vtk2numpy(mesh.polydata().GetPolys().GetData()).reshape((N, -1))[:,1:]
    cells = points[ids].reshape(N, 9).astype(dtype='float32')
    n = len(points)

    filea = open(src)
    tmp = []
    for line in filea:
        a = line.strip()
        tmp.append(int(a))
    labels = np.zeros([len(cells), 1], dtype=np.int32)

    for i in range(len(cells)):
        if tmp[i + n] == 0:
            labels[i] = 0
        elif tmp[i + n] == 38 or tmp[i + n] == 18:
            labels[i] = 1
        elif tmp[i + n] == 37 or tmp[i + n] == 17:
            labels[i] = 2
        elif tmp[i + n] == 36 or tmp[i + n] == 16:
            labels[i] = 3
        elif tmp[i + n] == 35 or tmp[i + n] == 15:
            labels[i] = 4
        elif tmp[i + n] == 34 or tmp[i + n] == 14:
            labels[i] = 5
        elif tmp[i + n] == 33 or tmp[i + n] == 13:
            labels[i] = 6
        elif tmp[i + n] == 32 or tmp[i + n] == 12:
            labels[i] = 7
        elif tmp[i + n] == 31 or tmp[i + n] == 11:
            labels[i] = 8
        elif tmp[i + n] == 41 or tmp[i + n] == 21:
            labels[i] = 9
        elif tmp[i + n] == 42 or tmp[i + n] == 22:
            labels[i] = 10
        elif tmp[i + n] == 43 or tmp[i + n] == 23:
            labels[i] = 11
        elif tmp[i + n] == 44 or tmp[i + n] == 24:
            labels[i] = 12
        elif tmp[i + n] == 45 or tmp[i + n] == 25:
            labels[i] = 13
        elif tmp[i + n] == 46 or tmp[i + n] == 26:
            labels[i] = 14
        elif tmp[i + n] == 47 or tmp[i + n] == 27:
            labels[i] = 15
        elif tmp[i + n] == 48 or tmp[i + n] == 28:
            labels[i] = 16
        elif tmp[i + n] == 75 or tmp[i + n] == 55:
            labels[i] = 17
        elif tmp[i + n] == 74 or tmp[i + n] == 54:
            labels[i] = 18
        elif tmp[i + n] == 73 or tmp[i + n] == 53:
            labels[i] = 19
        elif tmp[i + n] == 72 or tmp[i + n] == 52:
            labels[i] = 20
        elif tmp[i + n] == 71 or tmp[i + n] == 51:
            labels[i] = 21
        elif tmp[i + n] == 81 or tmp[i + n] == 61:
            labels[i] = 22
        elif tmp[i + n] == 82 or tmp[i + n] == 62:
            labels[i] = 23
        elif tmp[i + n] == 83 or tmp[i + n] == 63:
            labels[i] = 24
        elif tmp[i + n] == 84 or tmp[i + n] == 64:
            labels[i] = 25
        elif tmp[i + n] == 85 or tmp[i + n] == 65:
            labels[i] = 26

    mesh.addCellArray(labels, 'Label')
    # label = mesh.getCellArray('Label')
    # mesh_f = mesh.clone(deep=True).mirror("x")
    # label_f = mesh_f.getCellArray('Label')
    # for i in range(1, 17):
    #     if len(label_f == i) > 0:
    #         label_f[label == i] = 17 - i  # 1 -> 16, 2 -> 15, ..., 16 -> 1

    outpath_l = os.path.join(outpath, 'l')
    outpath_u = os.path.join(outpath, 'u')
    if not os.path.exists(outpath_l):
        os.mkdir(outpath_l)
    if not os.path.exists(outpath_u):
        os.mkdir(outpath_u)

    # if name[-1] == 'l':
    #     write(mesh, os.path.join(outpath_l, 'Sample_0{0}_d.vtp'.format(count_l)))
    #     write(mesh_f, os.path.join(outpath_l, 'Sample_0{0}_d.vtp'.format(count_l + 1000)))
    #     count_l += 1
    # if name[-1] == 'u':
    #     write(mesh, os.path.join(outpath_u, 'Sample_0{0}_d.vtp'.format(count_u)))
    #     write(mesh_f, os.path.join(outpath_u, 'Sample_0{0}_d.vtp'.format(count_u + 1000)))
    #     count_u += 1

    if name[-1] == 'l':
        write(mesh, os.path.join(outpath_l, '{0}.vtp'.format(name)))
        # write(mesh_f, os.path.join(outpath_l, 'Sample_0{0}_d.vtp'.format(count_l + 1000)))
        count_l += 1
    if name[-1] == 'u':
        write(mesh, os.path.join(outpath_u, '{0}.vtp'.format(name)))
        # write(mesh_f, os.path.join(outpath_u, 'Sample_0{0}_d.vtp'.format(count_u + 1000)))
        count_u += 1

    print('Sample filename: {} completed'.format(name))

    return True


if __name__ == "__main__":
    namelist = getlist()
    for name in namelist:
        trans(name)
    print("cout_l: ", count_l)
    print("cout_u: ", count_u)
    print('finished')
