import mysql.connector


class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="hit-demo-db")
            self.mycursor = self.conn.cursor()
        except:
            print("Some error occured. Could not connect to database")

        else:
            print("Connected to Database")

    def register(self, name, email, password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name, email, password)
                                  )
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self, email, password):
        self.mycursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email, password))

        data = self.mycursor.fetchall()

        return data
