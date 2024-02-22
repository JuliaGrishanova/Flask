from app.data.modelo.libro import Libro
from app.data.modelo.autor import Autor



class LibroBIB:

    def select_all(self,db) -> list[Libro]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM libros')
        libros_en_db = cursor.fetchall()
        libros : list[Libro]= list()
        for libro_en_db in libros_en_db:
            libros.append(Libro(libro_en_db[0], libro_en_db[1], libro_en_db[2], libro_en_db[3]))

        cursor.close()
        return libros

    def select_id_autor(self, db,autor) -> Autor:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM autores WHERE autor = %s', [autor])
        autores_en_db = cursor.fetchall()
        if (autores_en_db == []):
            return None
        autor_en_db = autores_en_db[0]        
        autor = Autor(autor_en_db[0], autor_en_db[1], autor_en_db[2],autor_en_db[3])
        cursor.close()
        return autor




    def insert(self,db,titulo,genero,id_autor):
        cursor = db.cursor()
        sql = ("INSERT INTO libros (titulo,genero,id_autor) values (%s,%s,%s) ")
        data = (titulo,genero,id_autor)
        cursor.execute(sql,data)
        db.commit()

    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("delete from libros where id = %s ")
        data = [id]
        cursor.execute(sql, data)
        db.commit()
        
    def update(self,db,id,titulo,genero):
        cursor = db.cursor()
        sql = ("update libros set titulo = %s, genero = %s where id = %s ")
        data = [titulo,genero,id]
        cursor.execute(sql, data)
        db.commit()   
           
