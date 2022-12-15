from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Opintojen seurantasovellus")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
