currentpath = createobject("Scripting.FileSystemObject").GetFolder(".").Path
set WshShell=WScript.CreateObject("WScript.Shell")
strDesktop=WshShell.SpecialFolders("Desktop")
set oShellLink=WshShell.CreateShortcut(strDesktop & "\��������ʿ�����鿴��.lnk")
oShellLink.TargetPath=currentpath+"\ClearSample.exe" 
oShellLink.WindowStyle=3
oShellLink.IconLocation=currentpath+"\publish\icons\ClearSite_Offline.ico,0"
oShellLink.Description="��������ʿ�����鿴����ݷ�ʽ"
oShellLink.WorkingDirectory=strDesktop
oShellLink.Save