# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from policy import MobilePolicy

logger = logging.getLogger(__name__)


def train_dialogue(domain_file="mobile_domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/mobile_story.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), MobilePolicy()])
    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        epochs=200,
        batch_size=16,
        augmentation_factor=50,
        validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.converters import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data("data/mobile_nlu_data.json")
    trainer = Trainer(config.load("mobile_nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist("models/", project_name="nlu",
                                      fixed_model_name="demo")

    return model_directory


def run_ivrbot_online(input_channel=ConsoleInputChannel(),
                      interpreter=RasaNLUInterpreter("models/nlu/demo"),
                      domain_file="mobile_domain.yml",
                      training_data_file="data/mobile_story.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy()],
                  interpreter=interpreter)
    training_data = agent.load_data(training_data_file)
    agent.train_online(training_data,
                       input_channel=input_channel,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent


def run(serve_forever=True):
    agent = Agent.load("models/dialogue",
                       interpreter=RasaNLUInterpreter("models/ivr/demo"))

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == "__main__":
    logging.basicConfig(level="INFO")

    parser = argparse.ArgumentParser(
        description="starts the bot")

    parser.add_argument(
        "task",
        choices=["train-nlu", "train-dialogue", "run", "online_train"],
        help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    elif task == "online_train":
        run_ivrbot_online()
    else:
        warnings.warn("Need to pass either 'train-nlu', 'train-dialogue' or "
                      "'run' to use the script.")
        exit(1)
