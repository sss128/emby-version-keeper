if [ $1 ]; then
	dockers="$(docker ps | grep "xiaoyaliu/alist\|haroldli/xiaoya-tvbox" | grep -v "xiaoyakeeper" | awk '{print $NF}')"
	XIAOYA_NAME="$(echo -e "$dockers" | sed '/^$/d' | head -n1)"
	XIAOYA_ROOT="$(docker inspect --format='{{range $v,$conf := .Mounts}}{{$conf.Source}}:{{$conf.Destination}}{{$conf.Type}}~{{end}}' "$XIAOYA_NAME" | tr '~' '\n' | grep bind | sed 's/bind//g' | grep ":/data" | awk -F: '{print $1}')"
	EMBY_SERVER="$(head -1 "$XIAOYA_ROOT"/emby_server.txt)"
	TOKEN="$(head -1 "$XIAOYA_ROOT"/infuse_api_key.txt)"
	echo $XIAOYA_ROOT
	echo $EMBY_SERVER
	echo $TOKEN
	docker run -it -e EMBY_SERVER=$EMBY_SERVER -e TOKEN=$TOKEN -e EMBY_CONFIG_DIR=$1 -v $1:$1 sss128/emby-version-keeper 1 
fi
