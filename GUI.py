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

    total_fci, fci_dataframe = calculator.calculate(entries)

    warning_label.config(text="")
    total_fci = "Total FCI: " + str(total_fci)

    fci_label.config(text=total_fci)
    output_to_excel_button.place(relx=0.25, rely=0.85, relwidth=0.48, relheight=0.1)


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
input_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.38, anchor='n')

output_frame = tk.Frame(root, bg='#ffffff', bd=5)
output_frame.place(relx=0.5, rely=0.9, relwidth=0.75, relheight=0.38, anchor='s')

# Mean annual temp label and entry
mat_label = tk.Label(input_frame, text="Mean Annual Temperature (" + constant.degree_symbol + "C):", anchor='w')
mat_label.place(relwidth=0.58, relheight=0.1)

mat_entry = tk.Entry(input_frame)
mat_entry.place(relx=0.6, relwidth=0.4, relheight=0.1)

max_summer_label = tk.Label(input_frame, text="Maximum Summer Temperature (" + constant.degree_symbol + "C):", anchor='w')
max_summer_label.place(rely=0.12, relwidth=0.58, relheight=0.1)

max_summer_entry = tk.Entry(input_frame)
max_summer_entry.place(relx=0.6, rely=0.12, relwidth=0.4, relheight=0.1)

min_winter_label = tk.Label(input_frame, text="Minimum Winter Temperature (" + constant.degree_symbol + "C):", anchor='w')
min_winter_label.place(rely=0.24, relwidth=0.58, relheight=0.1)

min_winter_entry = tk.Entry(input_frame)
min_winter_entry.place(relx=0.6, rely=0.24, relwidth=0.4, relheight=0.1)

max_depth_label = tk.Label(input_frame, text="Maximum Depth (cm): ", anchor='w')
max_depth_label.place(rely=0.36, relwidth=0.58, relheight=0.1)

max_depth_entry = tk.Entry(input_frame)
max_depth_entry.place(relx=0.6, rely=0.36, relwidth=0.4, relheight=0.1)

delta_depth_label = tk.Label(input_frame, text="Depth Interval (cm): ", anchor='w')
delta_depth_label.place(rely=0.48, relwidth=0.58, relheight=0.1)

delta_depth_entry = tk.Entry(input_frame)
delta_depth_entry.place(relx=0.6, rely=0.48, relwidth=0.4, relheight=0.1)

calculate_fci_button = tk.Button(input_frame, text="Calculate FCI", command=lambda: calculate_fci(
    mat_entry.get(),
    max_summer_entry.get(),
    min_winter_entry.get(),
    max_depth_entry.get(),
    delta_depth_entry.get()))

calculate_fci_button.place(relx=0.25, rely=0.85, relwidth=0.48, relheight=0.1)

warning_label = tk.Label(
    input_frame,
    text="",
    bg='#ffffff',
    fg='#ff0000')
warning_label.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.1)

fci_label = tk.Label(
    output_frame,
    text="Total FCI: ",
    fg='#000000',
    anchor='w')
fci_label.place(rely=0.05, relwidth=0.25, relheight=0.1, anchor='w')

output_to_excel_button = tk.Button(output_frame, text="Output to excel", command=lambda: output_to_excel())



root.mainloop()

sys.exit()





