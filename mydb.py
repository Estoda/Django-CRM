# # Install Mysql on your computer
# # https://dev.mysql.com/downloads/installer/
# # pip install mysql
# # pip install mysql-connector
# # pip install mysql-connector-python


# import mysql.connector

# dataBase = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="AhmedAmin@82253",
# )

# # Prepare a cursor object
# cursorObject = dataBase.cursor()

# # Create a database
# cursorObject.execute("CREATE DATABASE CRM")

# print("All Done!")


def name_shuffler(str_):
    s = str_.find(" ")
    return str_[s + 1 :] + " " + str_[0:s]


print(name_shuffler("Ahmed Amin"))
