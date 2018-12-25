## dir tree

```
.
├── actions
│   ├── actions.py
│   └── __pycache__
│       └── actions.cpython-36.pyc
├── config
│   ├── config_hanlp_mitie_sklearn.yml
│   └── config_jieba_mitie_sklearn.yml
├── create_rasabot.sh
├── data
│   ├── mobile_nlu_data.json
│   ├── mobile_story.md
│   └── total_word_feature_extractor.dat
├── mobile_domain.yml
└── policy.py

```

## 运行
```
  sh create_rasabot.sh +用户密码
```

## 测试结果
```
  curl --request POST \
    --url http://localhost:5005/webhooks/rest/webhook \
    --header 'content-type: application/json' \
    --data '{
      "message": "你好"
    }'
  ```
  
## Reference

1 [Development with Docker](https://rasa.com/docs/core/0.12.3/docker_walkthrough/#)
