# -*- coding: UTF-8 -*-

import re
# import fool
# import tensorflow as tf
#
# gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2)
# sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

def extract_regex(tokens):
    entities = []
    words = []
    for i in range(len(tokens)):
        text = tokens[i]
        if extract_phonenum(text) != []:
            entities.append((range(i, i + 1), 'phone_num', 1.0))
            words.append(text)
        elif extract_card(text) != []:
            entities.append((range(i, i + 1), 'Card_ID', 1.0))
            words.append(text)
        elif extract_telephonenum(text):
            entities.append((range(i, i + 1), 'Telephone_num', 1.0))
            words.append(text)
        else:
            pass
    return entities, words

#识别手机号码
def extract_phonenum(text):
    r = r'^(1[3-9]\d{9})$'
    return re.findall(r, text)

#识别身份证号码
def extract_card(text):
    r = r'^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$'
    return re.findall(r, text)

#识别固定电话
def extract_telephonenum(text):
    r = r'^((0\d{2}-?\d{8})|(0\d{3}-?\d{7}))(-\d{3,5})?$'
    return re.findall(r, text)

#中文命名实体识别:使用foolnltk
# def ner_fool(text):
#     words, ners = fool.analysis([text])
#     entities = []
#     ls = []
#     if ners[0] != []:
#         for i in range(len(ners[0])):
#             start, end, entity, value = ners[0][i]
#             ls.append(value)
#             entities.append({
#                         "entity": entity,
#                         "value": value,
#                         "start": start,
#                         "end": end-1,
#                         "confidence": None,
#                     })
#     else:
#         pass
#     return entities, ' '.join(ls)
