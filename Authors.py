from database import database
class Author:
    def add_author(self):
        print("----------------")
        print(" Add Author")
        print("----------------")
        author_name=input("Enter the author name :")
        if not author_name.strip():
            print("Author name cannot be empty.")
            return
        stmt="""
           select * from authors where author_name=%s      
            """
        sql_stmt="""
        insert into authors(author_name) 
        values (%s)
            """
        value=(author_name,)
        if database.execute_is_exist(self,stmt,value)==0:
            print("Already an author with same name exists.")
        else:
            database.execute_insertion(self,sql_stmt,value)


    def view_authors(self):
        print("----------------")
        print(" View Authors")
        print("----------------")

        dbobj = database.connect_to_db()
        dbcursor = dbobj.cursor()

        try:
            stmt = """
                SELECT author_id, author_name
                FROM authors
                ORDER BY author_id
            """

            dbcursor.execute(stmt)
            authors = dbcursor.fetchall()

            if not authors:
                print("No authors found.")
                return

            print("--------------------------------")
            print("ID\tAuthor Name")
            print("--------------------------------")

            for author in authors:
                print(f"{author[0]}\t{author[1]}")

        except Exception as e:
            print("Error...", e)

        finally:
            dbobj.close()