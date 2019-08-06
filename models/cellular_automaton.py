from config.config import CELLS, ALIVE, DEAD
from helpers.binary_converter import BinaryConverter
from helpers.file_writer import FileWriter
from random import random


class CellularAutomaton():
    """ Core of the application.

        Represents a Cellular Automaton following a set of rules.
    """
    def __init__(self, rules):
        self.rules = rules
        self.cells = []
        self.converter = BinaryConverter()
        self.file_writer = FileWriter()
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
        dec = self.converter.convert_to_dec(binary)
        index = 7 - dec
        return self.rules[index]

    def evolve(self):
        next_gen = []
        for index in range(CELLS):
            me = self.cells[index]
            if index == 0:
                # Left corner
                left = self.cells[CELLS - 1]
                right = self.cells[index + 1]
            elif index == CELLS - 1:
                # Right corner
                right = self.cells[0]
                left = self.cells[index - 1]
            else:
                right = self.cells[index + 1]
                left = self.cells[index - 1]
            cell = self.get_cell(left, me, right)
            next_gen.append(cell)

        self.cells = next_gen.copy()

    def add_row(self, gen):
        print(self.cells)
        self.file_writer.add_row(gen, self.cells)

    def save(self, rule, gens):
        # Write the CA
        self.file_writer.write(rule, gens)

        # Clear rows
        self.file_writer.clear_rows()
