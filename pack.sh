#!/bin/bash
read -p "Please input your instruction: " instruction
<<<<<<< HEAD
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
=======
if [ "${instruction}" = "exe" ]; then
    echo "pack exe"
    pyinstaller -F ./qt_crawler.py
elif [ "${instruction}" = "ui" ]; then
    echo "pack ui"
    pyuic5 Questionnaire.ui > qui.py
elif [ "${instruction}" = "win" ]; then
    echo "pack exe for windows, plz confirm that docker is running and your're in the folder named 'src'! "
    docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
else
    echo "plz input correct instruction like: pack, ui, win"
fi
>>>>>>> c9b025a4d0bae563ab59ee48c3a104e4c4aefba4
