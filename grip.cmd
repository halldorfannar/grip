@echo off
:: Pass in -h or --help for command line options
:: Usage: grip <input MD file> --export {|output HTML file}
%PM_PYTHON% %~dp0\main.py %*
