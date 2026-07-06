from database import database

class Category:

    def add_category(self):
        print("----------------------")
        print(" Add Category")
        print("----------------------")

        category_name = input("Enter category name : ").strip()

        # Validation
        if not category_name:
            print("Category name cannot be empty.")
            return

        # Check duplicate category
        stmt = """
            SELECT *
            FROM categories
            WHERE category_name = %s
        """

        value = (category_name,)

        if database.execute_is_exist(self, stmt, value) == 0:
            print("Duplicate category names are not allowed.")
            return

        # Insert category
        sql_stmt = """
            INSERT INTO categories(category_name)
            VALUES(%s)
        """

        database.execute_insertion(self, sql_stmt, value)
        print("Category added successfully.")

    def view_categories(self):
        dbobj=database.connect_to_db()
        dbcursor=dbobj.cursor()
        try:
            print("---------------------")
            print("View Category")
            print("---------------------")
            
            sql_stmt="""
            select * from categories
            """
            dbcursor.execute(sql_stmt)
            data=dbcursor.fetchAll()
            print("----------------------------")
            print("id\tCategory Name")
            print("-----------------------------")
            for i in data:
                print(f"{i[0]}\t{i[1]}")
        except Exception as e:
            print("Error :",e)
        finally:
            dbobj.close()

        