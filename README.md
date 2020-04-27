# TestLogService

- Testing a Windows Service that calls a Python executable that logs to a file
- Tutorial I followed: https://docs.microsoft.com/en-us/dotnet/framework/windows-services/walkthrough-creating-a-windows-service-application-in-the-component-designer>

## Installation

### Software
1. install Visual Studio 2019 (or later) IDE
   1. include ASP.NET and web development
2. install latest version of Python 3 <https://www.python.org/downloads/windows/>
   1. Add Python to path/environment variable: `C:\Users\ADunsmoor\AppData\Local\Programs\Python\Python38`
      1. Also add Scripts: `C:\Users\ADunsmoor\AppData\Local\Programs\Python\Python38\Scripts`
   2. use Command Prompt **not as an administrator**
   3. `python --version` should return a version
3. `python -m pip install pyinstaller`

### Install Windows Service

- run `Developer PowerShell for VS 2019` as administrator
- `cd C:\Users\adamd\Documents\GitHub\TestLogService\TestLogService\bin\Debug`
- `installutil TestLogService.exe`

## How to create Python Executable on Windows

- Note: Uses pyinstaller <https://www.pyinstaller.org/>

1. open a Command Prompt
   1. `cd C:\Users\adamd\Documents\GitHub\TestLogService\PythonFiles`
   2. `pyinstaller --onefile test.py`
      1. if having issues with path, use direct link to `pyinstaller.exe`
         1. `C:\Users\adamd\AppData\Local\Programs\Python\Python38-32\Scripts\pyinstaller.exe --onefile ToCloud.py`
   3. this will create a `.spec` file used for compilation
