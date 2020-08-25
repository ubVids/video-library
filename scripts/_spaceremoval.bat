@echo off
Setlocal enabledelayedexpansion

Set "Pattern= "
Set "Replace=_"

For %%a in (*) Do (
    Set "File=%%~a"
    Ren "%%a" "!File:%Pattern%=%Replace%!"
)

for /f "Tokens=*" %f in ('dir /l/b/a-d') do (rename "%f" "%f")

Pause&Exit