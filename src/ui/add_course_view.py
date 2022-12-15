from tkinter import ttk, constants, StringVar
from services.service import service


class AddCourseView:
    def __init__(self, root, handle_show_frontpage_view):
        self._root = root
        self._handle_show_frontpage_view = handle_show_frontpage_view
        self._frame = None
        self._name_entry = None
        self._credits_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(columnspan=2, sticky=constants.W)

    def _hide_error(self):
        self._error_label.grid_remove()

    def _add_course(self):
        name = self._name_entry.get()
        credits = self._credits_entry.get()

        if len(name) == 0 or len(credits) == 0:
            self._show_error("Kentät eivät voi olla tyhjiä.")
        elif int(credits) not in range(1,11):
            self._show_error("Opintopisteiden määrä tulee olla 1-10.")
        else:
            try:
                service.add_course(name, credits)
                self._handle_show_frontpage_view()
            except:
                print("kurssin lisääminen epäonnistui")

    def _initialize_course_name_field(self):
        name_label = ttk.Label(master=self._frame, text="Kurssin nimi:")
        self._name_entry = ttk.Entry(master=self._frame)

        name_label.grid(sticky=constants.W, padx=5, pady=5)
        self._name_entry.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)
    
    def _initialize_credits_field(self):
        credits_label = ttk.Label(
            master=self._frame, text="Opintopisteiden määrä:")
        self._credits_entry = ttk.Entry(master=self._frame)

        credits_label.grid(sticky=constants.W, padx=5, pady=5)
        self._credits_entry.grid(row=2, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Lisää kurssi")

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        add_button = ttk.Button(
            master=self._frame,
            text="Lisää kurssi",
            command=self._add_course
        )
        return_button = ttk.Button(
            master=self._frame,
            text="Palaa etusivulle",
            command=self._handle_show_frontpage_view
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        
        self._initialize_course_name_field()
        self._initialize_credits_field()

        self._error_label.grid(padx=5, pady=5)

        add_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        return_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()