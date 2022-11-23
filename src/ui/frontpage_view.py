from tkinter import ttk, constants
from services.service import service

class FrontPageView:
    def __init__(self, root, handle_go_to_login, handle_add_course):
        self._root = root
        self._handle_to_go_login = handle_go_to_login
        self._handle_add_course = handle_add_course
        self._frame = None
        self._user = service.get_current_user()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout(self):
        service.logout()
        self._logout()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Etusivu")

        user_label = ttk.Label(
            master=self._frame,
            text=f"Moi, {self._user.username}!"
        )

        add_course_button = ttk.Button(
            master=self._frame,
            text="Lisää uusi kurssi",
            command=self._handle_add_course
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._handle_to_go_login
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        user_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        add_course_button.grid(row=2, column=0, sticky=constants.W, padx=5, pady=5)
        logout_button.grid(row=2, column=1, sticky=constants.W, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)