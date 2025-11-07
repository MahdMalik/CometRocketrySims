echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" AIAA-UTD-Computer 51015 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 45156) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 47692) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 41240) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 48476) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 37692) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 19524)
del "C:\Users\AIAA UT Dallas\Documents\Comet Rocketry Sims\CometRocketryRocketpySims\cleanup-fluent-AIAA-UTD-Computer-37692.bat"
