echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" AIAA-UTD-Computer 56580 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 46728) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 48788) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 43304) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 41604) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 46404) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 39348)
del "C:\Users\AIAA UT Dallas\Documents\Comet Rocketry Sims\CometRocketryRocketpySims\cleanup-fluent-AIAA-UTD-Computer-46404.bat"
