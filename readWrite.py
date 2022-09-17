import xlsxwriter
import xlwings as xw
import calculator


def main():
    print("readwrite main")


def write_to_excel():
    print("writeToExcel")
    # book = xw.Book()
    # sheet = book.sheets[0]
    # sheet['A1'].value = "MAT"
    #
    # sheet['D1'].value = main.ta_dataframe
    #
    # writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    # # writer.write_cells("A1", )
    # # writer.write_cells("A2", mean_annual_temp)
    # #
    # workbook = writer.book
    # # ta_dataframe.to_excel(writer, float_format='%.2f', startrow=4, startcol=0)
    # fci_dataframe.to_excel(writer, startrow=4, startcol=0)
    # writer.save()

    # workbook = xlsxwriter.Workbook('output.xlsx')
    # worksheet = workbook.add_worksheet()
    # worksheet.write_string(0, 0, "MAT")
    # workbook.close()


if __name__ == "__main__":
    main()
