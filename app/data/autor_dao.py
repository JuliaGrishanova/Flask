from app.data.modelo.autor import Autor

class AutorDAO:

    def select_all(self,db) -> list[Autor]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM autores')
        autores_en_db = cursor.fetchall()
        autores : list[Autor]= list()
        for autor_en_db in autores_en_db:
            autores.append(Autor(autor_en_db[0], autor_en_db[1], autor_en_db[2]))

        cursor.close()
        return autores
    
    def select_uno(self,db,autor) -> Autor:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM autores where autor = %s',[autor])
        autores_en_db = cursor.fetchall()
        if (autores_en_db == []):
            return None
        autor_en_db = autores_en_db[0]        
        autor = Autor(autor_en_db[0], autor_en_db[1], autor_en_db[2])
        cursor.close()
        return autor

    def insert(self,db,autor,pais):
        cursor = db.cursor()
        sql = ("INSERT INTO autores (autor,pais) values (%s,%s) ")
        data = (autor,pais)
        cursor.execute(sql,data)
        db.commit()

    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("delete from autores where id = %s ")
        data = [id]
        cursor.execute(sql, data)
        db.commit()
        
    def update(self,db,id,autor,pais):
        cursor = db.cursor()
        sql = ("update autores set autor = %s, pais = %s where id = %s ")
        data = [autor,pais,id]
        cursor.execute(sql, data)
        db.commit()   
           
    def updateAutor(self,db,id,autor):
        cursor = db.cursor()
        sql = ("update autores set autor = %s where id = %s ")
        data = [autor,id]
        cursor.execute(sql, data)
        db.commit()           

