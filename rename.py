import os

# # 图片存放的路径
# path = "C:\\Users\\xuzih\\Desktop\\pre_train\\l\\t"
#
# # 遍历更改文件名
# num = 1
# f_n = 1
# for file in os.listdir(path):
#     if num < 132:
#         os.rename(os.path.join(path,file),os.path.join(path,'Sample_0{0}_d.vtp'.format(num)))
#         num += 1
#     else:
#         os.rename(os.path.join(path,file),os.path.join(path,'Sample_0{0}_d.vtp'.format(f_n + 1000)))
#         f_n += 1

# # 图片存放的路径
# path = "C:\\Users\\xuzih\\Desktop\\pre_train\\l\\t"
#
# # 遍历更改文件名
# num = 1
# f_n = 1
# for file in os.listdir(path):
#     os.rename(os.path.join(path,file),os.path.join(path,'Sample_0{0}_d.vtp'.format(num)))
#     num += 1


# 图片存放的路径
path = "C:\\Users\\xuzih\\Desktop\\rename"

# 遍历更改文件名
num = 1
f_n = 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,'Sample_0{0}_d.vtp'.format(num)))
    num += 1

# # 图片存放的路径
# path = "C:\\Users\\xuzih\\Desktop\\rename"
#
# # 遍历更改文件名
# num = 1
# f_n = 1
# for file in os.listdir(path):
#     os.rename(os.path.join(path,file),os.path.join(path,'{0}.vtp'.format(num)))
#     num += 1


# # 图片存放的路径
# path = "C:\\dev\\MeshSegNet\\src"
#
# # 遍历更改文件名
# num = 1
# f_n = 1
# for file in os.listdir(path):
#     os.rename(os.path.join(path,file),os.path.join(path,'Sample_0{0}_d.vtp'.format(num)))
#     num += 1
#
# # 图片存放的路径
# path = "C:\\dev\\MeshSegNet\\src"
#
# # 遍历更改文件名
# num = 1
# f_n = 1
# for file in os.listdir(path):
#     os.rename(os.path.join(path,file),os.path.join(path,'{}'.format(num)))
#     num += 1