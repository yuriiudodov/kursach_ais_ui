import pandas as pd
from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from sqlalchemy import create_engine, text

DB_PATH = "DB.sqlite3"


def add_position_to_order(self):  # add order entry

    VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
    VetDbConnnection.setDatabaseName(DB_PATH)
    VetDbConnnection.open()
    VetTableQuery = QSqlQuery()
    VetTableQuery.prepare(
        f"INSERT INTO order_entry (name, count, price, related_to_order, sum) "
        f"VALUES ('{self.goodsTableWidget.item(self.goodsTableWidget.currentRow(), 1).text()}','{str(self.countSpinBox.value())}','{self.priceLineEdit.text()}','{self.order_pk}','{self.label.text()}')"
    )
    uspeh = VetTableQuery.exec()
    VetDbConnnection.close()
def date_format(date):
    date_day=str(date[2])
    date_month = str(date[1])
    date_year=str(date[0])
    formated_date = date_day + "." + date_month + "." + date_year
    return formated_date
def just_give_doc_number():
    TABLE_ROW_LIMIT = 10
    db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

    data_for_table = pd.read_sql(text(f'SELECT * FROM orderj ORDER BY pk DESC'), db_connection).astype(str)
    return (str(data_for_table.iloc[0]['pk']))
def create_new_order():

    TABLE_ROW_LIMIT = 10
    db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

    data_for_table = pd.read_sql(text(f'SELECT * FROM orderj ORDER BY pk DESC'), db_connection).astype(str)

    VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
    VetDbConnnection.setDatabaseName(DB_PATH)
    VetDbConnnection.open() #INSERT INTO orderj (kostyl, date) VALUES
    VetTableQuery = QSqlQuery()
    VetTableQuery.prepare(f"INSERT INTO orderj (kostyl, date) VALUES ('ass','{str(date_format(QDate.currentDate().getDate()))}')")
    uspeh = VetTableQuery.exec()
    VetDbConnnection.close()
    return (str(data_for_table.iloc[0]['pk']))
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