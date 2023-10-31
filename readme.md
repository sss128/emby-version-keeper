```python
示例1 合并 /mnt/xiaoya/每日更新/电影
docker run -it \
 -e EMBY_SERVER=http://192.168.1.10:2345 \
 -e TOKEN=05b739a0c0794e6d87e7df7427s2ac0f \
 -e EMBY_CONFIG_DIR=/app/emby/config \
 -v /app/emby/config:/app/emby/config \
sss128/emby-version-keeper 1 /mnt/xiaoya/每日更新/电影

示例2 拆分已合并 /mnt/xiaoya/每日更新/电影
docker run -it \
 -e EMBY_SERVER=http://192.168.1.10:2345 \
 -e TOKEN=05b739a0c0794e6d87e7df7427s2ac0f \
 -e EMBY_CONFIG_DIR=/app/emby/config \
 -v /app/emby/config:/app/emby/config \
sss128/emby-version-keeper 2 /mnt/xiaoya/每日更新/电影

说明，
docker run -it \
 -e EMBY_SERVER=你的emby地址 \
 -e TOKEN=emby中生成的apikey（infuse那个就可以） \
 -e EMBY_CONFIG_DIR=你的emby config地址 \       
 -v 你的emby_config地址:你的emby_config地址 \    #注意这三个emby_config地址是一样的
sss128/emby-version-keeper 模式(1合并，2拆分) emby中library的目录，见下
```
<img width="633" alt="image" src="https://github.com/sss128/emby-version-keeper/assets/149408730/6674d673-244f-4668-abaa-873bc42840c4">
