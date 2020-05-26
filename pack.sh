#!/bin/bash
read -p "Please input your instruction: " instruction
case $instruction in
    "exe") 
        echo "pack exe"
        pyinstaller -F ./qt_crawler.py;;
     "ui") 
        echo "pack ui"
        pyuic5 Questionnaire.ui > qui.py;;
     "win") 
        echo "pack exe for windows, plz confirm that docker is running and your're in the folder named 'src'! "
        docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows;;
    *) 
        echo "plz input correct instruction like: pack, ui, win"
        exit 1
esac