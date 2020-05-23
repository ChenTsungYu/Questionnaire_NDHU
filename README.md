Install virtual enviroment
```
virtualenv env
```
Run virtual enviroment
啟動虛擬環境
```
souce env/bin/activate
```
Install dependency
```
pip3 install -r requirements.txt
```
Pack `.exe`
```
pyinstaller -F ./crawler.py
# 或執行shell script
./pack.sh
```
Wirte dependency into`requirements.txt`(Optional)
```
pip3 freeze > requirements.txt
```

## Note
The version of `chromedriver` needs to be same as Chrome. 
If they're different,plz follow the link below.
[這篇](https://chentsungyu.github.io/2019/09/03/Python/%5BPython%5D%20%E7%88%AC%E8%9F%B2%E7%AD%86%E8%A8%983-%20Selenium/#%E7%89%88%E6%9C%AC%E5%95%8F%E9%A1%8C)