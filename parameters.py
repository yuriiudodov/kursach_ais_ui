DB_PATH = "DB.sqlite3"
def date_format(date):
    date_day=str(date[2])
    date_month = str(date[1])
    date_year=str(date[0])
    formated_date = date_day + "." + date_month + "." + date_year
    return formated_date

    # def refresh_customers_table(self):
    #     DB_PATH = parameters.DB_PATH  # bezvremennoe reshenie
    #     TABLE_ROW_LIMIT = 10
    #     db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
    #
    #     data_for_table = pd.read_sql(text(f'SELECT * FROM customer'), db_connection).astype(str)
    #     self.customerTableWidget.setRowCount(len(data_for_table))
    #
    #     for col_num in range(len(data_for_table.columns)):
    #         for row_num in range(len(data_for_table)):
    #             self.customerTableWidget.setItem(row_num, col_num,
    #                                              QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    # def refresh_suppliers_table(self):
    #     DB_PATH = parameters.DB_PATH  # bezvremennoe reshenie
    #     TABLE_ROW_LIMIT = 10
    #     db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
    #
    #     data_for_table = pd.read_sql(text(f'SELECT * FROM supplier'), db_connection).astype(str)
    #     self.supplierTableWidget.setRowCount(len(data_for_table))
    #
    #     for col_num in range(len(data_for_table.columns)):
    #         for row_num in range(len(data_for_table)):
    #             self.supplierTableWidget.setItem(row_num, col_num,
    #                                              QTableWidgetItem(data_for_table.iloc[row_num, col_num]))