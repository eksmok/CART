from typing import Dict, List
from src.datapoint import DataPoint, Gini
import numpy as np


class Node:
    def __init__(self, datapoint: DataPoint):
        """
        Represents a Node of the Tree
        :param datapoint: Datapoint object
        """
        self.data_node = datapoint
        self._pointer: Pointer = Pointer()

    # def __repr__(self) -> str:
    #     if len(self._pointer.list_node):
    #         return f'{self.data_node} -> {self._pointer}'
    #     else:
    #         return f'{self.data_node}'

    @property
    def get_data(self) -> DataPoint:
        return self.data_node

    def add_node_to_pointer(self, node) -> None:
        self._pointer.list_node.append(node)

    # def find_pointer(self, data_node) -> "Pointer":
        # return next(pointer for pointer in self._pointer if pointer.get_pointer == data_node)


class Pointer:
    def __init(self):
        self.list_node: List[Node] = []
        self._data_node = None
        self._node = None

    def __repr(self):
        return f'{self._data_node} -> {self._node}'

    @property
    def get_pointer(self) -> List[Node]:
        return self.list_node


class Leaf:
    def __init__(self, dataset: DataPoint):
        self._dataset = dataset


class Tree:
    def __init__(self):
        self._exit: bool = False
        self.list_node = []

    # Step of the algorithm : - Computation of the gini index for every feature
    #                         - Select the feature which has the minimum value
    #                         - Then, apply the function in a recursive way.
    # The stop condition is : the length of the dataset is 1 and the gini index is equal to 0
    def build_tree(self, node: Node) -> Leaf:
        self.list_node.append(node)
        features = list(node.data_node.datapoint.keys())
        dataset: Dict[str, np.ndarray] = node.data_node.datapoint
        gini = self._get_gini_index(features=features, dataset=dataset)

        if self._exit_condition(node):
            return Leaf(DataPoint(dataset, feature_predict_name=node.data_node.feature_to_predict))

        feature_chosen: str = min(gini, key=gini.get)
        feature_chosen_value: np.ndarray = dataset[feature_chosen]
        for value in feature_chosen_value:
            dataset_filtered_by_value = self._filter_feature_value(value, feature_chosen, node)
            new_node = Node(DataPoint(dataset_filtered_by_value, node.data_node.feature_to_predict))
            node.add_node_to_pointer(new_node)
            return self.build_tree(node=new_node)

    def _exit_condition(self, node):
        if len(set(node.data_node.datapoint.feature_to_predict)) == 1:
            self._exit = True
        return self._exit

    @staticmethod
    def _get_gini_index(features: List[str], dataset: Dict[str, np.ndarray]):
        metric: Gini = Gini()
        gini: Dict[str, float] = {}
        for feature in features:
            gini[feature] = metric.gini_feature(feature=feature, dataset=dataset)
        return gini

    def _filter_feature_value(self, value: any, feature_chosen_values: np.ndarray, node: Node) -> Dict[str, np.ndarray]:
        dataset_filtered = self._initialize_dataset(node)
        length_dataset = len(feature_chosen_values)
        for i in range(length_dataset):
            if feature_chosen_values[i] == value:
                dataset_filtered = self._add_value_every_feature(index=i, dataset_filtered=dataset_filtered, node=node)
        return dataset_filtered

    @staticmethod
    def _initialize_dataset(node: Node):
        dataset: Dict[str, List] = {}
        for feature in node.data_node.datapoint.keys():
            dataset[feature] = []
        return dataset

    @staticmethod
    def _add_value_every_feature(index: int, dataset_filtered: Dict[str, List], node: Node) -> Dict[str, List]:
        for feature in node.data_node.datapoint:
            dataset_filtered[feature].append(node.data_node.datapoint[feature][index])
        return dataset_filtered
