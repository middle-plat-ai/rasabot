# -*- coding:utf-8 -*-


# #train
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config


def Train_nlu(nlu_file, config_file):
    training_data = load_data(nlu_file)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist("models/", project_name="nlu",
                                      fixed_model_name="current")  # Returns the directory the model is stored in
    return model_directory

if __name__ == "__main__":
    nlu_file = 'data/mobile_nlu_data.json'
    config_file = "sample_configs/config_hanlp_mitie_sklearn.yml"
    model_directory = Train_nlu(nlu_file, config_file)
