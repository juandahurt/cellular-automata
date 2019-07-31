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
        root = Tk()
        self.main_view = MainView(root, self)
        self.reload()
        root.mainloop()

    def reload(self):
        self.main_view.resize_cells()
        # Get the set of rules
        rule_n = self.main_view.cbx_rules.get()
        rules = self.rules.get(rule_n)
        self.cellular_automaton = CellularAutomaton(rules)

        # Get the number of generatios
        gens = int(self.main_view.spx_gens.get())
        for gen in range(gens):
            self.main_view.draw_generation(self.cellular_automaton.cells, gen)
            self.cellular_automaton.evolve()
