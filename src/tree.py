# from typing import List
from src.datapoint import DataPoint


class Node:
    def __init__(self, datapoint: DataPoint):
        """

        :param datapoint:
        """
        self.datapoint = datapoint


    def information_gain(self, feature: str, datapoint: DataPoint) -> float:
        """

        :param feature:
        :param datapoint:
        :return:
        """


