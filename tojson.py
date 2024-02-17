import json

#
#   0 左中右合并  1 并入左词 2 并入右词   3 单独拆分
#   4 删去    5 删去且合并左右   20 替换为sub
#
#   6 左右空   7 左右字   8 左字右空  9 左空右字
#   10 行首   11行末
#

preset_en = {
    "space": {
        "match": [
            {"sign": " ", "pos": 7}],
        "process": 1,
    },
    "space_illegal": {
        "match": [
            {"sign": " ", "pos": 10},
            {"sign": " ", "pos": 11}],
        "process": 4,
    },
    "break": {
        "match": [
            {"sign": "—", "pos": 6},
            {"sign": "-", "pos": 6},
            {"sign": "—", "pos": 11},
            {"sign": "-", "pos": 11}],
        "process": 1,
    },
    "dash": {
        "match": [
            {"sign": "-", "pos": 7}],
        "process": 1,
    },
    "comma, period, exclam, ques, colon": {
        "match": [
            {"sign": ",", "pos": 8},
            {"sign": "\\.", "pos": 8},
            {"sign": "\\!", "pos": 8},
            {"sign": "\\?", "pos": 8},
            {"sign": ":", "pos": 8},
            {"sign": ",", "pos": 11},
            {"sign": "\\.", "pos": 11},
            {"sign": "\\!", "pos": 11},
            {"sign": "\\?", "pos": 11},
            {"sign": ":", "pos": 11}],
        "process": 1,
    },
    "quote_front": {
        "match": [
            {"sign": "\"", "pos": 9},
            {"sign": "\"", "pos": 10}],
        "process": 2,
    },
    "quote_end": {
        "match": [
            {"sign": "\"", "pos": 8},
            {"sign": "\"", "pos": 9},
            {"sign": "\"", "pos": 11}],
        "process": 1,
    },
}

preset_ru = {
    "space": {
        "match": [
            {"sign": " ", "pos": 7}],
        "process": 1,
    },
    "space_illegal": {
        "match": [
            {"sign": " ", "pos": 10},
            {"sign": " ", "pos": 11}],
        "process": 4,
    },
    "break": {
        "match": [
            {"sign": "—", "pos": 6},
            {"sign": "-", "pos": 6},
            {"sign": "—", "pos": 11},
            {"sign": "-", "pos": 11}],
        "process": 2,
    },
    "dash": {
        "match": [
            {"sign": "-", "pos": 7}],
        "process": 1,
    },
    "comma_period_exclam_ques_colon": {
        "match": [
            {"sign": ",", "pos": 8},
            {"sign": "\\.", "pos": 8},
            {"sign": "\\!", "pos": 8},
            {"sign": "\\?", "pos": 8},
            {"sign": ":", "pos": 8},
            {"sign": ",", "pos": 11},
            {"sign": "\\.", "pos": 11},
            {"sign": "\\!", "pos": 11},
            {"sign": "\\?", "pos": 11},
            {"sign": ":", "pos": 11}],
        "process": 1,
    },
    "quote_front": {
        "match": [
            {"sign": "\"", "pos": 9},
            {"sign": "\"", "pos": 10}],
        "process": 2,
    },
    "quote_end": {
        "match": [
            {"sign": "\"", "pos": 8},
            {"sign": "\"", "pos": 9},
            {"sign": "\"", "pos": 11}],
        "process": 1,
    },
    "rus_quote_front": {
        "match": [
            {"sign": "«", "pos": 9},
            {"sign": "«", "pos": 10},
        ],
        "process": 20,
        "sub": "\"",
    },
    "rus_quote_end": {
        "match": [
            {"sign": "»", "pos": 8},
            {"sign": "»", "pos": 9},
            {"sign": "»", "pos": 11}],
        "process": 20,
        "sub": "\"",
    },
}

preset_hans = {
    "split_every_word": {
        "builtins": 0,
    },
    "space": {
        "match": [
            {"sign": " ", "pos": 7}],
        "process": 1,
    },
    "space_illegal": {
        "match": [
            {"sign": " ", "pos": 10},
            {"sign": " ", "pos": 11}],
        "process": 4,
    },
    "break": {
        "match": [
            {"sign": "—", "pos": 6},
            {"sign": "——", "pos": 6},
            {"sign": "—", "pos": 11},
            {"sign": "——", "pos": 11}],
        "process": 1,
    },
    "comma, period, exclam, ques, colon": {
        "match": [
            {"sign": "，", "pos": 8},
            {"sign": "。", "pos": 8},
            {"sign": "！", "pos": 8},
            {"sign": "？", "pos": 8},
            {"sign": "：", "pos": 8},
            {"sign": "，", "pos": 11},
            {"sign": "。", "pos": 11},
            {"sign": "！", "pos": 11},
            {"sign": "？", "pos": 11},
            {"sign": "：", "pos": 11}],
        "process": 1,
    },
    "quote_front": {
        "match": [
            {"sign": "\"", "pos": 9},
            {"sign": "\"", "pos": 10}],
        "process": 2,
    },
    "quote_end": {
        "match": [
            {"sign": "\"", "pos": 8},
            {"sign": "\"", "pos": 9},
            {"sign": "\"", "pos": 11}],
        "process": 1,
    },
    "chn_quote_front": {
        "match": [
            {"sign": "“", "pos": 9},
            {"sign": "“", "pos": 10},
        ],
        "process": 20,
        "sub": "\"",
    },
    "chn_quote_end": {
        "match": [
            {"sign": "”", "pos": 8},
            {"sign": "”", "pos": 9},
            {"sign": "”", "pos": 11}],
        "process": 20,
        "sub": "\"",
    },
}

y = json.dumps(preset_hans)

with open("preset_hans.json", "w", encoding="utf-8") as f:
    f.write(y)
