# rasa-nlu-example

[rasa-nlu官方文档](https://rasa.com/docs/nlu/)

### install dependency:
- [follow here](https://github.com/algteam/rasabot/tree/master/rasa-nlu-example/INSTALL.md)

### dir tree
```
rasa-nlu-example/
├── data
│   ├── mobile_nlu_data.json  # rasa nlu train data
│   ├── mobile_raw_data.txt   # raw data
│   └── total_word_feature_extractor.dat  # mitie word vector feature
├── requirements.txt
├── train_nlu.py              # train nlu model
├── trainsfer_raw_to_rasa.py.py               # 把raw data变成rasa nlu train data
├── start-server.sh           # run nlu and core server
├── sample_configs            # nlu-configs
├── models                    # directory to save trained models
└── README.md                 # readme file

```

### 配置hanlp分词

[pyhanlp](https://github.com/hankcs/pyhanlp)

在sample_configs目录，用registry.py替换掉site-packages/rasa_nlu的registry.py，hanlp_tokenizer.py放到anaconda安装目录的site-packages/rasa_nlu/tokenizers目录下

### train nlu model
```bash
python -m rasa_nlu.train --config  mobile_nlu_model_config.json --data data/mobile_nlu_data.json  --path models
```
or 

python train_nlu.py

## start nlu -server
sh start-server.sh

### test rasa nlu
```
$python -m rasa_nlu.server --path models
$ curl -X POST localhost:5000/parse -d '{"q":"hello", "project": "nlu", "model": "current"}' | python -m json.tool
{
    "intent": {
        "name": "greet",
        "confidence": 1.0
    },
    "entities": [],
    "text": "hello",
    "project": "default",
    "model": "fallback"
}

```

### train word vector

You can train your own MITIE model using following method:
```
$ git clone https://github.com/mit-nlp/MITIE.git
$ cd MITIE/tools/wordrep
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build . --config Release
$ ./wordrep -e /path/to/your/folder_of_cutted_text_files
```
/path/to/your/folder_of_cutted_text_files是训练语料所在目录，训练大概需要2天(10G语料)

Reference

1 [zqhZY/_rasa_chatbot](https://github.com/zqhZY/_rasa_chatbot)

2 [crownpku/Rasa_NLU_Chi](https://github.com/crownpku/Rasa_NLU_Chi)
