from models.cellular_automaton import CellularAutomaton
from models.rules import Rules
from tkinter import *
from views.main_view import MainView


class MainController():
    """ Controller for the Main View.
    """
    def __init__(self):
        self.ca = None
        self.rules = Rules()
        root = Tk()
        self.main_view = MainView(root, self)
        self.reload()
        root.mainloop()

    def reload(self):
        self.main_view.resize_cells()

        # Get the set of rules
        rule = self.main_view.cbx_rules.get()
        rules = self.rules.get(rule)
        self.ca = CellularAutomaton(rules)

        # Get the number of generations
        gens = int(self.main_view.spx_gens.get())
        for gen in range(gens):
            # Draw the generation
            self.main_view.draw_generation(self.ca.cells, gen)

            # Add the generation as a row
            self.ca.add_row(gen)

            # The CA evolves!
            self.ca.evolve()

        # Write the cellular automaton in a file
        self.ca.save(rule, gens)
