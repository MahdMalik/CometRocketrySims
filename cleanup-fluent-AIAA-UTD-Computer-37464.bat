echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" AIAA-UTD-Computer 65189 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40016) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 31304) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 33232) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 42524) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 42724) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 45980) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 42176) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 44052) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 40888) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 38816) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 38136) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 34496) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 3560) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 49924) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 32208) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 22324) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 38548) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 29204) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 50036) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 38400) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 48180) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 48704) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 47136) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 26652) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 42364) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 27328) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 12876) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 47208) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 47256) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 19052) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 37464) 
if /i "%LOCALHOST%"=="AIAA-UTD-Computer" (%KILL_CMD% 37972)
del "C:\Users\AIAA UT Dallas\Documents\Comet Rocketry Sims\CometRocketryRocketpySims\cleanup-fluent-AIAA-UTD-Computer-37464.bat"
