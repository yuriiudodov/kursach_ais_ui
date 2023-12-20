DB_PATH = "DB.sqlite3"
def date_format(date):
    date_day=str(date[2])
    date_month = str(date[1])
    date_year=str(date[0])
    formated_date = date_day + "." + date_month + "." + date_year
    return formated_date

