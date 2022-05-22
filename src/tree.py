from typing import Dict, List
from src.datapoint import DataPoint


class Node:
    def __init__(self, datapoint: DataPoint):
        """
        Represents a Node of the Tree
        :param datapoint: Datapoint object
        """
        self._data_node = datapoint
        self._pointer = []

    def __repr__(self) -> str:
        if len(self._pointer):
            return f'{self._data_node} -> {self._pointer}'
        else:
            return f'{self._data_node}'

    @property
    def get_data(self) -> DataPoint:
        return self._data_node

    def add_node_to_pointer(self, Node) -> None:
        self._pointer.append(Node)

    def find_pointer(self, data_node) -> "Pointer":
        return next(pointer for pointer in self._pointer if pointer.get_pointer == data_node)


class Pointer:
    def __init(self):
        self.list_node : List[Node] = []

    def __repr(self):
        return f'{self._data_node} -> {self.node}'

    @property
    def get_pointer(self) -> List[Node]:
        return self.list_node


class Tree:
    def __init__(self, datapoint: DataPoint):
        self._datapoint = datapoint

    # Step of the algorithm : - Computation of the gini index for every feature
    #                         - Select the feature which has the minimum value
    #                         - Then, apply the function in a recursive way.
    # The stop condition is : the length of the datapoint is 1 and the gini index is equal to 0
    def build_tree(self) -> Node:
        gini: Dict[str, float] = {}
        features = list(self._datapoint.datapoint.keys())
        for feature in features:
            gini[feature] = self._datapoint.gini_feature(feature)

        if len(set(self._datapoint.feature_to_predict)) == 1:
            return Node(self._datapoint)
        feature_chosen: str = min(gini, key=gini.get)
        pass
