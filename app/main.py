'''
    Application - A code explainer for SQL
'''
from tkinter import END, messagebox
from typing import Tuple
from utils.interpret import explain_code
import customtkinter


# Creating home configs
customtkinter.set_appearance_mode("Dark")


def alert_error(error_message):
    '''
        Show alert for error
    '''
    messagebox.showerror(title="Error founded", message=error_message)


def alert_information(information_message):
    '''
        Show alert for information
    '''
    messagebox.showinfo(message=information_message)


class Retiql(customtkinter.CTk):
    '''
        Creating the app for SQL code explainer
    '''

    def __init__(self, fg_color: str | Tuple[str, str] | None = None,
                 **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title('Retiql')
        self.geometry("1466X868")

        # Screen components
        # Title
        self.app_name = customtkinter.CTkLabel(
            self, text="Retiql", font=customtkinter.CTkFont(
                family='Modern No. 20', size=32,
                weight='bold'))

        self.app_name.pack(pady=12)

        # Description
        self._description_app = customtkinter.CTkLabel(
            self, text=(
                '''
A SQL code explainer. It uses Python to articulate the SQL code in a simple way
'''),
            font=customtkinter.CTkFont(
                family='Trebuchet MS', slant='italic'),
        )
        self._description_app.pack()

        # Input code field
        self.input_output_frame = customtkinter.CTkFrame(
            self, fg_color=("gray100", "gray15"))
        self.input_output_frame.pack(pady=10)

        self.input_frame = customtkinter.CTkFrame(self.input_output_frame)
        self.input_frame.pack(padx=10, side="left")

        self.input_label = customtkinter.CTkLabel(
            self.input_frame, text="Input", font=customtkinter.CTkFont(
                family="Yu Gothic UI Semibold"))
        self.input_label.pack()

        self.input_textarea = customtkinter.CTkTextbox(
            self.input_frame, width=550, height=400,
            font=customtkinter.CTkFont(family="Courier"),
            corner_radius=0, wrap="none")
        self.input_textarea.pack()

        # Interpret button
        self.interpret_button = customtkinter.CTkButton(
            self.input_frame, text='Translate',
            fg_color=("green"), hover_color=('#19692c'),
            command=self.interpret_query,
            font=customtkinter.CTkFont(family="@Yu Gothic UI", weight="bold"))
        self.interpret_button.pack(side='right', pady=10, padx=10)

        # Clear button
        self.clear_button = customtkinter.CTkButton(
            self.input_frame, text='Clear',
            fg_color='red',
            hover_color=("#DB3E39", "#821D1A"),
            command=self.clear_query,
            font=customtkinter.CTkFont(family="@Yu Gothic UI", weight="bold")
        )
        self.clear_button.pack(side="right", pady=10, padx=10)

        # Output translated field
        self.output_frame = customtkinter.CTkFrame(self.input_output_frame)
        self.output_frame.pack(padx=10)

        self.output_label = customtkinter.CTkLabel(
            self.output_frame, text="Output",
            font=customtkinter.CTkFont(family="Yu Gothic UI Semibold"))
        self.output_label.pack()

        self.output_textarea = customtkinter.CTkTextbox(
            self.output_frame, width=550, height=400,
            font=customtkinter.CTkFont(family="Trebuchet MS"),
            fg_color="transparent", corner_radius=0,
            wrap="word"
        )

        self.output_textarea.configure(state='disabled')
        self.output_textarea.pack()

        # Copy explanation button
        self.copy_button = customtkinter.CTkButton(
            self.output_frame, text='Copy',
            command=self.get_output_text, font=customtkinter.CTkFont(
                family="@Yu Gothic UI", weight="bold"))
        self.copy_button.pack(pady=10, padx=10)

    def clear_query(self):
        '''
            Clear query from input and output textarea
        '''
        self.input_textarea.delete("0.0", END)
        self.output_textarea.configure(state='normal')
        self.output_textarea.delete("0.0", END)
        self.output_textarea.configure(state='disabled')

    def get_output_text(self):
        '''
            Get output text from textarea
        '''
        transference_area = self.output_textarea.get("0.0", END)
        if transference_area != "\n" and transference_area != "":
            self.copy_button.configure(text="Coppied !")

            self.clipboard_clear()
            self.clipboard_append(transference_area)
            alert_information("Text coppied to clipboard !")

            self.copy_button.configure(text="Coppy")

        else:
            alert_error("The text isn't able to copy.")

    def interpret_query(self):
        '''
            Get the query code and translate
        '''
        query = self.input_textarea.get("0.0", END).strip()

        if self.output_textarea.get("0.0", END) != "":
            self.output_textarea.configure(state='normal')
            self.output_textarea.delete("0.0", END)
            self.output_textarea.insert(END, "\n")
        if query == "":
            alert_error("The text isn't valid to translate.")
        else:
            translate = explain_code(query)
            self.output_textarea.insert("1.0", translate)
            self.output_textarea.insert(END, "\n")
            self.output_textarea.configure(state='disabled')


if __name__ == '__main__':
    retiql = Retiql()
    retiql.mainloop()
