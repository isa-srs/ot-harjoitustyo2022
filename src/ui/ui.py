from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.frontpage_view import FrontPageView
from ui.add_course_view import AddCourseView
from ui.set_grade_view import SetGrade


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
            self._show_add_course_view,
            self._show_set_grade_view
        )

        self._current_view.pack()

    def _show_add_course_view(self):
        self._hide_current_view()

        self._current_view = AddCourseView(
            self._root,
            self._show_frontpage_view
        )

        self._current_view.pack()
    
    def _show_set_grade_view(self):
        self._hide_current_view()

        self._current_view = SetGrade(
            self._root,
            self._show_frontpage_view
        )

        self._current_view.pack()

