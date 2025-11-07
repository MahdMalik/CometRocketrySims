echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" AIAA-UTD-Computer 62897 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 39468) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 37624) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 19668) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 10588) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 31560) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 21792) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 3320) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 37560) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 21800) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 37864) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 9788) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 29612) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 27244) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 39752) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 37380) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40220) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40200) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40180) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40160) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40140) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40120) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40100) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40080) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40060) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40044) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40020) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40004) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 39984) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 39956) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 5952) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 41260) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 44472)
del "C:\Users\AIAA UT Dallas\Documents\Comet Rocketry Sims\CometRocketryRocketpySims\cleanup-fluent-AIAA-UTD-Computer-41260.bat"
