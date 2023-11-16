<h4>说明</h4>

合并仅限于单个媒体库的重复项，不能跨库合并

```python
bash -c "$(curl https://raw.githubusercontent.com/sss128/emby-version-keeper/main/run.sh)" -s emby_config_dir mode media_to_merge
```
<h5>三个参数</h5>

`emby_config_dir`:  你的emby config目录，xiaoya全家桶位于执行全家桶时输入的-s 媒体库目录/config

`mode`:  1 合并，2 拆分

`media_to_merge`:  emby中想要合并的媒体库，比如在全家桶的 `/media/每日更新/电影`
<img width="642" alt="image" src="https://github.com/sss128/emby-version-keeper/assets/149408730/c463ca42-904a-47b8-97a1-d5d60b5f0c99">



<h5>示例1 合并 /media/电影/每日更新</h5>

bash -c "$(curl https://raw.githubusercontent.com/sss128/emby-version-keeper/main/run.sh)" -s `/emby_config_dir` `1` `/media/电影/每日更新`

<h5>示例2 拆分已合并 /media/电影/每日更新</h5>

bash -c "$(curl https://raw.githubusercontent.com/sss128/emby-version-keeper/main/run.sh)" -s `/emby_config_dir` `2` `/media/电影/每日更新`

<h5>示例3 合并全部媒体库</h5>

bash -c "$(curl https://raw.githubusercontent.com/sss128/emby-version-keeper/main/run.sh)" -s `/emby_config_dir`

<h5>示例4 对多个媒体库分别合并</h5>

bash -c "$(curl https://raw.githubusercontent.com/sss128/emby-version-keeper/main/run.sh)" -s `/emby_config_dir` `1` `/media/电影/每日更新` `/media/电影/4k`
