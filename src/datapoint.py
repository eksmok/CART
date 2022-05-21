from typing import Dict
import numpy as np


class DataPoint:
    def __init__(self, data: Dict[str, np.array], feature_predict_name: str, method: str = 'C'):
        """
        :param: data the data which will be the input to the decision tree
        :param: method Refers of the tree is 'R' for regression or 'C' for classification
        """
        self.feature_to_predict = data.pop(feature_predict_name, None)
        self.datapoint = data
        self.method = method

    def gini_attribute(self, feature: str, attribute: str):
        element_feature = self.datapoint[feature]
        unique = np.unique(self.feature_to_predict)
        dict_gini = {}

        for i in range(len(unique)):
            dict_gini[unique[i]] = 0
            for j in range(len(element_feature)):
                if element_feature[j] == attribute and self.feature_to_predict[i] == unique[i]:
                    dict_gini[unique[i]] += 1

        gini = np.array(list(dict_gini.values()))
        nb_occurence_attribute = np.sum(gini)
        gini = gini/nb_occurence_attribute

        return 1 - np.sum(gini**2)

    def gini_feature(self, feature: str) -> Dict[str, float]:
        element_feature: np.array = self.datapoint[feature]
        gini_index = {}
        unique, counts = np.unique(element_feature, return_counts=True)
        unique_dict = dict(zip(unique, counts))
        length_data = len(self.datapoint)

        for attribute in element_feature:
            gini_index[attribute] = self.gini_attribute(feature, attribute)
        weighted_sum: float = 0.0
        for attribute, gini in gini_index.items():
            weighted_sum += (unique_dict[attribute]/length_data)*gini

        gini_index['weighted_sum'] = weighted_sum
        return gini_index

    def entropy(self, feature: str) -> float:
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

# Structure of the data :
#   Dict { feature 1 : [ value1, value2, ...], feature 2 : [value1, value2, ...]
