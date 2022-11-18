from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, handle_register):
        self._root = root
        self._handle_register = handle_register
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Kirjaudu sisään")
        
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        username_entry = ttk.Entry(master=self._frame)
        
        password_label = ttk.Label(master=self._frame, text="Salasana")
        password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(master=self._frame, text="Kirjaudu")

        register_label = ttk.Label(master=self._frame, text="Ei tunnusta?")
        register_button = ttk.Button(
            master=self._frame,
            text="Luo uusi tunnus",
            command=self._handle_register
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=constants.EW, padx=5, pady=5)

        login_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        register_label.grid(row=4, column=0, sticky=constants.EW)
        register_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)