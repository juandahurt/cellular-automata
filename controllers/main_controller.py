from config.config import GENS
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
        # Get the set of rules
        rule_n = self.main_view.cbx_rules.get()
        rules = self.rules.get(rule_n)
        self.cellular_automaton = CellularAutomaton(rules)
        print(self.cellular_automaton.cells)
        for gen in range(GENS):
            self.main_view.draw_generation(self.cellular_automaton.cells, gen)
            self.cellular_automaton.evolve()
