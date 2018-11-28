## install dependency

#### python3
install or update to python 3

最好是直接装anaconda：python3.6

#### install rasa_core, this will install rasa nlu too, and now support chinese.
```
pip install rasa_nlu
pip install pyhanlp
hanlp
```

#### install sklearn and MITIE

```
pip install -U scikit-learn==0.19.1 sklearn-crfsuite
pip install git+https://github.com/mit-nlp/MITIE.git

scikit-learn不要安装0.20以上的版本
