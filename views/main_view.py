from config.config import *
from tkinter import *
from tkinter.ttk import Combobox


class MainView():
    """ Main View of the application.
    """
    def __init__(self, root, controller):
        self.root = root
        self.root.title('Elementary Cellular Automata')
        self.controller = controller

        self.canvas = Canvas(
            self.root,
            bg='white',
            height=HEIGHT,
            width=WIDTH
        )
        self.canvas.pack()

        self.lbl_rules = Label(
            root,
            text='Choose a rule'
        )
        self.lbl_rules.pack()

        self.cbx_rules = Combobox(
            root,
            state='readonly'
        )
        self.cbx_rules.pack()
        self.set_combobox_values()
        self.cbx_rules.current(0)

        self.lbl_gens = Label(
            root,
            text='Generations'
        )
        self.lbl_gens.pack()

        self.spx_gens = Spinbox(
            root,
            from_=1,
            to=100,
            state='readonly'
        )
        self.spx_gens.pack()

        self.btn_reload = Button(
            root,
            text="Reload",
            command=self.controller.reload
        )
        self.btn_reload.pack()

        # Get the height and width
        window_width = root.winfo_reqwidth()
        window_height = root.winfo_reqheight()

        position_right = int(root.winfo_screenwidth() / 2 - WIDTH / 2)
        position_down = int(root.winfo_screenheight() / 2 - HEIGHT)

        # Position the window at the center of the screen
        root.geometry("+{}+{}".format(position_right, position_down))

    def resize_cells(self):
        # Get the dimensions of every cell
        self.cell_width = WIDTH / CELLS
        self.cell_height = HEIGHT / int(self.spx_gens.get())

    def draw_generation(self, cells, n):
        for index in range(CELLS):
            x = index * self.cell_width
            y = n * self.cell_height
            color = ALIVE_COLOR if cells[index] == ALIVE else DEAD_COLOR
            self.canvas.create_rectangle(
                x,
                y,
                x + self.cell_width,
                y + self.cell_height,
                fill=color,
                width=0
            )

    def set_combobox_values(self):
        values = []
        for rule in range(0, 256):
            values.append(rule)
        self.cbx_rules['values'] = values
