# -*- coding:utf-8 -*-

__author__ = 'lyy'
__date__ = '19-1-4 下午4:37'

# #train
from rasa_nlu_gao.training_data import load_data
from rasa_nlu_gao.model import Trainer
from rasa_nlu_gao import config


def Train_nlu(nlu_file, config_file):
    training_data = load_data(nlu_file)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist("models/", project_name="nlu_gao",
                                      fixed_model_name="current")  # Returns the directory the model is stored in
    return model_directory

if __name__ == "__main__":
    nlu_file = 'data/rasa_dataset_training.json'
    config_file = "sample_configs/config_embedding_bilstm.yml"
    model_directory = Train_nlu(nlu_file, config_file)
