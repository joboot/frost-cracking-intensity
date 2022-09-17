import tkinter as tk
import constant


def calculate_fci(entry1, entry2, entry3, entry4, entry5):

    print("Button clicked")
    entries = [entry1, entry2, entry3, entry4, entry5]

    for entry in entries:
        try:
            entry = float(entry)
        except ValueError as ve:
            warning_label = tk.Label(input_frame, text="Please ensure your entries are numbers.")
            warning_label.place(relx=0.25, rely=0.7, relwidth=0.48, relheight=0.1)

    print(entries)

        # if type(entry) != int or float:
        #     print("Please ensure your entries are numbers.")


    # print(int(entry1))
    # print(entry2)
    # print(entry3)
    # print(entry4)
    # print(int(entry5))
    print(entry1 + entry5)


degree_symbol = u'\N{DEGREE SIGN}'
print("GUI main")
root = tk.Tk()

canvas = tk.Canvas(root, height=constant.CANVAS_HEIGHT, width=constant.CANVAS_WIDTH)
canvas.pack()

input_frame = tk.Frame(root, bg='#80c1ff', bd=5)
input_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.38, anchor='n')

# Mean annual temp label and entry
mat_label = tk.Label(input_frame, text="Mean Annual Temperature (" + degree_symbol + "C):", anchor='w')
mat_label.place(relwidth=0.58, relheight=0.1)

mat_entry = tk.Entry(input_frame)
mat_entry.place(relx=0.6, relwidth=0.4, relheight=0.1)

max_summer_label = tk.Label(input_frame, text="Maximum Summer Temperature (" + degree_symbol + "C):", anchor='w')
max_summer_label.place(rely=0.12, relwidth=0.58, relheight=0.1)

max_summer_entry = tk.Entry(input_frame)
max_summer_entry.place(relx=0.6, rely=0.12, relwidth=0.4, relheight=0.1)

min_winter_label = tk.Label(input_frame, text="Minimum Winter Temperature (" + degree_symbol + "C):", anchor='w')
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

enter_button = tk.Button(input_frame, text="Calculate FCI", command=lambda: calculate_fci(
    # float(mat_entry.get()),
    # float(max_summer_entry.get()),
    # float(min_winter_entry.get()),
    # float(max_depth_entry.get()),
    # float(delta_depth_entry.get())))
    mat_entry.get(),
    max_summer_entry.get(),
    min_winter_entry.get(),
    max_depth_entry.get(),
    delta_depth_entry.get()))
enter_button.place(relx=0.25, rely=0.85, relwidth=0.48, relheight=0.1)

output_frame = tk.Frame(root, bg='#eb4034', bd=5)
output_frame.place(relx=0.5, rely=0.9, relwidth=0.75, relheight=0.38, anchor='s')

root.mainloop()



