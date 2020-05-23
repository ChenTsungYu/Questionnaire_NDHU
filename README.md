Install virtual environment
```
virtualenv env
```
Run virtual environment
```
source env/bin/activate
```
Install dependency
```
pip3 install -r requirements.txt
```
Pack `.py` as `.exe`
```
pyinstaller -F ./crawler.py
# or run in shell script
./pack.sh
```
Write dependency into`requirements.txt`(Optional)
```
pip3 freeze > requirements.txt
```