import os
import time
import threading

# path = "C:/Users/Administrator/AppData/Roaming/ClearBos/201905290004/Data2" #001文件夹目录
# path="E:\\clearbos\\TestServer\\PatientFiles"     #病例路径
# outpath="E:\\TESTS\\Cut\\AiData\\"                   #导出路径
# path="\\\\192.168.1.250\\UserData\\DataBaseDailyBackup\\DataBaseDailyBackup-FULL\\E\\clearbos\\TestServer\\PatientFiles"     #病例路径
# outpath="..\\data04\\"
# path = "C:\\Users\\xuzih\\AppData\\Roaming\\ClearBos"  # 病例路径
path = "C:\\Users\\xuzih\\Desktop\\tmp_test"
# outpath = "C:\\Users\\xuzih\\Desktop\\test_out_v1"
# path = "C:\\Users\\xuzih\\Desktop\\tmptest"  # 病例路径
outpath = "C:\\Users\\xuzih\\Desktop\\tmp_test_out"

# exePath = "C:\\Users\\xuzih\\Downloads\\AI_Splittooth\\AI_Splittooth\\ExportAIData\\4.3.4.0\\bin\\ClearShape.exe"  # 执行文件的绝对路径
# exePath = "./Release/ClearShape.exe"
exePath = "C:\\dev\\MeshSegNet\\Release\\ClearShape.exe"
# exePath = "C:\\Program Files (x86)\\ClearBos\\4.5.7.1\\bin\\ClearShape.exe"
# exePath = "C:\\dev\\clear\\Bin\\Release\\ClearShape.exe"

minStr = "200011240001"
maxStr = "202311250001"
# maxStr="201903140012"

TEST = 0  # all

fileCount = 0
fileTotalCount = 0

successCount = 0
failCount = 0


# 4处理文件
def ProFile(file):
    inputFile = file
    global outpath
    # 003 命令字符串
    cmd = "\"" + exePath + "\"" + " -f OutPutCutToothData -v 1 -i " + inputFile + " -o " + outpath
    print("\ncmd=", cmd, "\n")
    r_v = 0
    r_v = os.system(cmd)

    return file;


# 0 in
def IsRange(file, minStr, maxStr):
    if not TEST:
        return 0
    (filepath, tempfilename) = os.path.split(file)
    tempfilename = tempfilename.replace(".cbm", "");
    tempfilename = tempfilename.replace("m", "");
    print(tempfilename, minStr, maxStr)

    if (tempfilename < minStr):
        return -1
    elif (tempfilename > maxStr):
        return 1
    else:
        return 0


def eachFile(filepath, curCount, totalCount):
    fileNames = os.listdir(filepath)
    for file in fileNames:
        newDir = filepath + '/' + file
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".cbm":

                iRange = IsRange(file, minStr, maxStr)
                if (iRange < 0):
                    continue;
                elif (iRange > 0):
                    break;
                # 3处理文件
                if (curCount > totalCount):
                    return
                t1 = threading.Thread(target=ProFile, args=(newDir,));
                t1.start();
                t1.join();
                ProFile(newDir)
                curCount = curCount + 1
                print("{} finished".format(file))

        else:
            eachFile(newDir, curCount, totalCount)  # 如果不是文件，递归这个文件夹的路径


def eachFileGetTotalCount(filepath):
    fileNames = os.listdir(filepath)
    for file in fileNames:
        newDir = filepath + '/' + file
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".cbm":
                iRange = IsRange(file, minStr, maxStr)
                if (iRange < 0):
                    continue;
                elif (iRange > 0):
                    break;
                global fileTotalCount
                fileTotalCount = fileTotalCount + 1
        else:
            eachFileGetTotalCount(newDir)  # 如果不是文件，递归这个文件夹的路径


def GetLocalTimeStrs():
    localTime = time.localtime(time.time())
    localTimeStrs = time.strftime("%Y%m%d_%H%M%S", localTime)
    return localTimeStrs


# 1 入口函数
if __name__ == "__main__":
    localTimeStrs = GetLocalTimeStrs()
    print(localTimeStrs, "\n")
    # start
    logMsg = localTimeStrs + "\n" + path + "\n"

    # 2递归遍历 cbm文件
    # eachFileGetTotalCount(path)
    curCount = 0
    totalCount = 1000
    eachFile(path, curCount, totalCount)

    # end
    localTimeStrs = GetLocalTimeStrs()
    print(localTimeStrs, "\n")

    os.system("pause")
