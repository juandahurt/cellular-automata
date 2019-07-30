from config.config import CELLS, ALIVE, DEAD
from helpers.binary_converter import BinaryConverter
from random import random


class CellularAutomaton():
    """ Core of the application.

        Represents a Cellular Automaton following a set of rules.
    """
    def __init__(self, rules):
        self.rules = rules
        self.cells = []
        self.converter = BinaryConverter()
        self.init_cells()

    def init_cells(self):
        # Set inital seed
        for index in range(CELLS):
            if index == int(CELLS / 2):
                self.cells.append(ALIVE)
            else:
                self.cells.append(DEAD)

    def get_cell(self, left, me, right):
        binary = [left, me, right]
        dec = self.converter.convert(binary)
        index = 7 - dec
        return self.rules[index]

    def evolve(self):
        next_gen = []
        for index in range(CELLS):
            if index == 0:
                # Left corner
                next_gen.append(0)
                pass
            elif index == CELLS - 1:
                # Right corner
                next_gen.append(0)
                pass
            else:
                left = self.cells[index - 1]
                me = self.cells[index]
                right = self.cells[index + 1]
                cell = self.get_cell(left, me, right)
                next_gen.append(cell)

        self.cells = next_gen.copy()
