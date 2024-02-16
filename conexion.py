import mysql.connector


    def conexion(self):
        db = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "", database = "Ta Te Ti")
        return db
    
    def gamerone(self, user1):
        con = self.conexion()
        cursor = con.cursor()
        consul = "INSERT INTO user (nom_usu, id_tip_usu) VALUES (%s, %s)"
        cursor.execute(consul, user1)
        con.commit()
        con.close()

    def gamertwo(self, user2):
        con = self.conexion()
        cursor = con.cursor()
        consul = "INSERT INTO user (nom_usu, id_tip_usu) VALUES (%s, %s)"
        cursor.execute(consul, user2)
        con.commit()
        con.close()

    def Partida(self, gamers):
        con = self.conexion()
        cursor = con.cursor()
        consul = "INSERT INTO partida (id_user1, id_user2) VALUES (%s, %s)"
        cursor.execute(consul,gamers)
        con.commit()
        con.close()
