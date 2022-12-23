import xlwings as xw
from xlwings import constants

import constant
import graph


def main():
    print("readwrite main")


def write_to_excel(fci_dataframe, entries, depth_to_0, total_fci, fci_dataframe_fci_10015, depth_to_0_fci_10015,
                   total_fci_fci_10015):
    print("writeToExcel")
    mat = entries[0]
    ta = (entries[1] - entries[2]) / 4
    max_depth = entries[3]
    depth_interval = entries[4]
    thermal_diffusivity = entries[5]
    frost_cracking_window_max = entries[6]
    frost_cracking_window_min = entries[7]

    fci_graph = graph.create_graph(fci_dataframe)

    book = xw.Book()
    book.sheets.add()
    sheet1 = book.sheets[0]
    sheet2 = book.sheets[1]

    sheet1.name = "FCI Data"
    sheet2.name = "Graph"

    data_ex_headers_range = sheet1.range("A2").expand('table')
    for border_id in range(7, 13):
        data_ex_headers_range.api.Borders(border_id).Weight = 2
        data_ex_headers_range.api.Borders(border_id).Color = 0xFFFFFF

    sheet1['A1'].value = "Total FCI (" + constant.fci_unit + ")"
    sheet1['A2'].value = total_fci

    sheet1['B1'].value = "Total FCI" + constant.fci_10015_subscript + " (" + constant.fci_unit + ")"
    sheet1['B2'].value = total_fci_fci_10015

    sheet1['C1'].value = "MAT (" + constant.degree_symbol + "C)"
    sheet1['C2'].value = mat

    sheet1['D1'].value = constant.ta + " (" + constant.degree_symbol + "C)"
    sheet1['D2'].value = ta

    sheet1['E1'].value = "Max Depth (cm)"
    sheet1['E2'].value = max_depth

    sheet1['F1'].value = "Depth interval (cm)"
    sheet1['F2'].value = depth_interval

    sheet1['G1'].value = "Thermal Diffusivity of Rock (" + constant.alpha_unit + ")"
    sheet1['G2'].value = thermal_diffusivity

    sheet1['H1'].value = "Frost Cracking window (" + constant.degree_symbol + "C)"
    sheet1['H2'].value = str(frost_cracking_window_max) + ' - ' + str(frost_cracking_window_min)

    sheet1['I1'].value = "Depth to 0 FCI (cm)"
    sheet1['I2'].value = depth_to_0

    sheet1['J1'].value = "Depth to 0 FCI" + constant.fci_10015_subscript + " (cm)"
    sheet1['J2'].value = depth_to_0_fci_10015

    sheet1['A5'].value = "Depth (cm)"
    sheet1['B5'].value = "FCI (" + constant.fci_unit + ")"
    sheet1['A6'].value = fci_dataframe

    sheet1['D5'].value = "Depth (cm)"
    sheet1['E5'].value = "FCI" + constant.fci_10015_subscript + " (" + constant.fci_unit + ")"
    sheet1['D6'].value = fci_dataframe_fci_10015

    sheet1.range('B6:B2000').number_format = '0.00'
    sheet1.range('E6:E2000').number_format = '0.00'

    # ------------------------------------------------------------------------------------------
    # Header Label
    # ------------------------------------------------------------------------------------------

    header_label_range = sheet1.range("A1").expand('right')
    header_label_range.column_width = 20

    header_label_range.api.Font.Name = 'Arial'
    header_label_range.api.Font.Size = 10
    header_label_range.api.Font.Bold = True
    header_label_range.api.WrapText = True
    header_label_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter

    for border_id in range(7, 13):
        header_label_range.api.Borders(border_id).Weight = 2

    # ------------------------------------------------------------------------------------------
    # Header Data
    # ------------------------------------------------------------------------------------------

    header_data_range = sheet1.range("A2").expand('right')
    header_data_range.row_height = 15
    header_data_range.column_width = 20

    header_data_range.api.Font.Name = 'Arial'
    header_data_range.api.Font.Size = 10
    header_data_range.api.WrapText = True
    header_data_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter

    # ------------------------------------------------------------------------------------------
    # FCI Dataframe Header
    # ------------------------------------------------------------------------------------------
    fci_header_range = sheet1.range("A5").expand('right')
    fci_header_range.column_width = 15

    fci_header_range.api.Font.Name = 'Arial'
    fci_header_range.api.Font.Size = 10
    fci_header_range.api.WrapText = True
    fci_header_range.api.Font.Bold = True
    fci_header_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter

    for border_id in range(7, 13):
        fci_header_range.api.Borders(border_id).Weight = 2

    # ------------------------------------------------------------------------------------------
    # FCI Dataframe Data
    # ------------------------------------------------------------------------------------------

    fci_data_range = sheet1.range("A6").expand('table')
    fci_data_range.row_height = 15
    fci_data_range.column_width = 15

    fci_data_range.api.Font.Name = 'Arial'
    fci_data_range.api.Font.Size = 10
    fci_data_range.api.WrapText = False
    fci_data_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter

    # ------------------------------------------------------------------------------------------
    # FCI_10015 Dataframe Header
    # ------------------------------------------------------------------------------------------
    fci_10015_header_range = sheet1.range("D5").expand('right')
    fci_10015_header_range.column_width = 15

    fci_10015_header_range.api.Font.Name = 'Arial'
    fci_10015_header_range.api.Font.Size = 10
    fci_10015_header_range.api.WrapText = True
    fci_10015_header_range.api.Font.Bold = True
    fci_10015_header_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter

    for border_id in range(7, 13):
        fci_10015_header_range.api.Borders(border_id).Weight = 2

    # ------------------------------------------------------------------------------------------
    # FCI_10015 Dataframe Data
    # ------------------------------------------------------------------------------------------

    fci_10015_data_range = sheet1.range("D6").expand('table')
    fci_10015_data_range.row_height = 15
    fci_10015_data_range.column_width = 15

    fci_10015_data_range.api.Font.Name = 'Arial'
    fci_10015_data_range.api.Font.Size = 10
    fci_10015_data_range.api.WrapText = False
    fci_10015_data_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter

    sheet2.pictures.add(
        fci_graph,
        name="Matplotlib",
        update=True,
        left=sheet2.range("B4").left,
        top=sheet2.range("B4").top,
        height=450,
        width=450
    )


if __name__ == "__main__":
    main()
