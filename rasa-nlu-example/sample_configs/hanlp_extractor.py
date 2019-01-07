from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import warnings

from builtins import str
from typing import Any
from typing import Dict
from typing import Optional
from typing import Text

from rasa_nlu_gao import utils
from rasa_nlu_gao.extractors import EntityExtractor
from rasa_nlu_gao.model import Metadata
from rasa_nlu_gao.training_data import Message
from rasa_nlu_gao.training_data import TrainingData
from rasa_nlu_gao.utils import write_json_to_file
from pyhanlp import *


class HanlpExtractor(EntityExtractor):
    name = "hanlp_extractor"

    provides = ["entities"]

    defaults = {
        "part_of_speech": ['nr'] # nr：人名，ns：地名，nt：机构名
    }

    def __init__(self, component_config=None):
        # type: (Optional[Dict[Text, Text]]) -> None

        super(HanlpExtractor, self).__init__(component_config)

    def train(self, training_data, config, **kwargs):
        # type: (TrainingData) -> None

        self.component_config = config.for_component(self.name, self.defaults)

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None

        extracted = self.add_extractor_name(self.ner_hanlp(message))

        message.set("entities", extracted, add_to_output=True)

    def ner_hanlp(self, example):
        """
        Tokenize a sentence and yields tuples of (word, start, end)
        type: (Text) -> List[Token]
        Parameter:
            - text: the str(unicode) to be segmented.
        """
        segment = HanLP.newSegment().enableNameRecognize(True).enableOrganizationRecognize(True)
        entities = []
        tokenized = segment.seg(example.text)
        start = 0
        for term in tokenized:
            w, pos = str(term).split('/')
            width = len(w)
            part_of_speech = self.component_config["part_of_speech"][0]
            if pos.find(part_of_speech) >= 0:
                entities.append({
                    "entity": part_of_speech,
                    "value": w,
                    "start": start,
                    "end": start + width,
                    "confidence": None,
                })
            else:
                pass
            start += width
        return entities

    @classmethod
    def load(cls,
             model_dir=None,  # type: Optional[Text]
             model_metadata=None,  # type: Optional[Metadata]
             cached_component=None,  # type: Optional[Component]
             **kwargs  # type: **Any
             ):

        meta = model_metadata.for_component(cls.name)

        return cls(meta)
