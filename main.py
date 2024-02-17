from presets import Preset
import regex as re


class Modifier:
    posRules = {
        6: lambda x: rf"(?<= ){x}(?= )",
        7: lambda x: rf"(?<=\w){x}(?=\w)",
        8: lambda x: rf"(?<=\w){x}(?= )",
        9: lambda x: rf"(?<= ){x}(?=\w)",
        10: lambda x: rf"^{x}",
        11: lambda x: rf"{x}$",
    }

    def __init__(self, path: str):
        self.preset = Preset()
        with open(path, "r", encoding="utf-8") as f:
            self.content = [l.replace("\n", "") for l in f.readlines()]

    def setLangPreset(self, langPreset: Preset):
        self.preset = langPreset

    def __applyRuleToSingleLine(self, strSingleLine: str) -> str:
        for ruleName, ruleContent in self.preset.rules.items():
            for matchedSign in ruleContent.get("match"):
                _sign = matchedSign.get("sign")
                _pos = matchedSign.get("pos")
                
