# www

## Django Blog System


> nginx
```
sudo service nginx start / stop / status / restart;
```
>uwsgi重启
```
lsof -i:8000
# 查询到uwsgi的端口号
kill -9 端口号
uwsgi --ini uwsgi.ini
```
