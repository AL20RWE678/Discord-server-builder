@REM -- Simple automatic installation script to make your life easier. --
@REM -- Yes, this is my first time writing batch. -- 
@echo off

where /q python
IF ERRORLEVEL 1 (
    echo You didn't install python or added it to your path.
    PAUSE
    exit /b
)
where /q curl
IF ERRORLEVEL 1 (
    echo cURL does not exists. You cannot use this file.
    PAUSE
    exit /b
)
echo Downloading pip . . .
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py

echo Installing . . .
python get-pip.py

echo -----------------------------------

echo Downloading required packages . . .
pip install -r requirements.txt
echo Installed . . .

echo -----------------------------------

echo Clearing unused files . . .
del get-pip.py

echo -----------------------------------

echo Installation completed!
PAUSE
exit /b