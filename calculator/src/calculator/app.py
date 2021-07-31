"""
Calculator Example
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial


class Calculator(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        # add 6 boxes
        # box1 -> input text
        # box2 -> button 7 8 9 +
        # box3 -> button 4 5 6 -
        # box4 -> button 1 2 3 *
        # box5 -> . 0 C /
        # box -> Calculate button

        box_1 = toga.Box()
        box_2 = toga.Box()
        box_3 = toga.Box()
        box_4 = toga.Box()
        box_5 = toga.Box()
        box_6 = toga.Box()

        main_box = toga.Box()

        # text_input
        self.input_text = toga.TextInput()
        self.input_text.style.width = 300

        button_7 = toga.Button("7", on_press=partial(self.enter_data, data="7"))
        button_7.style.padding_top = 20

        button_8 = toga.Button("8", on_press=partial(self.enter_data, data="8"))
        button_8.style.padding_top = 20

        button_9 = toga.Button("9", on_press=partial(self.enter_data, data="9"))
        button_9.style.padding_top = 20

        button_plus = toga.Button("+", on_press=partial(self.enter_data, data="+"))
        button_plus.style.padding_top = 20

        # button 4 5 6 -
        button_4 = toga.Button("4", on_press=partial(self.enter_data, data="4"))
        button_4.style.padding_top = 20

        button_5 = toga.Button("5", on_press=partial(self.enter_data, data="5"))
        button_5.style.padding_top = 20

        button_6 = toga.Button("6", on_press=partial(self.enter_data, data="6"))
        button_6.style.padding_top = 20

        button_minus = toga.Button("-", on_press=partial(self.enter_data, data="-"))
        button_minus.style.padding_top = 20

        # button 1 2 3 *
        button_1 = toga.Button("1", on_press=partial(self.enter_data, data="1"))
        button_1.style.padding_top = 20

        button_2 = toga.Button("2", on_press=partial(self.enter_data, data="2"))
        button_2.style.padding_top = 20

        button_3 = toga.Button("3", on_press=partial(self.enter_data, data="3"))
        button_3.style.padding_top = 20

        button_multiply = toga.Button("*", on_press=partial(self.enter_data, data="*"))
        button_multiply.style.padding_top = 20

        # button dot 0 clear /
        button_dot = toga.Button(".", on_press=partial(self.enter_data, data="."))
        button_dot.style.padding_top = 20

        button_0 = toga.Button("0", on_press=partial(self.enter_data, data="0"))
        button_0.style.padding_top = 20

        button_clear = toga.Button("C", on_press=partial(self.enter_data, data="C"))
        button_clear.style.padding_top = 20

        button_divide = toga.Button("/", on_press=partial(self.enter_data, data="/"))
        button_divide.style.padding_top = 20

        # calculate button
        calculate = toga.Button("Calculate", on_press=self.calculate)
        calculate.style.width = 300
        calculate.style.padding_top = 30

        # add buttons to boxes
        box_1.add(self.input_text)

        box_2.add(button_7)
        box_2.add(button_8)
        box_2.add(button_9)
        box_2.add(button_plus)

        box_3.add(button_4)
        box_3.add(button_5)
        box_3.add(button_6)
        box_3.add(button_minus)

        box_4.add(button_1)
        box_4.add(button_2)
        box_4.add(button_3)
        box_4.add(button_multiply)

        box_5.add(button_dot)
        box_5.add(button_0)
        box_5.add(button_clear)
        box_5.add(button_divide)

        box_6.add(calculate)

        # add box_1  to 6 in main box
        main_box.add(box_1)
        main_box.add(box_2)
        main_box.add(box_3)
        main_box.add(box_4)
        main_box.add(box_5)
        main_box.add(box_6)

        main_box.style.update(direction=COLUMN)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def enter_data(self, widget, data):
        if data == "C":
            self.input_text.value = ""
        else:
            self.input_text.value = self.input_text.value + data

    def calculate(self, widget):
        output = eval(self.input_text.value)  # to evaluate string
        self.main_window.info_dialog("Result", str(output))
        # dialog box


def main():
    return Calculator()
