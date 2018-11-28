#!/bin/bash

#启动nlu服务
nohup python -m rasa_nlu.server -c sample_configs/config_hanlp_mitie_sklearn.yml --path models >> nlu_logs.txt 2>&1 &

#启动core服务
nohup python -m rasa_core.server -d models/dialogue --debug >> dialogue_logs.txt 2>&1 &
