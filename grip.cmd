@echo off
:: Pass in -h or --help for command line options
:: Usage: grip <input MD file> --export {|output HTML file}
%PM_PACKAGES_ROOT%\python\2.7.6-windows-x86\python.exe %~dp0\main.py %*
