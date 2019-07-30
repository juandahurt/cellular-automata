from config.config import *
from tkinter import *
from tkinter.ttk import Combobox


class MainView():
    """ Main View of the application.
    """
    def __init__(self, root, controller):
        self.root = root
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
        position_down = int(root.winfo_screenheight() / 2 - HEIGHT / 2)

        # Position the window at the center of the screen
        root.geometry("+{}+{}".format(position_right, position_down))

        # Get the dimensions of every cell
        self.cell_width = WIDTH / CELLS
        self.cell_height = HEIGHT / GENS

        self.loop()

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
                fill=color
            )

    def set_combobox_values(self):
        values = []
        for rule in range(1, 257):
            values.append(rule)
        self.cbx_rules['values'] = values

    def loop(self):
        # This is the main loop!
        self.root.after(200, self.loop)
