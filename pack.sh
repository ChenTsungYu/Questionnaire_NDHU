#!/bin/bash
read -p "Please input your instruction: " instruction
if [ "${instruction}" = "exe" ]; then
    echo "pack exe"
    pyinstaller -F ./qt_crawler.py
elif [ "${instruction}" = "ui" ]; then
    echo "pack ui"
    pyuic5 Questionnaire.ui > qui.py
elif [ "${instruction}" = "win" ]; then
    echo "pack exe for windows, plz comfirm that docker is running and in the folder named 'src'! "
    docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
else
    echo "plz imput correct instruction like: pack, ui, win"
fi