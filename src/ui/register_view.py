from tkinter import ttk, constants

class RegisterView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
    
        heading_label = ttk.Label(master=self._frame, text="Rekisteröidy")
        
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        username_entry = ttk.Entry(master=self._frame)
        
        password_label = ttk.Label(master=self._frame, text="Salasana")
        password_entry = ttk.Entry(master=self._frame)

        register_button = ttk.Button(master=self._frame, text="Rekisteröidy")

        login_label = ttk.Label(master=self._frame, text="Sinulla on jo tunnus?")
        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_login
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=constants.EW, padx=5, pady=5)

        register_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        login_label.grid(row=4, column=0, sticky=constants.EW)
        login_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)