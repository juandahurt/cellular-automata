from helpers.file_writer import FileWriter
from models.cellular_automaton import CellularAutomaton
from models.rules import Rules
from tkinter import *
from views.main_view import MainView


class MainController():
    """ Controller for the Main View.
    """
    def __init__(self):
        self.cellular_automaton = None
        self.rules = Rules()
        self.file_writer = FileWriter()
        root = Tk()
        self.main_view = MainView(root, self)
        self.reload()
        root.mainloop()

    def reload(self):
        self.main_view.resize_cells()

        # Get the set of rules
        rule = self.main_view.cbx_rules.get()
        rules = self.rules.get(rule)
        self.cellular_automaton = CellularAutomaton(rules)

        # Get the number of generations
        gens = int(self.main_view.spx_gens.get())
        for gen in range(gens):
            # Draw the generation
            self.main_view.draw_generation(self.cellular_automaton.cells, gen)

            # Add the generation as a row
            self.file_writer.add_row(gen, self.cellular_automaton.cells)

            # The CA evolves!
            self.cellular_automaton.evolve()

        # Write the cellular automaton in a file
        self.file_writer.write(rule, gens)
        self.file_writer.clear_rows()
