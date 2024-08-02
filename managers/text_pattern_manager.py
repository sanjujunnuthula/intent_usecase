from extr import RegEx, RegExLabel
import re

class Entity_pattern:
    def __init__(self):
        self.entity_pattern = [
            RegExLabel(
                label='workload',
                regexes=[
                    RegEx([r'\d{1}[A-Za-z]{1}\s[A-Za-z]{4,5}'], re.IGNORECASE)
                ]
            ),
            RegExLabel(
                label='region',
                regexes=[
                    RegEx([r'(["][A-Za-z]{1}["])\s*(?=region)|(?<=region\s)(["][A-Za-z]{1}["]) |(["][Y]{1}["]) |(["][y]{1}["]) |(\sy{1}) |(\sY{1})'], re.IGNORECASE)
                ]
            ),
            RegExLabel(
                label='vendor',
                regexes=[
                    RegEx([r'(?<=vendor\s)(["][A-Za-z]{1}["]) |(["][X]{1}["]) |(["][x]{1}["]) |(\sx{1}) |(\sX{1})'], re.IGNORECASE)
                ]
            ),
            RegExLabel(
                label='version',
                regexes=[
                    RegEx([r'([A-Za-z]{3,10})\s*(?=version)'], re.IGNORECASE)
                ]
            ),]
    def pattern(self):
        entity_pattern=self.entity_pattern
        return entity_pattern
