import sys
import tkinter as tk
from typing import Any

import pandas as pd

import constant
import calculator
import readWrite
import graph

entries: list[Any] = []
fci_dataframe = pd.DataFrame()
depth_to_0 = 0
total_fci = 0
fci_dataframe_fci_10015 = pd.DataFrame()
depth_to_0_fci_10015 = 0
total_fci_fci_10015 = 0


def calculate_fci(*args):
    """
    This calls upon the calculator.calculate_fci method with the entries the user has submitted. Will either show the
    calculated FCI if the entries are correct along with the "Output to Excel" and the "Show graph" buttons, otherwise
    it will populate the error message and display that. This runs when the "Calculate FCI" button is pressed.
    :param args: All of the entries, regardless of object type
    :return None: If there are any errors
    """
    global entries
    global fci_dataframe
    global depth_to_0
    global total_fci
    global fci_dataframe_fci_10015
    global depth_to_0_fci_10015
    global total_fci_fci_10015

    depth_to_0_label.config(text="Depth to 0 FCI (cm): ")
    fci_label.config(text="Total FCI (" + constant.fci_unit + "): ")
    depth_to_0_label_fci_10015.config(text="Depth to 0 FCI" + constant.fci_10015_subscript + " (cm): ")
    fci_label_fci_10015.config(text="Total FCI" + constant.fci_10015_subscript + " (" + constant.fci_unit + "): ")

    entries = [*args]

    for i in range(len(entries)):
        try:
            if entries[i] == '':
                warning_label.config(text="Error: Entry missing")
                return None

            entries[i] = float(entries[i])

        except ValueError:
            warning_label.config(text="Error: Entry is not a number")
            entries[i] = None

    if entries[3] <= 0:
        warning_label.config(text="Error: Maximum depth must be greater than 0")
        entries[3] = None

    if not entries[4].is_integer():
        warning_label.config(text="Error: Depth interval must be an integer")
        entries[4] = None
    elif entries[4] <= 0:
        warning_label.config(text="Error: Depth interval must be greater than 0")
        entries[4] = None

    if None in entries:
        return None

    try:
        total_fci, fci_dataframe, depth_to_0, total_fci_fci_10015, fci_dataframe_fci_10015, depth_to_0_fci_10015 = \
            calculator.calculate_fci(entries)

        warning_label.config(text="")

        total_fci_label_text = "Total FCI (" + constant.fci_unit + "): " + str(total_fci)
        fci_label.config(text=total_fci_label_text)

        total_fci_label_fci_10015_text = "Total FCI" + constant.fci_10015_subscript + " (" + constant.fci_unit + "): " \
                                         + str(total_fci_fci_10015)
        fci_label_fci_10015.config(text=total_fci_label_fci_10015_text)

        if depth_to_0 is None:
            depth_to_0_label.config(text="Depth to 0 FCI (cm): Increase max depth")
        else:
            depth_to_0_label_text = "Depth to 0 FCI (cm): " + str(depth_to_0)
            depth_to_0_label.config(text=depth_to_0_label_text)

        if depth_to_0 is None:
            depth_to_0_label.config(text="Depth to 0 FCI (cm): Increase max depth")
        else:
            depth_to_0_label_fci_10015_text = "Depth to 0 FCI" + constant.fci_10015_subscript + " (cm): " \
                                              + str(depth_to_0_fci_10015)
            depth_to_0_label_fci_10015.config(text=depth_to_0_label_fci_10015_text)

        output_to_excel_button.place(relx=0.25, rely=0.85, relwidth=0.24, relheight=0.125)
        show_graph_button.place(relx=0.5, rely=0.85, relwidth=0.24, relheight=0.125)

    except TypeError:
        warning_label.config(text="Error: Frost cracking window invalid")


def output_to_excel():
    """
    Calls upon the readWrite.write_to_excel method. This runs when the "Output to Excel" button is pressed.
    :return None:
    """
    global fci_dataframe
    global entries
    global depth_to_0
    global total_fci
    global fci_dataframe_fci_10015
    global depth_to_0_fci_10015
    global total_fci_fci_10015

    readWrite.write_to_excel(fci_dataframe, entries, depth_to_0, total_fci, fci_dataframe_fci_10015,
                             depth_to_0_fci_10015, total_fci_fci_10015)


def show_graph():
    """
    Calls upon the graph.create_graph and graph.show_graph methods. This runs when the "Show Graph" button is pressed.
    :return None:
    """
    global fci_dataframe

    graph.create_graph(fci_dataframe)
    graph.show_graph()


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
                                     text="Thermal Diffusivity of Rock (" + constant.alpha_unit + "):",
                                     anchor='w',
                                     font=("Times New Roman", 14)
                                     )
thermal_diffusivity_label.place(rely=0.5, relwidth=0.58, relheight=0.075)

thermal_diffusivity_entry = tk.Entry(input_frame, font=("Times New Roman", 14))
thermal_diffusivity_entry.place(relx=0.6, rely=0.5, relwidth=0.4, relheight=0.075)

frost_cracking_window_label = tk.Label(input_frame,
                                       text="Frost Cracking Window (" + constant.degree_symbol
                                            + "C) (maximum to minimum):",
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

# Creation of the "Calculate FCI" button. Utilizes lambda function to get all of the entries currently in the inputs.
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
fci_label.place(rely=0.075, relwidth=0.55, relheight=0.125, anchor='w')

depth_to_0_label = tk.Label(
    output_frame,
    text="Depth to 0 FCI (cm): ",
    fg='#000000',
    anchor='w',
    font=("Times New Roman", 14)
)
depth_to_0_label.place(rely=0.25, relwidth=0.55, relheight=0.125, anchor='w')

fci_label_fci_10015 = tk.Label(
    output_frame,
    text="Total FCI" + constant.fci_10015_subscript + " (" + constant.fci_unit + "): ",
    fg='#000000',
    anchor='w',
    font=("Times New Roman", 14)
)
fci_label_fci_10015.place(rely=0.425, relwidth=0.55, relheight=0.125, anchor='w')

depth_to_0_label_fci_10015 = tk.Label(
    output_frame,
    text="Depth to 0 FCI" + constant.fci_10015_subscript + " (cm): ",
    fg='#000000',
    anchor='w',
    font=("Times New Roman", 14)
)
depth_to_0_label_fci_10015.place(rely=0.6, relwidth=0.55, relheight=0.125, anchor='w')

# Creation of the "Output to Excel" button
output_to_excel_button = tk.Button(output_frame,
                                   text="Output to Excel",
                                   font=("Times New Roman", 14),
                                   command=lambda: output_to_excel()
                                   )

# Creation of the "Show Graph" button
show_graph_button = tk.Button(output_frame,
                              text="Show Graph",
                              font=("Times New Roman", 14),
                              command=lambda: show_graph()
                              )

root.mainloop()

sys.exit()
