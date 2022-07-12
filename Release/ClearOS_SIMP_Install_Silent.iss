; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "ClearOS"
#define MyAppVersion "4.5.5.3"
#define MyAppPublisher "ClearMed Corp. Copyright(c) 2020"
#define MyAppURL "http://www.clearbos.com/"
#define MyAppExeName "ClearOS Installer"
#define MyAppExeNameA "ClearShape.exe"
#define MyAppExeNameB "ClearDesign.exe"
#define MyAppExeNameC "ClearWork.exe"
#define MyAppExeNameD "ClearCheck.exe"
#define MutexName "ClearMutexName"
#define MyMedicineICO  "Medicine.ico"
#define MyOnlineICO  "ClearSite_online.ico"
#define MyOfflineICO  "ClearSite_Offline.ico"
#define MyModelICO    "Model.ico"
#define ResourcesPath ".\publish\*"
#define AppData GetEnv('APPDATA')
#define OutputFilename "ClearOS_SIMP_Silent"

#define MyDateTimeString GetDateTimeString('yymmdd_hhnnss', '', '')



[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{AAD39D90-7727-48BD-9F41-8F8421917CC1}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
VersionInfoVersion={#MyAppVersion}
VersionInfoCopyright={#MyAppPublisher}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
UsePreviousAppDir=No
DefaultDirName={pf}\ClearBos\{#MyAppVersion}
DefaultGroupName={#MyAppVersion}
LicenseFile=.\publish\license.txt
;InfoAfterFile=.\readme.txt
OutputDir=..\
OutputBaseFilename={#OutputFilename}
;安装图标
SetupIconFile=.\publish\file.ico
;Compression=lzma/Max
;SolidCompression=true
Compression=lzma
SolidCompression=yes
WizardImageBackColor=$FFFFFF
WindowVisible=false
BackColor=clFuchsia
WizardImageStretch=false
PrivilegesRequired=admin
AppMutex={#MutexName}
DirExistsWarning=no
DisableDirPage=yes
Versioninfodescription={#MyAppName} 安装程序
VersionInfoCompany=http://www.clearbos.com/


[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: fileassoc; Description: CBM文件与{#MyAppName}关联; GroupDescription: 附加任务选项; Flags: unchecked
;Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
;Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1


[Dirs]
Name: "{app}" ; Permissions: everyone-modify

[Messages]
//BeveledLabel=可丽尔博士   //安装过程中显示文本信息
   DiskSpaceMBLabel=剩余磁盘空间至少要有 [mb] MB。

[Files]
; fold
;资源文件，安装向导
Source: ".\Attachment\*"; DestDir: "{app}\bin\Attachment"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\OfflineBrowse\*"; DestDir: "{app}\bin\OfflineBrowse"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\OfflineBrowse\images\*"; DestDir: "{app}\bin\OfflineBrowse\images"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: {#ResourcesPath}; DestDir: {tmp}; Flags: dontcopy solidbreak ; Attribs: hidden system
Source: ".\publish\icons\*"; DestDir: "{app}\bin\publish\icons"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\Root\*"; DestDir: "{app}\bin\Root"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\Template\*"; DestDir: "{app}\bin\Template"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\ToothMoveDiff.cfg"; DestDir: "{app}\bin"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\platforms\*"; DestDir: "{app}\bin\platforms"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\imageformats\*"; DestDir: "{app}\bin\imageformats"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ".\yanshi\*"; DestDir: "{userappdata}\..\Roaming\ClearBos\"; Flags: ignoreversion recursesubdirs createallsubdirs
;Source: ".\assert\*"; DestDir: "{app}\bin\assert"; Flags: ignoreversion recursesubdirs createallsubdirs

; font
Source: ".\arial.ttf"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\msyhbd.ttf"; DestDir: "{app}\bin"; Flags: ignoreversion

; text
Source: ".\server.xml"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\ColorConfig.ini"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\ColorRenderGum.ini"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\ColorRenderJaw.ini"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\ColorRenderTooth.ini"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\log4cplus.properties"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\ClearSample.ini"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\Log4cxxConfig-ClearCheck.xml"; DestDir: "{app}\bin"; Flags: ignoreversion

; picture
Source: ".\bkg.bmp"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\gum.bmp"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\teeth.bmp"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\LVLogo.png"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\bkgClearCheck.bmp"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\GumImagebump.png"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\GumImageredwhite.png"; DestDir: "{app}\bin"; Flags: ignoreversion
; exe
Source: ".\CBAutoUpdate.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CBOfflineBrowser.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\ClearCheck.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
;Source: ".\ClearDesign.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
;Source: ".\ClearShape.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
;Source: ".\ClearWork.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\ClearSample.exe"; DestDir: "{app}\bin"; Flags: ignoreversion

;bat
Source: ".\PMSort.bat"; DestDir: "{app}\bin"; Flags: ignoreversion

; dll
Source: ".\avcodec-56.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\avdevice-56.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\avfilter-5.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\avformat-56.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\avutil-54.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbControlLib.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbFileTransferLib.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbKits.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbMathLib.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbNurbsLib.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbOrthoLib.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbRenderLib.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbArrayToothLib.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\glew32.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\LZMA.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\swresample-1.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\swscale-3.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\log4cplusU.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbApplicationLayer.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\FreeImage.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\postproc-53.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\Qt5Core.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\Qt5Gui.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\Qt5Widgets.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\tinyxml2d.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbProduct.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\freetype.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\ucrtbased.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\vcruntime140d.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\log4cxx.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CGAL_Core-vc140-mt-4.13.1.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CGAL_ImageIO-vc140-mt-4.13.1.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CGAL_Qt5-vc140-mt-4.13.1.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CGAL_Qt5-vc140-mt-gd-4.13.1.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CGAL-vc140-mt-4.13.1.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CGAL-vc140-mt-gd-4.13.1.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\CbCGALib.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\libgmp-10.dll"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: ".\libmpfr-4.dll"; DestDir: "{app}\bin"; Flags: ignoreversion

; assert exe
Source: ".\publish\vc_redist.x86.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall;
Source: ".\publish\file.ico"; DestDir: "{app}"; Flags: deleteafterinstall;

[Registry] 
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearShape"; ValueType: string; ValueName:;ValueData: "WebClearShape";Flags: CreateValueIfDoesntExist UninsDeleteKey;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearShape"; ValueType: string; ValueName:"URL Protocol";ValueData: "{app}\bin\{#MyAppExeNameA} %l";Flags: CreateValueIfDoesntExist
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearShape\DefaultIcon"; ValueType: string; ValueName:;ValueData: "%SystemRoot%\system32\url.dll,0";Flags: CreateValueIfDoesntExist
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearShape\Shell"; ValueName: ; Flags: CreateValueIfDoesntExist; ValueType: string;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearShape\Shell\open"; ValueName: ; Flags: CreateValueIfDoesntExist; ValueType: string;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearShape\Shell\open\command"; ValueType: string; ValueName:;ValueData: "{app}\bin\{#MyAppExeNameA} %l";Flags: CreateValueIfDoesntExist

Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearDesign"; ValueType: string; ValueName:;ValueData: "WebClearDesign";Flags: CreateValueIfDoesntExist UninsDeleteKey;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearDesign"; ValueType: string; ValueName:"URL Protocol";ValueData: "{app}\bin\{#MyAppExeNameB} %l";Flags: CreateValueIfDoesntExist
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearDesign\DefaultIcon"; ValueType: string; ValueName:;ValueData: "%SystemRoot%\system32\url.dll,0";Flags: CreateValueIfDoesntExist
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearDesign\Shell"; ValueName: ; Flags: CreateValueIfDoesntExist; ValueType: string;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearDesign\Shell\open"; ValueName: ; Flags: CreateValueIfDoesntExist; ValueType: string;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearDesign\Shell\open\command"; ValueType: string; ValueName:;ValueData: "{app}\bin\{#MyAppExeNameB} %l";Flags: CreateValueIfDoesntExist

Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearWork"; ValueType: string; ValueName:;ValueData: "WebClearWork";Flags: CreateValueIfDoesntExist UninsDeleteKey;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearWork"; ValueType: string; ValueName:"URL Protocol";ValueData: "{app}\bin\{#MyAppExeNameC} %l";Flags: CreateValueIfDoesntExist
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearWork\DefaultIcon"; ValueType: string; ValueName:;ValueData: "%SystemRoot%\system32\url.dll,0";Flags: CreateValueIfDoesntExist
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearWork\Shell"; ValueName: ; Flags: CreateValueIfDoesntExist; ValueType: string;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearWork\Shell\open"; ValueName: ; Flags: CreateValueIfDoesntExist; ValueType: string;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearWork\Shell\open\command"; ValueType: string; ValueName:;ValueData: "{app}\bin\{#MyAppExeNameC} %l";Flags: CreateValueIfDoesntExist

Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearCheck"; ValueType: string; ValueName:;ValueData: "WebClearCheck";Flags: CreateValueIfDoesntExist UninsDeleteKey;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearCheck"; ValueType: string; ValueName:"URL Protocol";ValueData: "{app}\bin\{#MyAppExeNameD} %l";Flags: CreateValueIfDoesntExist
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearCheck\DefaultIcon"; ValueType: string; ValueName:;ValueData: "%SystemRoot%\system32\url.dll,0";Flags: CreateValueIfDoesntExist
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearCheck\Shell"; ValueName: ; Flags: CreateValueIfDoesntExist; ValueType: string;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearCheck\Shell\open"; ValueName: ; Flags: CreateValueIfDoesntExist; ValueType: string;
Root: "HKLM"; SubKey: "SOFTWARE\Classes\WebClearCheck\Shell\open\command"; ValueType: string; ValueName:;ValueData: "{app}\bin\{#MyAppExeNameD} %l";Flags: CreateValueIfDoesntExist

//更新版本时需要更新注册表的值，默认是用ClearCheck打开
Root: "HKLM"; SubKey: "SOFTWARE\Classes\{#MyAppName}\Versions\{#MyAppVersion}"; ValueName: ; Flags: CreateValueIfDoesntExist; ValueType: string;
Root: "HKCR"; Subkey: "*.CBM"; ValueType: String; ValueData: "CBM文件"; Flags: uninsdeletekey; Tasks: fileassoc
Root: "HKCR"; Subkey: "CBM文件"; ValueType: String; ValueData: "CBM文件"; Flags: uninsdeletekey; Tasks: fileassoc
Root: "HKCR"; Subkey: "CBM文件\DefaultIcon"; ValueType: String; ValueData: "{app}\file.ico"; Flags: uninsdeletekey; Tasks: fileassoc
Root: "HKCR"; Subkey: "CBM文件\shell\open\command"; ValueType: String; ValueData: """{app}\bin\{#MyAppExeNameD}"" ""%1"""; Flags: uninsdeletekey; Tasks: fileassoc
Root: "HKCR"; Subkey: "CBM文件\shell\OpenWithClearCheck"; ValueType: String; ValueData: "使用&ClearCheck 打开"; Flags: uninsdeletekey; Tasks: fileassoc
Root: "HKCR"; Subkey: "CBM文件\shell\OpenWithClearCheck\command"; ValueType: String; ValueData: """{app}\bin\ClearCheck.exe"" ""%1"""; Flags: uninsdeletekey; Tasks: fileassoc
;Root: "HKCR"; Subkey: "cmediafile//Shell//Open//Command"; ValueType: string; ValueName: ""; ValueData: "{app}/CMediaManager.exe %1"


Root: "HKCU"; Subkey: "SoftWare\Classes\CBM_auto_file\shell\open\command"; ValueType: string; ValueData: """{app}\bin\ClearCheck.exe"" ""%1"""; Flags: createvalueifdoesntexist uninsdeletekey; Tasks: fileassoc
Root: "HKCR"; Subkey: "Applications\{#MyAppName}\shell\open\command"; ValueType: string; ValueData: """{app}\bin\ClearCheck.exe"" ""%1"""; Flags: createvalueifdoesntexist uninsdeletekey; Tasks: fileassoc
Root: "HKCU"; Subkey: "Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.CBM\OpenWithList"; ValueType: string; ValueName: "MRUList"; ValueData: "a"; Flags: createvalueifdoesntexist uninsdeletekey; Tasks: fileassoc
Root: "HKCU"; Subkey: "Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.CBM\OpenWithList"; ValueType: string; ValueName: "a"; ValueData: "ClearCheck.exe"; Flags: createvalueifdoesntexist uninsdeletekey; Tasks: fileassoc
Root: "HKCU"; Subkey: "Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.CBM\OpenWithProgids"; ValueType: none; ValueName: "CBM_auto_file"; ValueData: "0"; Flags: createvalueifdoesntexist uninsdeletekey; Tasks: fileassoc


[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\bin\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{userdesktop}\可丽尔博士医生登录"; Filename: "http://doctor.clearbos.com/index.html"; IconFilename: "{app}\bin\publish\icons\{#MyOnlineICO}"
;Name: "{userdesktop}\离线登录";Filename: "{app}\bin\CBOfflineBrowser.exe"; IconFilename: "{app}\bin\publish\icons\{#MyOfflineICO}"
Name: "{userdesktop}\可丽尔博士病例查看器"; Filename: "{app}\bin\ClearSample.exe"; IconFilename: "{app}\bin\publish\icons\ClearCheck.ico"


[UninstallDelete]
Type: filesandordirs; Name: "{app}"
Type: filesandordirs; Name: "{userappdata}\ClearBos"

[Run]
Filename: "{tmp}\vc_redist.x86.2008.exe"; Parameters: /q; WorkingDir: {tmp}; Flags: skipifdoesntexist; StatusMsg: "安装 Microsoft Visual C++ 2008 Runtime ...";
Filename: "{tmp}\vc_redist.x86.exe"; Parameters: /q; WorkingDir: {tmp}; Flags: skipifdoesntexist; StatusMsg: "安装 Microsoft Visual C++ 2015 Runtime ...";


[Components]
;Name: "ClearCheck"; Description: "ClearCheck"; Types:Custom; Flags: fixed


[Code]
//卸载以前的版本
function InitializeSetup(): boolean;
var
  ResultStr: String;
  ResultCode: Integer;
begin
  if RegQueryStringValue(HKLM, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{AAD39D90-7727-48BD-9F41-8F8421917CC1}_is1', 'UninstallString', ResultStr) then
    begin
      ResultStr := RemoveQuotes(ResultStr);
      Exec(ResultStr, '/silent', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    end;
    result := true;
end;

//关键代码静默安装
procedure InitializeWizard();
begin
  //不显示边框，这样就能达到不会闪两下了
  WizardForm.BorderStyle:=bsNone;
end; 
procedure CurPageChanged(CurPageID: Integer);
begin
 //因为安装过程界面隐藏不了，所以设置窗口宽高为0
  WizardForm.ClientWidth := ScaleX(0)
  WizardForm.ClientHeight := ScaleY(0)
if CurPageID = wpWelcome then
WizardForm.NextButton.OnClick(WizardForm);
if CurPageID >= wpInstalling then
    WizardForm.Visible := False
  else
    WizardForm.Visible := True;
 // WizardForm.NextButton.OnClick(WizardForm);
end;
 
function ShouldSkipPage(PageID: Integer): Boolean;
begin
result := true;
end;
