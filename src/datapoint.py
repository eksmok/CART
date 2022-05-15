from typing import Dict, List


class DataPoint:
    def __init__(self, data: Dict[str, float]):
        """
        :param data: represent the data of the tree, "feature : float"
        """
        self.data = data

    @staticmethod
    def computation_gini(cls, observation: List['DataPoint'], feature: str) -> float:
        gini: float
        n_observation = len(observation)
        list_feature = cls._get_feature(feature=feature, data=observation)

        pass

    @staticmethod
    def _get_feature(feature: str, data: List['DataPoint']) -> List[float]:
        list_feature: List[float] = []
        for datapoint in data:
            list_feature.append(datapoint.data[feature])
        return list_feature
