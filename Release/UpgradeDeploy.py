#!/usr/bin/python
# -*- coding: UTF-8 -*-

#1.拷贝文件
#2.生成 UpdateList.txt

import os
import shutil

inputDir = ".\\";
outputDir = "..\\Upgrade\\4.5.0.0\\";

outputListFileName = outputDir+ "UpdateList.txt";


excludes = [".exp",".iss",".iobj",".ipdb",".lib",".pdb",".py",".reg"];#排除后缀
excludesDir = ["Help","publish"];                                     #排除目录

#includes = [".att",".dll",".ttf",".bmp",".jpg"];

def eachFile(filepath,prefix,fileList):
    pathDir = os.listdir(filepath)                   #获取当前路径下的文件名，返回List
    for s in pathDir:
        if s.startswith('.'):
            continue;
        newDir=os.path.join(filepath,s)              #将文件命加入到当前文件路径后面
        if os.path.isfile(newDir) :                  #如果是文件
            extension = os.path.splitext(newDir)[1]; #获取扩展名
            if extension not in  excludes:                  #判断是否是txt
                fileList.append(prefix+s)
                pass
        else:
            if prefix +s in excludesDir:
                continue;
            prefix1 = prefix +s +"\\"
            eachFile(newDir,prefix1,fileList)                #如果不是文件，递归这个文件夹的路径
            pass

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
       # print "%s not exist!"%(srcfile)
       pass
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
       # print "copy %s -> %s"%( srcfile,dstfile)
        
if __name__ == '__main__':
    fileList = [];
    eachFile(inputDir,"",fileList)


    isExists=os.path.exists(outputDir)
    if  isExists:
        shutil.rmtree(outputDir);
        
    isExists=os.path.exists(outputDir)
    if  not isExists:
        os.makedirs(outputDir)
        
    fp = open(outputListFileName,'w+');
    
    for s in fileList:
        fp.write(s+"\n");
        mycopyfile(inputDir+s,outputDir+s); 
        print (s)

    fp.close();
    #os.system("pause")
