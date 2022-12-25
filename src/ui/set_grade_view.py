from tkinter import ttk, constants, StringVar
from services.service import service


class SetGrade:
    def __init__(self,root, handle_show_frontpage_view):
        self._root = root
        self._handle_show_frontpage_view = handle_show_frontpage_view
        self._frame = None
        self._course = service.get_current_course()
        self._grade_entry = None
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
    
    def _set_grade(self):
        grade = self._grade_entry.get()
        grades = [str(x) for x in range(1,6)]

        if len(grade) == 0:
            self._show_error("Kenttä ei voi olla tyhjä.")
        elif grade not in grades:
            self._show_error("Syötä kelvollinen arvosana (1-5)")
        else:
            try:
                service.set_course_completed(self._course, grade)
                service.set_current_course(None)
                self._handle_show_frontpage_view()
            except:
                print("arvosanan merkitseminen epäonnistui")
    
    def _initialize_grade_field(self):
        grade_label = ttk.Label(master=self._frame, text="Arvosana:")
        self._grade_entry = ttk.Entry(master=self._frame)

        grade_label.grid(row=1, column= 0, sticky=constants.W, padx=5, pady=5)
        self._grade_entry.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)

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

        heading_label = ttk.Label(master=self._frame, text="Syötä kurssista saatu arvosana saadaksesi kurssisuoritus")

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        button = ttk.Button(
            master=self._frame,
            text="Merkitse suoritetuksi",
            command=self._set_grade
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Palaa etusivulle",
            command=self._handle_show_frontpage_view
        )

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        self._initialize_grade_field()

        self._error_label.grid(padx=5, pady=5)

        button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        return_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()