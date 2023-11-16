```python
说明
bash -c "$(curl https://raw.githubusercontent.com/sss128/emby-version-keeper/main/run.sh)" -s emby_config_dir mode media_to_merge
三个参数，emby_config_dir: 你的emby config目录，xiaoya全家桶位于执行全家桶时输入的-s 媒体库目录/config
        mode: 1 合并，2 拆分
        media_to_merge: emby中想要合并的媒体库，比如在全家桶的 `/media/每日更新/电影`

示例1 合并 /media/电影/每日更新
bash -c "$(curl https://raw.githubusercontent.com/sss128/emby-version-keeper/main/run.sh)" -s `/emby_config_dir` `1` `/media/电影/每日更新`

示例2 拆分已合并 /media/电影/每日更新
bash -c "$(curl https://raw.githubusercontent.com/sss128/emby-version-keeper/main/run.sh)" -s `/emby_config_dir` `2` `/media/电影/每日更新`

<img width="633" alt="image" src="https://github.com/sss128/emby-version-keeper/assets/149408730/6674d673-244f-4668-abaa-873bc42840c4">
