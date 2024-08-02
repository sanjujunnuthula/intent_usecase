from dataclasses import dataclass


@dataclass
class EvaluationModel():
    input_url: str
    output_url: str
    predictions: list

    def __init__(self):
        self.input_url = ''
        self.output_url = ''
