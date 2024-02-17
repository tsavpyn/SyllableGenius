import json


class Preset:
    def __init__(self, rules=None):
        if rules is None:
            rules = {}
        self.rules = rules

    def importFromJSON(self, strJSON: str):
        self.rules = json.loads(strJSON)

    def importFromFile(self, filePath: str):
        with open(filePath, "r", encoding="utf-8") as f:
            self.importFromJSON(f.read())

    @property
    def listOfRules(self):
        return self.rules.keys()


defaultPresetEn = """{
  "space": {
    "match": [
      {
        "sign": " ",
        "pos": 7
      }
    ],
    "process": 1
  },
  "space_illegal": {
    "match": [
      {
        "sign": " ",
        "pos": 10
      },
      {
        "sign": " ",
        "pos": 11
      }
    ],
    "process": 4
  },
  "break": {
    "match": [
      {
        "sign": "\u2014",
        "pos": 6
      },
      {
        "sign": "-",
        "pos": 6
      },
      {
        "sign": "\u2014",
        "pos": 11
      },
      {
        "sign": "-",
        "pos": 11
      }
    ],
    "process": 1
  },
  "dash": {
    "match": [
      {
        "sign": "-",
        "pos": 7
      }
    ],
    "process": 1
  },
  "comma, period, exclam, ques, colon": {
    "match": [
      {
        "sign": ",",
        "pos": 8
      },
      {
        "sign": ".",
        "pos": 8
      },
      {
        "sign": "!",
        "pos": 8
      },
      {
        "sign": "?",
        "pos": 8
      },
      {
        "sign": ":",
        "pos": 8
      },
      {
        "sign": ",",
        "pos": 11
      },
      {
        "sign": ".",
        "pos": 11
      },
      {
        "sign": "!",
        "pos": 11
      },
      {
        "sign": "?",
        "pos": 11
      },
      {
        "sign": ":",
        "pos": 11
      }
    ],
    "process": 1
  },
  "quote_front": {
    "match": [
      {
        "sign": "\"",
        "pos": 9
      },
      {
        "sign": "\"",
        "pos": 10
      }
    ],
    "process": 2
  },
  "quote_end": {
    "match": [
      {
        "sign": "\"",
        "pos": 8
      },
      {
        "sign": "\"",
        "pos": 9
      },
      {
        "sign": "\"",
        "pos": 11
      }
    ],
    "process": 1
  }
}"""
defaultPresetHans = """{
  "split_every_word": {
    "match": [
      {
        "sign": "",
        "pos": 12
      }
    ],
    "process": 3
  },
  "space": {
    "match": [
      {
        "sign": " ",
        "pos": 7
      }
    ],
    "process": 1
  },
  "space_illegal": {
    "match": [
      {
        "sign": " ",
        "pos": 10
      },
      {
        "sign": " ",
        "pos": 11
      }
    ],
    "process": 4
  },
  "break": {
    "match": [
      {
        "sign": "\u2014",
        "pos": 6
      },
      {
        "sign": "\u2014\u2014",
        "pos": 6
      },
      {
        "sign": "\u2014",
        "pos": 11
      },
      {
        "sign": "\u2014\u2014",
        "pos": 11
      }
    ],
    "process": 1
  },
  "comma, period, exclam, ques, colon": {
    "match": [
      {
        "sign": "\uff0c",
        "pos": 8
      },
      {
        "sign": "\u3002",
        "pos": 8
      },
      {
        "sign": "\uff01",
        "pos": 8
      },
      {
        "sign": "\uff1f",
        "pos": 8
      },
      {
        "sign": "\uff1a",
        "pos": 8
      },
      {
        "sign": "\uff0c",
        "pos": 11
      },
      {
        "sign": "\u3002",
        "pos": 11
      },
      {
        "sign": "\uff01",
        "pos": 11
      },
      {
        "sign": "\uff1f",
        "pos": 11
      },
      {
        "sign": "\uff1a",
        "pos": 11
      }
    ],
    "process": 1
  },
  "quote_front": {
    "match": [
      {
        "sign": "\"",
        "pos": 9
      },
      {
        "sign": "\"",
        "pos": 10
      }
    ],
    "process": 2
  },
  "quote_end": {
    "match": [
      {
        "sign": "\"",
        "pos": 8
      },
      {
        "sign": "\"",
        "pos": 9
      },
      {
        "sign": "\"",
        "pos": 11
      }
    ],
    "process": 1
  },
  "chn_quote_front": {
    "match": [
      {
        "sign": "\u201c",
        "pos": 9
      },
      {
        "sign": "\u201c",
        "pos": 10
      }
    ],
    "process": 20,
    "sub": "\""
  },
  "chn_quote_end": {
    "match": [
      {
        "sign": "\u201d",
        "pos": 8
      },
      {
        "sign": "\u201d",
        "pos": 9
      },
      {
        "sign": "\u201d",
        "pos": 11
      }
    ],
    "process": 20,
    "sub": "\""
  }
}"""
defaultPresetRu = """{
  "space": {
    "match": [
      {
        "sign": " ",
        "pos": 7
      }
    ],
    "process": 1
  },
  "space_illegal": {
    "match": [
      {
        "sign": " ",
        "pos": 10
      },
      {
        "sign": " ",
        "pos": 11
      }
    ],
    "process": 4
  },
  "break": {
    "match": [
      {
        "sign": "\u2014",
        "pos": 6
      },
      {
        "sign": "-",
        "pos": 6
      },
      {
        "sign": "\u2014",
        "pos": 11
      },
      {
        "sign": "-",
        "pos": 11
      }
    ],
    "process": 2
  },
  "dash": {
    "match": [
      {
        "sign": "-",
        "pos": 7
      }
    ],
    "process": 1
  },
  "comma_period_exclam_ques_colon": {
    "match": [
      {
        "sign": ",",
        "pos": 8
      },
      {
        "sign": ".",
        "pos": 8
      },
      {
        "sign": "!",
        "pos": 8
      },
      {
        "sign": "?",
        "pos": 8
      },
      {
        "sign": ":",
        "pos": 8
      },
      {
        "sign": ",",
        "pos": 11
      },
      {
        "sign": ".",
        "pos": 11
      },
      {
        "sign": "!",
        "pos": 11
      },
      {
        "sign": "?",
        "pos": 11
      },
      {
        "sign": ":",
        "pos": 11
      }
    ],
    "process": 1
  },
  "quote_front": {
    "match": [
      {
        "sign": "\"",
        "pos": 9
      },
      {
        "sign": "\"",
        "pos": 10
      }
    ],
    "process": 2
  },
  "quote_end": {
    "match": [
      {
        "sign": "\"",
        "pos": 8
      },
      {
        "sign": "\"",
        "pos": 9
      },
      {
        "sign": "\"",
        "pos": 11
      }
    ],
    "process": 1
  },
  "rus_quote_front": {
    "match": [
      {
        "sign": "\u00ab",
        "pos": 9
      },
      {
        "sign": "\u00ab",
        "pos": 10
      }
    ],
    "process": 20,
    "sub": "\""
  },
  "rus_quote_end": {
    "match": [
      {
        "sign": "\u00bb",
        "pos": 8
      },
      {
        "sign": "\u00bb",
        "pos": 9
      },
      {
        "sign": "\u00bb",
        "pos": 11
      }
    ],
    "process": 20,
    "sub": "\""
  }
}"""
