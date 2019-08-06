from prettytable import PrettyTable
from config.config import PATH


class FileWriter():
    """ This class allows to write the generations of a Cellular Automaton
        as a table in a file.
    """
    def __init__(self):
        self.info_table = PrettyTable(['Rule', 'No. Generations'])
        self.gens_table = PrettyTable(['Generation', 'Cells'])

    def add_row(self, gen, cells):
        self.gens_table.add_row([gen, cells])

    def clear_rows(self):
        self.gens_table.clear_rows()
        self.info_table.clear_rows()

    def write(self, rule, gens):
        self.info_table.add_row([rule, gens])

        # Write the tables
        with open(PATH, 'w') as f:
            f.write(str(self.info_table))
            f.write('\n')
            f.write(str(self.gens_table))
