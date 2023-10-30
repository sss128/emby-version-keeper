示例
docker run -it \
 -e EMBY_SERVER=http://192.168.1.10:2345 \
 -e TOKEN=05b739a0c0794e6d87e7df7427s2ac0f \
 -e EMBY_CONFIG_DIR=/app/emby/config \
 -v /app/emby/config:/app/emby/config \
sss128/emby-version-keeper 1 /mnt/

说明
docker run -it \
 -e EMBY_SERVER=你的emby地址 \
 -e TOKEN=emby中生成的apikey（infuse那个就可以） \
 -e EMBY_CONFIG_DIR=你的emby config地址 \
 -v 你的emby_config地址:你的emby_config地址 \
sss128/emby-version-keeper 模式(1合并，2拆分) emby中library的目录
