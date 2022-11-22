from tkinter import ttk, constants

class AddCourseView:
    def __init__(self, root, handle_show_frontpage_view):
        self._root = root
        self._handle_show_frontpage_view = handle_show_frontpage_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Lisää kurssi")

        name_label = ttk.Label(master=self._frame, text="Kurssin nimi:")
        name_entry = ttk.Entry(master=self._frame)

        credit_label = ttk.Label(master=self._frame, text="Opintopisteiden määrä:")
        credit_entry = ttk.Entry(master=self._frame)

        add_button = ttk.Button(
            master=self._frame,
            text="Lisää kurssi",
            command=self._handle_show_frontpage_view    
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        name_label.grid(sticky=constants.W, padx=5, pady=5)
        name_entry.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)

        credit_label.grid(sticky=constants.W, padx=5, pady=5)
        credit_entry.grid(row=2, column=1, sticky=constants.EW, padx=5, pady=5)

        add_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)