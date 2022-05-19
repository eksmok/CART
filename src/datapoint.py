from typing import Dict, List


class DataPoint:
    def __init__(self, classes: Dict[str, List[str]], features: Dict[str, float]):
        """

        :param classes: list of sub feature of a feature
        :param features: the values of the different subfeatures
        """
        self.classes = classes
        self.features = features

    @staticmethod
    def computation_gini(cls, observation: 'DataPoint', feature: str) -> float:
        """
        Compute the gini indice of a feature based on the data

        :param cls:
        :param observation: The data used for the CART
        :param feature: The computation of the specific feature
        :return: gini for a chosen feature
        """
        # TODO : Je dois réflechir au concept de classe et de feature, et selon ma déf, je calcule le gini d'UNE
        # TODO : D'UNE FEATURE ICI. Donc cela à revient à calculer gini de chacun des classes et de pondérer ces gini par leurs nb d'observation
        gini_of_feature: float
        list_feature_value = cls._get_feature(feature=feature,)
        nb_total_of_the_feature = len(list_feature_value)
        for classe in observation.classes:
            pass
        pass

    @staticmethod
    def _get_feature(feature: str, data: 'DataPoint') -> List[float]:
        list_feature_value: List[float] = data.classes[feature]
        return list_feature_value
# Structure of the data :
#   Dict { feature 1 : [ value1, value2, ...], feature 2 : [value1, value2, ...]
