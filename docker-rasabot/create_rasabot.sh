#!/bin/bash

#查看docker版本
echo "$1" | sudo -S docker -v && docker-compose -v

#Creating a Chatbot Using Rasa Core：https://rasa.com/docs/core/0.12.3/docker_walkthrough/#id6
#添加用户自定义actions
touch __init__.py


#训练core-model
echo "$1" | sudo -S docker run \
  -v $(pwd):/app/project \
  -v $(pwd)/models/rasa_core:/app/models \
  rasa/rasa_core:latest \
  train \
    --domain project/mobile_domain.yml \
    --stories project/data/mobile_story.md \
    --out models

##test
echo "$1" | sudo -S docker run \
  -it \
  -v $(pwd)/models/rasa_core:/app/models \
  rasa/rasa_core:latest \
  start \
    --core models


##训练nlu-model
echo "$1" | sudo -S docker run \
  -v $(pwd):/app/project \
  -v $(pwd)/models/rasa_nlu:/app/models \
  -v $(pwd)/config:/app/config \
  rasa/rasa_nlu:latest-full \
  run \
    python -m rasa_nlu.train \
    -c config/config_jieba_mitie_sklearn.yml \
    -d project/data/mobile_nlu_data.json \
    -o models \
    --project current


##联系core和nlu
cat >> config/endpoints.yml <<EOF
nlu:
  url: http://rasa_nlu:5000
action_endpoint:
  url: http://action_server:5055/webhook
EOF


cat >> docker-compose.yml <<EOF
version: '3.0'

services:
  rasa_core:
    image: rasa/rasa_core:latest
    ports:
      - 5005:5005
    volumes:
      - ./models/rasa_core:/app/models
      - ./config:/app/config
    command:
      - start
      - --core
      - models
      - -c
      - rest
      - --endpoints
      - config/endpoints.yml
      - -u
      - current/nlu
  action_server:
    image: rasa/rasa_core_sdk:latest
    volumes:
      - ./actions:/app/actions
  rasa_nlu:
    image: rasa/rasa_nlu:latest-full
    volumes:
      - ./models/rasa_nlu:/app/models
      - ./config:/app/config
    command:
      - start
      - --path
      - models
      - -c
      - config/config_jieba_mitie_sklearn.yml
EOF


##启动nlu和core的服务
#echo "$1" | sudo -S sudo docker-compose up
