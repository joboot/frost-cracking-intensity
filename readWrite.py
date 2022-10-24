import xlsxwriter
import xlwings as xw
import calculator
import pandas as pd
import constant
from xlwings import constants


def main():
    print("readwrite main")


def write_to_excel(dataframe, entries, depth_to_0):
    print("writeToExcel")
    mat = entries[0]
    ta = (entries[1]-entries[2])/2
    max_depth = entries[3]
    depth_interval = entries[4]
    thermal_diffusivity = entries[5]
    frost_cracking_window_max = entries[6]
    frost_cracking_window_min = entries[7]

    # First method, not awful
    # =========================================================================
    number_format = "#,##0"

    book = xw.Book()
    sheet = book.sheets[0]

    data_ex_headers_range = sheet.range("A2").expand('table')
    for border_id in range(7, 13):
        data_ex_headers_range.api.Borders(border_id).Weight = 2
        data_ex_headers_range.api.Borders(border_id).Color = 0xFFFFFF

    sheet['A1'].value = "MAT (" + constant.degree_symbol + "C)"
    sheet['A2'].value = mat

    sheet['B1'].value = constant.ta + " (" + constant.degree_symbol + "C)"
    sheet['B2'].value = ta

    sheet['C1'].value = "Max Depth (cm)"
    sheet['C2'].value = max_depth

    sheet['D1'].value = "Depth interval (cm)"
    sheet['D2'].value = depth_interval

    sheet['E1'].value = "Thermal Diffusivity of Rock (" + constant.alpha_unit + ")"
    sheet['E2'].value = thermal_diffusivity

    sheet['F1'].value = "Frost Cracking window (" + constant.degree_symbol + "C)"
    sheet['F2'].value = str(frost_cracking_window_max) + ' - ' + str(frost_cracking_window_min)

    sheet['G1'].value = "Depth to 0 (cm)"
    sheet['G2'].value = depth_to_0

    sheet['A5'].value = "Depth (cm)"
    sheet['B5'].value = "FCI (" + constant.fci_unit + ")"
    sheet['A6'].value = dataframe

    sheet.range('B6:B2000').number_format = '0.00'

    header_label_range = sheet.range("A1").expand('right')
    header_label_range.column_width = 20

    header_label_range.api.Font.Name = 'Times New Roman'
    header_label_range.api.Font.Size = 12
    header_label_range.api.Font.Bold = True
    header_label_range.api.WrapText = True
    header_label_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter

    for border_id in range(7, 13):
        header_label_range.api.Borders(border_id).Weight = 2

    header_data_range = sheet.range("A2").expand('right')
    header_data_range.row_height = 15
    header_data_range.column_width = 20

    header_data_range.api.Font.Name = 'Times New Roman'
    header_data_range.api.Font.Size = 12
    header_data_range.api.WrapText = True
    header_data_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter

    fci_header_range = sheet.range("A5").expand('right')
    fci_header_range.column_width = 15

    fci_header_range.api.Font.Name = 'Times New Roman'
    fci_header_range.api.Font.Size = 12
    fci_header_range.api.WrapText = True
    fci_header_range.api.Font.Bold = True
    fci_header_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter

    for border_id in range(7, 13):
        fci_header_range.api.Borders(border_id).Weight = 2

    fci_data_range = sheet.range("A6").expand('table')
    fci_data_range.row_height = 15
    fci_data_range.column_width = 15

    fci_data_range.api.Font.Name = 'Times New Roman'
    fci_data_range.api.Font.Size = 12
    fci_data_range.api.WrapText = False
    fci_data_range.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter
    #
    #
    # header_range = sheet.range("A1").expand('right')
    # header_range.color = (112, 173, 71)
    # header_range.api.Font.Color = 0x000000
    # header_range.api.Font.Bold = True
    # header_range.api.Font.Size = 9

    # =========================================================================
    #
    # =========================================================================

    # file_name = "output.xlsx"
    # sheet_name = "Output"
    #
    # writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    # dataframe.to_excel(writer, sheet_name=sheet_name, startrow=4, startcol=0)
    #
    # workbook = writer.book
    # worksheet = writer.sheets[sheet_name]
    # # worksheet.write(0, 0, 'Cryptocurrency Pricing Summary on ' + datetime.now().strftime('%d %b %Y'),
    # #                 workbook.add_format({'bold': True, 'color': '#E26B0A', 'size': 14}))
    #
    # worksheet.write(0, 2, "MAT (" + constant.degree_symbol + "C)")
    # worksheet.write(1, 2, mat)
    # worksheet.set_column(2, 2, 10)
    #
    # worksheet.write(0, 3, constant.ta + " (" + constant.degree_symbol + "C)")
    # worksheet.write(1, 3, ta)
    # worksheet.set_column(3, 3, 10)
    #
    # worksheet.write(0, 4, "Max Depth (cm)")
    # worksheet.write(1, 4, max_depth)
    # worksheet.set_column(4, 4, 15)
    #
    # worksheet.write(0, 5, "Depth interval (cm)")
    # worksheet.write(1, 5, depth_interval)
    # worksheet.set_column(5, 5, 20)
    #
    # worksheet.write(0, 6, "Thermal Diffusivity of rock (" + constant.alpha_unit + ")")
    # worksheet.write(1, 6, thermal_diffusivity)
    # worksheet.set_column(6, 6, 28)
    #
    # worksheet.write(0, 7, "Frost Cracking window (" + constant.degree_symbol + "C)")
    # worksheet.write(1, 7, str(entries[6]) + ' - ' + str(entries[7]))
    # worksheet.set_column(7, 7, 25)
    #
    # workbook.close()
    #
    # # writer.write_cells("A2", entries[0])
    #
    # # ta_dataframe.to_excel(writer, float_format='%.2f', startrow=4, startcol=0)
    # # dataframe.to_excel(writer, )
    # writer.save()


    # =========================================================================
    #
    # =========================================================================

    # workbook = writer.book
    # workbook = xlsxwriter.Workbook('output.xlsx')
    # worksheet = workbook.add_worksheet()
    # worksheet.write_string(0, 0, "MAT")
    # workbook.close()


if __name__ == "__main__":
    main()
