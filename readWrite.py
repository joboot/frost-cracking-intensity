import xlsxwriter
import xlwings as xw
import calculator
import pandas as pd
import constant


def main():
    print("readwrite main")


def write_to_excel(dataframe, entries):
    print("writeToExcel")
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
    sheet['A2'].value = entries[0]

    sheet['B1'].value = constant.ta + " (" + constant.degree_symbol + "C)"
    sheet['B2'].value = (entries[1]-entries[2])/2

    sheet['C1'].value = "Max Depth (cm)"
    sheet['C2'].value = entries[3]

    sheet['D1'].value = "Depth interval (cm)"
    sheet['D2'].value = entries[4]

    sheet['A5'].value = "Depth (cm)"
    sheet['B5'].value = "FCI (" + constant.fci_unit + ")"
    sheet['A6'].value = dataframe

    sheet.range('B6:B500').number_format = '0.00'

    header_data_range = sheet.range("A1").expand('table')
    header_data_range.row_height = 15
    header_data_range.column_width = 15

    header_data_range.api.Font.Name = 'Times New Roman'
    header_data_range.api.Font.Size = 12
    header_data_range.api.WrapText = False

    fci_data_range = sheet.range("A5").expand('table')
    fci_data_range.row_height = 15
    fci_data_range.column_width = 15

    fci_data_range.api.Font.Name = 'Times New Roman'
    fci_data_range.api.Font.Size = 12
    fci_data_range.api.WrapText = False

    # fci_data_range.api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter
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

    # writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    # # writer.write_cells("A1", "MAT")
    # # writer.write_cells("A2", entries[0])
    #
    # # ta_dataframe.to_excel(writer, float_format='%.2f', startrow=4, startcol=0)
    # dataframe.to_excel(writer, startrow=4, startcol=0)
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
