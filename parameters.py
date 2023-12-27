import pandas as pd
from PySide6.QtCore import QDate
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QTableWidgetItem
from sqlalchemy import create_engine, text

DB_PATH = "mongoconf"#sqite db
  # NAKONEC TO BLYAT YA SDELAL NORMALNEE
EXCEL_TEMPLATE_PATH     = 'template.xlsx'
EXCEL_HEADER_ROWS       = 9#5
MAIN_REPORT_PAGE        = 'Отчет'
WRAP_COLUMNS            = ['is_conditions_good', 'specie']
SAVE_DIR                = 'C:/AIS_KURSCACH_UI'
NAMES_TXT_PATH          = 'names.txt'
DATABASE_DRIVER_QT      = 'QSQLITE'  #unused
DATABASE_DRIVER_PANDAS  = 'sqlite'


def get_customer_for_order(order_pk):
    db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
    peka =pd.read_sql(f'''select customer_pk from orderj where pk = {order_pk} ''', db_connection).iloc[0][0]
    return pd.read_sql(f'''SELECT (name ||" ИНН: "|| INN ||" КПП: "|| KPP) AS gay FROM customer WHERE pk={peka}''', db_connection).iloc[0][0]

def get_supplier_for_order(order_pk):
    db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
    peka =pd.read_sql(f'''select supplier_pk from orderj where pk = {order_pk} ''', db_connection).iloc[0][0]
    return pd.read_sql(f'''SELECT (name ||" ИНН: "|| INN ||" КПП: "|| KPP) AS gay FROM supplier WHERE pk={peka}''', db_connection).iloc[0][0]
def refresh_customers_table_order(self):  # order choose orgaisations
    TABLE_ROW_LIMIT = 10
    db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

    data_for_table = pd.read_sql(text(f'SELECT * FROM customer'), db_connection).astype(str)
    self.customerTableWidget.setRowCount(len(data_for_table))

    for col_num in range(len(data_for_table.columns)):
        for row_num in range(len(data_for_table)):
            self.customerTableWidget.setItem(row_num, col_num,
                                             QTableWidgetItem(data_for_table.iloc[row_num, col_num]))


def refresh_suppliers_table_order(self):  # order choose orgaisations
    TABLE_ROW_LIMIT = 10
    db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

    data_for_table = pd.read_sql(text(f'SELECT * FROM supplier'), db_connection).astype(str)
    self.supplierTableWidget.setRowCount(len(data_for_table))

    for col_num in range(len(data_for_table.columns)):
        for row_num in range(len(data_for_table)):
            self.supplierTableWidget.setItem(row_num, col_num,
                                             QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
def refresh_suppliers_table(self):  # order_add_position
     # bezvremennoe reshenie
    TABLE_ROW_LIMIT = 10
    db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

    data_for_table = pd.read_sql(
        text(f'SELECT goods.pk,goods.name,unit.name AS unit FROM goods LEFT JOIN unit ON goods.unit = unit.pk'),
        db_connection).astype(str)
    self.goodsTableWidget.setRowCount(len(data_for_table))

    for col_num in range(len(data_for_table.columns)):
        for row_num in range(len(data_for_table)):
            self.goodsTableWidget.setItem(row_num, col_num,
                                          QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
def add_license_to_db(self):#license_add
  # bezvremennoe reshenie
    VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
    VetDbConnnection.setDatabaseName(DB_PATH)
    VetDbConnnection.open()
    VetTableQuery = QSqlQuery()
    vet_query_str = """INSERT INTO license (license_name, date, expiration_date, key) 
    VALUES (:license_name, :date, :expiration_date, :key)"""
    VetTableQuery.prepare(vet_query_str)
    VetTableQuery.bindValue(":license_name", self.licenseNameLineEdit.text())
    VetTableQuery.bindValue(":date", date_format(self.dateEdit.date().getDate()))
    VetTableQuery.bindValue(":expiration_date", date_format(self.expirationDateEdit.date().getDate()))
    VetTableQuery.bindValue(":key", str(self.keyTextEdit.toPlainText()))

    uspeh = VetTableQuery.exec()
    VetDbConnnection.close()
    print(self.dateEdit.date().getDate(), uspeh)
def delete_license(self):  # licenses_view  # bezvremennoe reshenie
    VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
    VetDbConnnection.setDatabaseName(DB_PATH)
    VetDbConnnection.open()
    VetTableQuery = QSqlQuery()
    vet_query_str = """DELETE FROM license WHERE pk =""" + self.licensesTableWidget.item(
        self.licensesTableWidget.currentRow(), 0).text()
    VetTableQuery.prepare(vet_query_str)

    print("vot tut nuzhno obnovlenie tablewigeta ")

    uspeh = VetTableQuery.exec()
    VetDbConnnection.close()

def refresh_license_table(self):  # license_view  # bezvremennoe reshenie
    TABLE_ROW_LIMIT = 10
    db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

    data_for_table = pd.read_sql(text(f'SELECT * FROM license'), db_connection).astype(str)
    self.licensesTableWidget.setRowCount(len(data_for_table))

    for col_num in range(len(data_for_table.columns)):
        for row_num in range(len(data_for_table)):
            self.licensesTableWidget.setItem(row_num, col_num,
                                             QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

def refresh_order_entries_table(self):  # aka positions table widget
      # bezvremennoe reshenie
    TABLE_ROW_LIMIT = 10
    db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

    data_for_table = pd.read_sql(text(
        f'SELECT pk, name, price, count, (count*price) FROM order_entry WHERE related_to_order={str(self.order_num)}'),
                                 db_connection).astype(str)
    self.positionsTableWidget.setRowCount(len(data_for_table))

    for col_num in range(len(data_for_table.columns)):
        for row_num in range(len(data_for_table)):
            self.positionsTableWidget.setItem(row_num, col_num,
                                              QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
def write_license_to_db(self): #licenses edit py
    VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
    VetDbConnnection.setDatabaseName(DB_PATH)
    VetDbConnnection.open()
    VetTableQuery = QSqlQuery()
    VetTableQuery.prepare("""
                            UPDATE license SET license_name=:license_name, date=:date, expiration_date=:expiration_date, key=:license_key WHERE pk=:pk
                              """)
    VetTableQuery.bindValue(":license_name", self.licenseNameLineEdit.text())
    VetTableQuery.bindValue(":date", date_format(self.dateEdit.date().getDate()))
    VetTableQuery.bindValue(":expiration_date", date_format(self.expirationDateEdit.date().getDate()))
    VetTableQuery.bindValue(":license_key", self.keyTextEdit.toPlainText())

    VetTableQuery.bindValue(":pk", self.pk)
    uspeh = VetTableQuery.exec()
    print("USPEH BLYAT&", uspeh, VetTableQuery.lastQuery())
    # self.mongo_write_license_to_db()
    VetDbConnnection.close()


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