from typing import Dict, List


class DataPoint:
    def __init__(self, data: Dict[str, float]):
        self.data = data

    @staticmethod
    def computation_gini(data: List['DataPoint'], feature: str) -> float:
        pass

    @staticmethod
    def _get_feature(feature: str, data: List['DataPoint']):
        list_feature: List[float] = []
        for datapoint in data:
            list_feature.append(datapoint.data[feature])
        return list_feature
