Install virtual enviroment
```
virtualenv env
```
Run virtual enviroment
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

## Note
The version of `chromedriver` needs to be same as Chrome. 
If they're different,plz follow the link below:
[Here](https://chentsungyu.github.io/2019/09/03/Python/%5BPython%5D%20%E7%88%AC%E8%9F%B2%E7%AD%86%E8%A8%983-%20Selenium/#%E7%89%88%E6%9C%AC%E5%95%8F%E9%A1%8C)