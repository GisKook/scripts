#/bin/bash

KNET_PATH="/home/go/workspace/src/github.com/giskook/test_http/main/"
KNET_NAME="test_http"
KNET_LOG="test_http.log"

pidof $KNET_NAME
pkill -9 $KNET_NAME

`nohup $KNET_PATH$KNET_NAME > $KNET_PATH$KNET_LOG 2>&1 &`
pidof $KNET_NAME
