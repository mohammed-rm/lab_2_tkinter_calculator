from tkinter import Tk, Menu, Button, Entry, END, Label
from math import cos, sin, tan, log, exp, sqrt, pi


class Calculator(Tk):
    def __init__(self):
        super(Calculator, self).__init__()
        self.configure(bg='gray')
        self.title("Calculator")
        self.geometry("315x500")
        self.display: Entry = Entry()
        self.menu: Menu = Menu()
        self.standard: bool = False
        self.scientific: bool = False
        self.help: bool = False
        self.display_zone: bool = False

        # Center the window
        self.center_window()

        # Items
        self.create_display_zone()
        self.create_stantard_mode_buttons()
        self.create_menu()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.deiconify()

    def create_display_zone(self):
        self.display_zone = True
        self.display = Entry(self, width=20, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    def remove_display_zone(self):
        self.display_zone = False
        for widget in self.winfo_children():
            if widget.widgetName == "entry":
                widget.destroy()

    def create_menu(self):
        menu_bar = Menu(self)
        self.menu = Menu(menu_bar, tearoff=0, bg='tan')
        menu_bar.add_cascade(label="Menu", menu=self.menu)
        self.menu.add_command(label="Standard", command=lambda: self.selected_menu("Standard"))
        self.menu.add_command(label="Scientific", command=lambda: self.selected_menu("Scientific"))
        self.menu.add_command(label="Help", command=lambda: self.selected_menu("Help"))
        self.menu.add_command(label="Exit", command=self.quit)
        self.menu.entryconfig("Standard", state="disabled")
        self.config(menu=menu_bar)

    def selected_menu(self, item):
        if item == "Standard":
            self.menu.entryconfig("Standard", state="disabled")
            self.menu.entryconfig("Scientific", state="normal")
            self.menu.entryconfig("Help", state="normal")
            self.remove_scientific_mode_buttons() if self.scientific else None
            self.remove_help_mode_text() if self.help else None
            self.create_stantard_mode_buttons()
            self.create_display_zone() if not self.display_zone else None
        elif item == "Scientific":
            self.menu.entryconfig("Scientific", state="disabled")
            self.menu.entryconfig("Standard", state="normal")
            self.menu.entryconfig("Help", state="normal")
            self.remove_help_mode_text() if self.help else None
            self.create_scientific_mode_buttons()
            self.create_stantard_mode_buttons() if not self.standard else None
            self.create_display_zone() if not self.display_zone else None
        elif item == "Help":
            self.menu.entryconfig("Help", state="disabled")
            self.menu.entryconfig("Standard", state="normal")
            self.menu.entryconfig("Scientific", state="normal")
            self.remove_standard_mode_buttons() if self.standard else None
            self.remove_scientific_mode_buttons() if self.scientific else None
            self.remove_display_zone() if self.display_zone else None
            self.create_help_mode_text()

    def create_stantard_mode_buttons(self):
        self.standard = True
        Button(self, text="7", width=5, height=2, command=lambda: self.write_on_display(7)).grid(row=2, column=0,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text="8", width=5, height=2, command=lambda: self.write_on_display(8)).grid(row=2, column=1,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text="9", width=5, height=2, command=lambda: self.write_on_display(9)).grid(row=2, column=2,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text="/", width=5, height=2, command=lambda: self.write_on_display("/"), bg='cyan').grid(row=2,
                                                                                                              column=3,
                                                                                                              padx=5,
                                                                                                              pady=5)
        Button(self, text="4", width=5, height=2, command=lambda: self.write_on_display(4)).grid(row=3, column=0,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text="5", width=5, height=2, command=lambda: self.write_on_display(5)).grid(row=3, column=1,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text="6", width=5, height=2, command=lambda: self.write_on_display(6)).grid(row=3, column=2,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text="*", width=5, height=2, command=lambda: self.write_on_display("*"), bg='cyan').grid(row=3,
                                                                                                              column=3,
                                                                                                              padx=5,
                                                                                                              pady=5)
        Button(self, text="1", width=5, height=2, command=lambda: self.write_on_display(1)).grid(row=4, column=0,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text="2", width=5, height=2, command=lambda: self.write_on_display(2)).grid(row=4, column=1,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text="3", width=5, height=2, command=lambda: self.write_on_display(3)).grid(row=4, column=2,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text="-", width=5, height=2, command=lambda: self.write_on_display("-"), bg='cyan').grid(row=5,
                                                                                                              column=3,
                                                                                                              padx=5,
                                                                                                              pady=5)
        Button(self, text="0", width=5, height=2, command=lambda: self.write_on_display(0)).grid(row=5, column=0,
                                                                                                 padx=5,
                                                                                                 pady=5)
        Button(self, text=".", width=5, height=2, command=lambda: self.write_on_display(".")).grid(row=5, column=1,
                                                                                                   padx=5,
                                                                                                   pady=5)
        Button(self, text="=", width=5, height=2, command=lambda: self.calculate_result(), bg='green').grid(row=5,
                                                                                                            column=2,
                                                                                                            padx=5,
                                                                                                            pady=5)
        Button(self, text="+", width=5, height=2, command=lambda: self.write_on_display("+"), bg='cyan').grid(row=4,
                                                                                                              column=3,
                                                                                                              padx=5,
                                                                                                              pady=5)

        Button(self, text="AC", width=5, height=2, command=lambda: self.clear_display(), bg='red').grid(row=1, column=0,
                                                                                                        padx=5,
                                                                                                        pady=5)

        Button(self, text="C", width=5, height=2, command=lambda: self.delete_last(), bg='red').grid(row=1, column=1,
                                                                                                     padx=5,
                                                                                                     pady=5)

        Button(self, text="(", width=5, height=2, command=lambda: self.write_on_display("("), bg='cyan').grid(row=1,
                                                                                                              column=2,
                                                                                                              padx=5,
                                                                                                              pady=5)
        Button(self, text=")", width=5, height=2, command=lambda: self.write_on_display(")"), bg='cyan').grid(row=1,
                                                                                                              column=3,
                                                                                                              padx=5,
                                                                                                              pady=5)

    def remove_standard_mode_buttons(self):
        self.standard = False
        for widget in self.winfo_children():
            if widget.grid_info().get("row", 1) <= 6 and widget.grid_info().get("row",
                                                                                1) > 0 and widget.widgetName != "menu":
                widget.destroy()

    def create_scientific_mode_buttons(self):
        self.scientific = True
        Button(self, text="x²", width=5, height=2, command=lambda: self.write_on_display("**2"), bg='orange').grid(
            row=6, column=0,
            padx=5,
            pady=5)
        Button(self, text="x³", width=5, height=2, command=lambda: self.write_on_display("**3"), bg='orange').grid(
            row=6, column=1,
            padx=5,
            pady=5)
        Button(self, text="xⁿ", width=5, height=2, command=lambda: self.write_on_display("**"), bg='orange').grid(
            row=6,
            column=2,
            padx=5,
            pady=5)
        Button(self, text="√", width=5, height=2, command=lambda: self.write_on_display("sqrt("), bg='orange').grid(
            row=6, column=3,
            padx=5,
            pady=5)

        Button(self, text="sin", width=5, height=2, command=lambda: self.write_on_display("sin("), bg='orange').grid(
            row=7, column=0,
            padx=5,
            pady=5)
        Button(self, text="cos", width=5, height=2, command=lambda: self.write_on_display("cos("), bg='orange').grid(
            row=7, column=1,
            padx=5,
            pady=5)
        Button(self, text="tan", width=5, height=2, command=lambda: self.write_on_display("tan("), bg='orange').grid(
            row=7, column=2,
            padx=5,
            pady=5)
        Button(self, text="log", width=5, height=2, command=lambda: self.write_on_display("log("), bg='orange').grid(
            row=7, column=3,
            padx=5,
            pady=5)
        Button(self, text="exp", width=5, height=2, command=lambda: self.write_on_display("exp("), bg='orange').grid(
            row=8, column=0,
            padx=5,
            pady=5)
        Button(self, text="π", width=5, height=2, command=lambda: self.write_on_display("pi"), bg='orange').grid(
            row=8,
            column=1,
            padx=5,
            pady=5)

    def remove_scientific_mode_buttons(self):
        self.scientific = False
        for widget in self.winfo_children():
            if widget.grid_info().get("row", 0) >= 6:
                widget.destroy()

    def create_help_mode_text(self):
        self.help = True
        help_text = "Calculator with Standard and Scientific mode." \
                    "\n\nUse the menu to select the mode." \
                    "\n\nScientific mode:" \
                    "\n\nx²: x to the power of 2" \
                    "\nx³: x to the power of 3" \
                    "\nxⁿ: x to the power of n" \
                    "\n√: square root" \
                    "\nsin: sine" \
                    "\ncos: cosine" \
                    "\ntan: tangent" \
                    "\nlog: logarithm" \
                    "\nexp: exponential" \
                    "\nπ: pi"
        lab = Label(self, text=help_text, font=("Arial", 10))
        lab.pack()

    def remove_help_mode_text(self):
        self.help = False
        for widget in self.winfo_children():
            if widget.widgetName == "label":
                widget.destroy()

    def write_on_display(self, number):
        self.display.insert(END, number)

    def get_input(self):
        return self.display.get()

    def calculate_result(self):
        operation = self.get_input()
        result = eval(operation)
        self.display.delete(0, END)
        self.display.insert(0, result)

    def clear_display(self):
        self.display.delete(0, END)

    def delete_last(self):
        self.display.delete(len(self.display.get()) - 1)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()
