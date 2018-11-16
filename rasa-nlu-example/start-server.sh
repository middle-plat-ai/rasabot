#!/bin/bash

#启动nlu服务
nohup python -m rasa_nlu.server -c sample_configs/config_hanlp_mitie_sklearn.yml --path models >> logs/nlu_logs.txt 2>&1 &
