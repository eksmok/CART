from typing import Dict
import numpy as np


class DataPoint:
    def __init__(self, data: Dict[str, np.ndarray], feature_predict_name: str, method: str = 'C'):
        """
        :param: data the data which will be the input to the decision tree
        :param: Refers to the method used 'R' is for regression or 'C' is for classification
        """
        self.feature_to_predict: np.array = data.pop(feature_predict_name, None)
        self.datapoint: Dict[str, np.array] = data
        self.method: str = method

    def _gini_attribute(self, feature: str, attribute: str) -> float:
        """
        Compute the gini index of one attribute of a feature
        :param feature:
        :param attribute:
        :return:
        """
        element_feature: np.array = self.datapoint[feature]
        unique: np.array = np.unique(self.feature_to_predict)
        dict_gini: Dict[str, int] = {}

        for i in range(len(unique)):
            dict_gini[unique[i]] = 0
            for j in range(len(element_feature)):
                if element_feature[j] == attribute and self.feature_to_predict[i] == unique[i]:
                    dict_gini[unique[i]] += 1

        gini: np.array = np.array(list(dict_gini.values()))
        nb_occurence_attribute: int = np.sum(gini)
        gini = gini/nb_occurence_attribute

        return 1 - np.sum(gini**2)

    def gini_feature(self, feature: str) -> float:
        """
        Compute the gini index for a feature given
        :param feature:
        :return: the gini index for the given feature
        """
        element_feature: np.array = self.datapoint[feature]
        gini_index: Dict[str, float] = {}
        unique, counts = np.unique(element_feature, return_counts=True)
        unique_dict = dict(zip(unique, counts))
        length_data = len(self.datapoint)

        for attribute in element_feature:
            gini_index[attribute] = self.gini_attribute(feature, attribute)
        weighted_sum: float = 0.0
        for attribute, gini in gini_index.items():
            weighted_sum += (unique_dict[attribute]/length_data)*gini

        # gini_index['weighted_sum'] = weighted_sum
        return weighted_sum

    def _entropy(self, feature: str) -> float:
        """
        Compute the entropy impurity

        :param: feature chosen for computation
        :return: entropy: float
        """
        unique, counts = np.unique(self.datapoint["feature"], return_counts=True)
        length_feature = self.datapoint[feature].shape[0]
        counts = counts/length_feature
        counts = np.sum(-counts*np.log2(counts))
        return counts


if __name__ == '__main__':
    pass
# Structure of the data :
#   Dict { feature 1 : [ value1, value2, ...], feature 2 : [value1, value2, ...]
# Abstract class metric : gini, entropy hérite,
# Enum pour method
# Changer le format des données prendre des ndarray en supposant que les labels sont connus
# Généralité into details
# Build Tree plein de petite fonctiosn
# Exit : Leaf
# self.dataset_pure
# dataset gauche droite
# graph viz
# draft pull request