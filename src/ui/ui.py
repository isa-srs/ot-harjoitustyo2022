from tkinter import Tk
from login_view import LoginView
from register_view import RegisterView
from frontpage_view import FrontPageView
from add_course_view import AddCourseView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = None

    def _show_register_view(self):
        self._hide_current_view()

        self._current_view = RegisterView(
            self._root,
            self._show_login_view
        )

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_register_view,
            self._show_frontpage_view
        )

        self._current_view.pack()

    def _show_frontpage_view(self):
        self._hide_current_view()

        self._current_view = FrontPageView(
            self._root,
            self._show_login_view,
            self._show_add_course_view
        )

        self._current_view.pack()

    def _show_add_course_view(self):
        self._hide_current_view()

        self._current_view = AddCourseView(
            self._root,
            self._show_frontpage_view
        )

        self._current_view.pack()

window = Tk()
window.title("Sovellus")

ui = UI(window)
ui.start()

window.mainloop()