from tkinter import ttk, constants, StringVar
from services.service import service, InvalidCredentialsError


class LoginView:
    def __init__(self, root, handle_show_register_view, handle_login):
        self._root = root
        self._handle_show_register_view = handle_show_register_view
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            service.login(username, password)
            print("sisäänkirjautuminen onnistui")
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Käyttäjänimi tai salasana ei täsmää")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(columnspan=2, sticky=constants.W)

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi", background="#f5cee3")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(sticky=constants.W, padx=5, pady=5)
        self._username_entry.grid(
            row=1, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana", background="#f5cee3")
        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(sticky=constants.W, padx=5, pady=5)
        self._password_entry.grid(
            row=2, column=1, sticky=constants.EW, padx=5, pady=5)

    def _initialize_style(self):
        frame_style = ttk.Style()
        frame_style.configure("TFrame", background="#f5cee3")

        button_style = ttk.Style()
        button_style.configure("TButton", background="#f0a8ce", font="Verdana")

        label_style = ttk.Style()
        label_style.configure("TLabel", background="#f5cee3", font="Verdana")

    def _initialize(self):
        self._initialize_style()

        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Kirjaudu sisään", background="#f5cee3")

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red",
            background="#f5cee3"
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu",
            command=self._login
        )

        register_label = ttk.Label(master=self._frame, text="Ei tunnusta?", background="#f5cee3")
        register_button = ttk.Button(
            master=self._frame,
            text="Luo uusi tunnus",
            command=self._handle_show_register_view
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        self._error_label.grid(padx=5, pady=5)

        login_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        register_label.grid(sticky=constants.EW, padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()
