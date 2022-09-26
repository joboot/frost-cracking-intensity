import sys
import tkinter as tk
import constant
import calculator
import readWrite
import pandas as pd

fci_dataframe = pd.DataFrame()
entries = []


def calculate_fci(*args):
    global fci_dataframe
    global entries
    print("Button clicked")
    entries = [*args]

    for i in range(len(entries)):
        try:
            if entries[i] == '':
                warning_label.config(text="Error: Entry missing")
                return None

            entries[i] = float(entries[i])

        except ValueError as ve:
            warning_label.config(text="Error: Entry is not a number")
            entries[i] = None

    # print(entries)
    if None in entries:
        return None

    try:
        total_fci, fci_dataframe = calculator.calculate(entries)
        warning_label.config(text="")
        total_fci = "Total FCI (" + constant.fci_unit + "): " + str(total_fci)

        fci_label.config(text=total_fci)
        output_to_excel_button.place(relx=0.25, rely=0.85, relwidth=0.48, relheight=0.125)

    except TypeError as te:
        print(te)
        warning_label.config(text="Error: Frost cracking window invalid")




def output_to_excel():
    global fci_dataframe
    global entries
    print('output function')

    readWrite.write_to_excel(fci_dataframe, entries)


root = tk.Tk()
root.title("Frost Cracking Intensity Calculator")

canvas = tk.Canvas(root, height=constant.CANVAS_HEIGHT, width=constant.CANVAS_WIDTH)
canvas.pack()

input_frame = tk.Frame(root, bg='#ffffff', bd=5)
input_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.5, anchor='n')

output_frame = tk.Frame(root, bg='#ffffff', bd=5)
output_frame.place(relx=0.5, rely=0.9, relwidth=0.75, relheight=0.26, anchor='s')

# Mean annual temp label and entry
mat_label = tk.Label(input_frame,
                     text="Mean Annual Temperature (" + constant.degree_symbol + "C):",
                     anchor='w',
                     font=("Times New Roman", 14)
                     )
mat_label.place(relwidth=0.58, relheight=0.075)

mat_entry = tk.Entry(input_frame, font=("Times New Roman", 14))
mat_entry.place(relx=0.6, relwidth=0.4, relheight=0.075)

max_summer_label = tk.Label(input_frame,
                            text="Maximum Summer Temperature (" + constant.degree_symbol + "C):",
                            anchor='w',
                            font=("Times New Roman", 14)
                            )
max_summer_label.place(rely=0.1, relwidth=0.58, relheight=0.075)

max_summer_entry = tk.Entry(input_frame, font=("Times New Roman", 14))
max_summer_entry.place(relx=0.6, rely=0.1, relwidth=0.4, relheight=0.075)

min_winter_label = tk.Label(input_frame,
                            text="Minimum Winter Temperature (" + constant.degree_symbol + "C):",
                            anchor='w',
                            font=("Times New Roman", 14)
                            )
min_winter_label.place(rely=0.2, relwidth=0.58, relheight=0.075)

min_winter_entry = tk.Entry(input_frame, font=("Times New Roman", 14))
min_winter_entry.place(relx=0.6, rely=0.2, relwidth=0.4, relheight=0.075)

max_depth_label = tk.Label(input_frame,
                           text="Maximum Depth (cm): ",
                           anchor='w',
                           font=("Times New Roman", 14)
                           )
max_depth_label.place(rely=0.3, relwidth=0.58, relheight=0.075)

max_depth_entry = tk.Entry(input_frame, font=("Times New Roman", 14))
max_depth_entry.place(relx=0.6, rely=0.3, relwidth=0.4, relheight=0.075)

delta_depth_label = tk.Label(input_frame,
                             text="Depth Interval (cm): ",
                             anchor='w',
                             font=("Times New Roman", 14)
                             )
delta_depth_label.place(rely=0.4, relwidth=0.58, relheight=0.075)

delta_depth_entry = tk.Entry(input_frame, font=("Times New Roman", 14))
delta_depth_entry.place(relx=0.6, rely=0.4, relwidth=0.4, relheight=0.075)

thermal_diffusivity_label = tk.Label(input_frame,
                                     text="Thermal Diffusivity of rock (" + constant.alpha_unit + "):",
                                     anchor='w',
                                     font=("Times New Roman", 14)
                                     )
thermal_diffusivity_label.place(rely=0.5, relwidth=0.58, relheight=0.075)

thermal_diffusivity_entry = tk.Entry(input_frame, font=("Times New Roman", 14))
thermal_diffusivity_entry.place(relx=0.6, rely=0.5, relwidth=0.4, relheight=0.075)

frost_cracking_window_label = tk.Label(input_frame,
                                       text="Frost Cracking Window (" + constant.degree_symbol + "C) (max to min):",
                                       anchor='w',
                                       font=("Times New Roman", 14)
                                       )
frost_cracking_window_label.place(rely=0.6, relwidth=0.58, relheight=0.075)

frost_cracking_window_dash_label = tk.Label(input_frame,
                                            text=" - ",
                                            font=("Times New Roman", 14),
                                            bg='#ffffff'
                                            )
frost_cracking_window_dash_label.place(relx=0.675, rely=0.6, relwidth=0.1, relheight=0.075)

window_max_entry = tk.Entry(input_frame, font=("Times New Roman", 14))
window_max_entry.place(relx=0.6, rely=0.6, relwidth=0.1, relheight=0.075)

window_min_entry = tk.Entry(input_frame, font=("Times New Roman", 14))
window_min_entry.place(relx=0.75, rely=0.6, relwidth=0.1, relheight=0.075)

calculate_fci_button = tk.Button(input_frame,
                                 text="Calculate FCI",
                                 font=("Times New Roman", 14),
                                 command=lambda: calculate_fci(
                                     mat_entry.get(),
                                     max_summer_entry.get(),
                                     min_winter_entry.get(),
                                     max_depth_entry.get(),
                                     delta_depth_entry.get(),
                                     thermal_diffusivity_entry.get(),
                                     window_max_entry.get(),
                                     window_min_entry.get())
                                 )
calculate_fci_button.place(relx=0.25, rely=0.85, relwidth=0.48, relheight=0.075)

warning_label = tk.Label(
    input_frame,
    text="",
    font=("Times New Roman", 14),
    bg='#ffffff',
    fg='#ff0000'
)
warning_label.place(relx=0.15, rely=0.75, relwidth=0.7, relheight=0.075)

fci_label = tk.Label(
    output_frame,
    text="Total FCI (" + constant.fci_unit + "): ",
    fg='#000000',
    anchor='w',
    font=("Times New Roman", 14)
)
fci_label.place(rely=0.075, relwidth=0.45, relheight=0.125, anchor='w')

output_to_excel_button = tk.Button(output_frame,
                                   text="Output to Excel",
                                   font=("Times New Roman", 14),
                                   command=lambda: output_to_excel()
                                   )

root.mainloop()

sys.exit()
