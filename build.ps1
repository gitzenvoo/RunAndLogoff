#Requires -RunAsAdministrator
Remove-Item ./build -Recurse -Force
Remove-Item ./dist -Recurse -Force
remove-item ./RunAndLogoff.spec -force
pip install pyinstaller
pyinstaller.exe  --noconsole --onefile .\RunAndLogoff.py



