from tkinter import ttk, constants
from services.service import service


class CourseListView:
    def __init__(self, root, courses):
        self._root = root
        self._courses = courses
        self._frame = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize_course_item(self, course):
        item_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=item_frame, text=f"{course.name} ({course.credits} op)")

        label.grid(sticky=constants.W, padx=5, pady=5)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for course in self._courses:
            self._initialize_course_item(course)


class FrontPageView:
    def __init__(self, root, handle_go_to_login, handle_add_course):
        self._root = root
        self._handle_to_go_login = handle_go_to_login
        self._handle_add_course = handle_add_course
        self._frame = None
        self._user = service.get_current_user()
        self._all_credits = service.all_credits()
        self._course_list_view = None
        self._course_list_frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout(self):
        service.logout()
        self._handle_to_go_login()

    def _initialize_course_list(self):
        if self._course_list_view:
            self._course_list_view.destroy()
        
        courses = service.get_courses_by_user()

        self._course_list_view = CourseListView(
            self._course_list_frame,
            courses
        )

        self._course_list_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._course_list_frame = ttk.Frame(master=self._frame)

        heading_label = ttk.Label(master=self._frame, text="Etusivu")

        user_label = ttk.Label(
            master=self._frame,
            text=f"Moi, {self._user.username}!"
        )

        credits_label = ttk.Label(
            master=self._frame,
            text=f"Opintopisteitä yhteensä {self._all_credits}"
        )

        add_course_button = ttk.Button(
            master=self._frame,
            text="Lisää uusi kurssi",
            command=self._handle_add_course
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._logout
        )

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        user_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        credits_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        
        self._initialize_course_list()
        self._course_list_frame.grid(columnspan=2, sticky=constants.EW)

        add_course_button.grid(sticky=constants.W, padx=5, pady=5)
        logout_button.grid(sticky=constants.W, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=300)
        self._frame.grid_columnconfigure(1, weight=1)
