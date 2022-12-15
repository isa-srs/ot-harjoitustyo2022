from tkinter import ttk, constants
from services.service import service


class CourseListView:
    def __init__(self, root, courses, handle_delete_course):
        self._root = root
        self._courses = courses
        self._handle_delete_course = handle_delete_course
        self._frame = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()        
    
    def _initialize_course_item(self, course):
        item_frame = ttk.Frame(master=self._frame)

        name_label = ttk.Label(master=item_frame, text=f"{course.name}")
        credit_label = ttk.Label(master=item_frame, text=f"{course.credits} op")

        delete_button = ttk.Button(
            master=item_frame,
            text="Poista",
            command=lambda: self._handle_delete_course(course)
        )

        name_label.grid(sticky=constants.W, padx=5, pady=5)
        credit_label.grid(sticky=constants.W, padx=5, pady=5)
        delete_button.grid(sticky=constants.W, padx=5, pady=5)

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
        self._courses = service.get_courses_by_user()
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
    
    def _handle_delete_course(self, course):
        service.delete_course(course.name)
        self._initialize_course_list()

    def _initialize_course_list(self):
        if self._course_list_view:
            self._course_list_view.destroy()

        self._course_list_view = CourseListView(
            self._course_list_frame,
            self._courses,
            self._handle_delete_course
        )

        self._course_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Moi, {self._user.username}!"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._logout
        )

        credits_label = ttk.Label(
            master=self._frame,
            text=f"Opintopisteesi yhteensä {self._all_credits}"
        )

        user_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        logout_button.grid(row=0, column=1, sticky=constants.SE, padx=5)
        credits_label.grid(sticky=constants.W, padx=5, pady=5)
    
    def _initialize_style(self):
        frame_style = ttk.Style()
        frame_style.configure("TFrame", background="#f5cee3")

        button_style = ttk.Style()
        button_style.configure("TButton", background="#f0a8ce")

        label_style = ttk.Style()
        label_style.configure("TLabel", background="#f5cee3")

    def _initialize(self):
        self._initialize_style()

        self._frame = ttk.Frame(master=self._root)
        self._course_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()

        add_course_button = ttk.Button(
            master=self._frame,
            text="Lisää uusi kurssi",
            command=self._handle_add_course
        )

        if len(self._courses) == 0:
            no_courses = ttk.Label(master=self._frame, text="Et ole lisännyt vielä kursseja.")
            no_courses.grid(sticky=constants.W, padx=5, pady=5)
            
        add_course_button.grid(sticky=constants.W, padx=5, pady=5)
        
        if len(self._courses) > 0:
            course_label = ttk.Label(master=self._frame, text="Kurssit:")
            course_label.grid(sticky=constants.W, padx=5, pady=5)
        
        self._initialize_course_list()
        self._course_list_frame.grid(columnspan=2, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=300)
        self._frame.grid_columnconfigure(1, weight=1)
