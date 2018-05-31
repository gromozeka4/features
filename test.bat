@echo off
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ("%TIME%") do (set mytime=%%a%%b)
echo %mydate%_%mytime%
python -m behave c:\behave\features\Read_Socket.feature > c:\reports\behave_report%mydate%_%mytime%.txt
python -m behave c:\behave\features\Read_Socket.feature
xcopy /s c:\reports\* \\10.100.5.87\temp\reports