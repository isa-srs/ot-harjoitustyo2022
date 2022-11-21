from tkinter import ttk, constants
from services.service import service

class RegisterView:
    def __init__(self, root, handle_go_to_login):
        self._root = root
        self._handle_login = handle_go_to_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _create_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            service.create_user(username, password)
        except:
            print("todo: error")
        
    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(sticky=constants.W, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(sticky=constants.W, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
    
        heading_label = ttk.Label(master=self._frame, text="Rekisteröidy")

        self._initialize_username_field()
        self._initialize_password_field()

        register_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._create_user)

        login_label = ttk.Label(master=self._frame, text="Sinulla on jo tunnus?")
        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_login
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        register_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        login_label.grid(row=4, column=0, sticky=constants.EW)
        login_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)