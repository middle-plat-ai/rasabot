## install dependency

#### python3
install or update to python 3

最好是直接装anaconda：python3.6

#### install rasa_core, this will install rasa nlu too, and now support chinese.
```
pip install rasa_nlu_gao
pip install pyhanlp
hanlp
```

#### install sklearn and MITIE

```
pip install -U scikit-learn==0.19.1 sklearn-crfsuite
pip install git+https://github.com/mit-nlp/MITIE.git

scikit-learn不要安装0.20以上的版本
```

### 使用bert服务
```
pip install bert-serving-server  # server
pip install bert-serving-client  # client, independent of `bert-serving-server`
```

### 下载bert的预训练模型
bert-serving-start -model_dir /tmp/english_L-12_H-768_A-12/ -num_worker=4 
