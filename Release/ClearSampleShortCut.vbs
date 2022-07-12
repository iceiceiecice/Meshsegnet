currentpath = createobject("Scripting.FileSystemObject").GetFolder(".").Path
set WshShell=WScript.CreateObject("WScript.Shell")
strDesktop=WshShell.SpecialFolders("Desktop")
set oShellLink=WshShell.CreateShortcut(strDesktop & "\可丽尔博士病例查看器.lnk")
oShellLink.TargetPath=currentpath+"\ClearSample.exe" 
oShellLink.WindowStyle=3
oShellLink.IconLocation=currentpath+"\publish\icons\ClearSite_Offline.ico,0"
oShellLink.Description="可丽尔博士病例查看器快捷方式"
oShellLink.WorkingDirectory=strDesktop
oShellLink.Save