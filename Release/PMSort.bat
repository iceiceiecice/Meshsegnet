
echo %1
cd /d "%1"

dir *U*_CUT.igs /B /OD > PMReadFileList.txt & dir *L*_CUT.igs /B /OD >> PMReadFileList.txt

::pause

