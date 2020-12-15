Install virtual environment
```
virtualenv env
```
Run virtual environment
```
source env/bin/activate
```
Install packages
```
pip3 install -r requirements.txt
```
Pack `.py` as `.exe`
```
pyinstaller -F ./crawler.py
# or run in shell script
./pack.sh
```
Save packages in `requirements.txt`(Optional)
```
pip3 freeze > requirements.txt
```

# Reference
* [Python 程式打包為執行檔.exe ( Mac OS )](https://medium.com/%E6%88%91%E5%B0%B1%E5%95%8F%E4%B8%80%E5%8F%A5-%E6%80%8E%E9%BA%BC%E5%AF%AB/python-%E5%B0%87%E7%A8%8B%E5%BC%8F%E6%89%93%E5%8C%85%E7%82%BA%E5%9F%B7%E8%A1%8C%E6%AA%94-exe-mac-os-e9521bc87e24)
* [Repository: docker-pyinstaller](https://github.com/cdrx/docker-pyinstaller)
