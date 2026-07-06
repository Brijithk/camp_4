from database import database

class Book:

    def add_book(self):
        print("----------------------")
        print(" Add Book")
        print("----------------------")

        title = input("Enter book title : ").strip()

        if not title:
            print("Book title cannot be empty.")
            return

        # Display Authors
        db = database()
        dbobj = database.connect_to_db()
        cursor = dbobj.cursor()

        cursor.execute("SELECT author_id, author_name FROM authors")
        authors = cursor.fetchall()

        if not authors:
            print("No authors found. Please add an author first.")
            dbobj.close()
            return

        print("\nAvailable Authors")
        print("-----------------")
        for author in authors:
            print(f"{author[0]}. {author[1]}")

        author_id = input("\nEnter author id : ")

        # Validate author
        stmt = """
            SELECT *
            FROM authors
            WHERE author_id = %s
        """

        if db.execute_is_exist(stmt, (author_id,)) == 1:
            print("Author does not exist.")
            dbobj.close()
            return

        # Display Categories
        cursor.execute("SELECT category_id, category_name FROM categories")
        categories = cursor.fetchall()

        if not categories:
            print("No categories found. Please add a category first.")
            dbobj.close()
            return

        print("\nAvailable Categories")
        print("--------------------")
        for category in categories:
            print(f"{category[0]}. {category[1]}")

        category_id = input("\nEnter category id : ")

        # Validate category
        stmt = """
            SELECT *
            FROM categories
            WHERE category_id = %s
        """

        if db.execute_is_exist(stmt, (category_id,)) == 1:
            print("Category does not exist.")
            dbobj.close()
            return

        # Price validation
        try:
            price = float(input("Enter price : "))
            if price <= 0:
                print("Price must be greater than 0.")
                dbobj.close()
                return
        except:
            print("Invalid price.")
            dbobj.close()
            return

        # Quantity validation
        try:
            quantity = int(input("Enter quantity : "))
            if quantity < 0:
                print("Quantity must be greater than or equal to 0.")
                dbobj.close()
                return
        except:
            print("Invalid quantity.")
            dbobj.close()
            return

        sql_stmt = """
            INSERT INTO books
            (title, author_id, category_id, price, quantity)
            VALUES (%s, %s, %s, %s, %s)
        """

        value = (
            title,
            author_id,
            category_id,
            price,
            quantity
        )

        db.execute_insertion(sql_stmt, value)

        dbobj.close()

        print("Book added successfully.")

    from database import database

    def view_books(self):
        print("---------------------------------------------------------------")
        print("ID\tTitle\t\tAuthor\t\tCategory\tPrice\tQty")
        print("---------------------------------------------------------------")

        dbobj = database.connect_to_db()
        dbcursor = dbobj.cursor()

        try:
            stmt = """
                SELECT
                    b.book_id,
                    b.title,
                    a.author_name,
                    c.category_name,
                    b.price,
                    b.quantity
                FROM books b
                JOIN authors a
                    ON b.author_id = a.author_id
                JOIN categories c
                    ON b.category_id = c.category_id
                ORDER BY b.book_id
            """

            dbcursor.execute(stmt)
            books = dbcursor.fetchall()

            if not books:
                print("No books available.")
                return

            for book in books:
                print(
                    f"{book[0]}\t"
                    f"{book[1]}\t"
                    f"{book[2]}\t"
                    f"{book[3]}\t"
                    f"{book[4]}\t"
                    f"{book[5]}"
                )

        except Exception as e:
            print("Error...", e)

        finally:
            dbobj.close()

    def search_book(self):
        print("----------------------")
        print(" Search Book")
        print("----------------------")

        try:
            book_id = int(input("Enter book id : "))
        except:
            print("Invalid book id.")
            return

        dbobj = database.connect_to_db()
        dbcursor = dbobj.cursor()

        try:
            stmt = """
                SELECT
                    b.title,
                    a.author_name,
                    c.category_name,
                    b.price,
                    b.quantity
                FROM books b
                JOIN authors a
                    ON b.author_id = a.author_id
                JOIN categories c
                    ON b.category_id = c.category_id
                WHERE b.book_id = %s
            """

            value = (book_id,)

            dbcursor.execute(stmt, value)
            book = dbcursor.fetchone()

            if not book:
                print("Book not found.")
                return

            print("\nBook Details")
            print("------------")
            print("Title     :", book[0])
            print("Author    :", book[1])
            print("Category  :", book[2])
            print("Price     :", book[3])
            print("Quantity  :", book[4])

        except Exception as e:
            print("Error...", e)

        finally:
            dbobj.close()


    def update_book(self):
        print("----------------------")
        print(" Update Book")
        print("----------------------")

        try:
            book_id = int(input("Enter book id : "))
        except:
            print("Invalid book id.")
            return

        dbobj = database.connect_to_db()
        dbcursor = dbobj.cursor()

        try:
            # Check whether the book exists
            stmt = """
                SELECT title, price, quantity, category_id
                FROM books
                WHERE book_id = %s
            """

            dbcursor.execute(stmt, (book_id,))
            book = dbcursor.fetchone()

            if not book:
                print("Book not found.")
                return

            print("\nCurrent Details")
            print("----------------")
            print("Title    :", book[0])
            print("Price    :", book[1])
            print("Quantity :", book[2])
            print("Category :", book[3])

            # Price validation
            try:
                price = float(input("\nEnter new price : "))
                if price <= 0:
                    print("Price must be greater than 0.")
                    return
            except:
                print("Invalid price.")
                return

            # Quantity validation
            try:
                quantity = int(input("Enter new quantity : "))
                if quantity < 0:
                    print("Quantity must be greater than or equal to 0.")
                    return
            except:
                print("Invalid quantity.")
                return

            # Display categories
            print("\nAvailable Categories")
            print("--------------------")

            dbcursor.execute(
                "SELECT category_id, category_name FROM categories"
            )
            categories = dbcursor.fetchall()

            if not categories:
                print("No categories found.")
                return

            for category in categories:
                print(f"{category[0]}. {category[1]}")

            try:
                category_id = int(input("\nEnter new category id : "))
            except:
                print("Invalid category id.")
                return

            # Validate category
            stmt = """
                SELECT *
                FROM categories
                WHERE category_id = %s
            """

            dbcursor.execute(stmt, (category_id,))
            if not dbcursor.fetchone():
                print("Category does not exist.")
                return

            # Update book
            stmt = """
                UPDATE books
                SET price=%s,
                    quantity=%s,
                    category_id=%s
                WHERE book_id=%s
            """

            value = (
                price,
                quantity,
                category_id,
                book_id
            )

            dbcursor.execute(stmt, value)
            dbobj.commit()

            print("Book updated successfully.")

        except Exception as e:
            print("Error...", e)
            dbobj.rollback()

        finally:
            dbobj.close()


    def delete_book(self):
        print("----------------------")
        print(" Delete Book")
        print("----------------------")

        try:
            book_id = int(input("Enter book id : "))
        except:
            print("Invalid book id.")
            return

        dbobj = database.connect_to_db()
        dbcursor = dbobj.cursor()

        try:
            # Check whether the book exists
            stmt = """
                SELECT title
                FROM books
                WHERE book_id = %s
            """

            dbcursor.execute(stmt, (book_id,))
            book = dbcursor.fetchone()

            if not book:
                print("Book not found.")
                return

            print("\nBook Title :", book[0])

            choice = input("Are you sure (Y/N)? ").strip().upper()

            if choice != 'Y':
                print("Deletion cancelled.")
                return

            # Delete book
            stmt = """
                DELETE FROM books
                WHERE book_id = %s
            """

            dbcursor.execute(stmt, (book_id,))
            dbobj.commit()

            print("Book deleted successfully.")

        except Exception as e:
            print("Error...", e)
            dbobj.rollback()

        finally:
            dbobj.close()

    def issue_book(self):
        print("----------------------")
        print(" Issue Book")
        print("----------------------")

        try:
            book_id = int(input("Enter book id : "))
        except:
            print("Invalid book id.")
            return

        dbobj = database.connect_to_db()
        dbcursor = dbobj.cursor()

        try:
            # Check whether the book exists
            stmt = """
                SELECT title, quantity
                FROM books
                WHERE book_id = %s
            """

            dbcursor.execute(stmt, (book_id,))
            book = dbcursor.fetchone()

            if not book:
                print("Book not found.")
                return

            quantity = book[1]

            # Validate quantity
            if quantity <= 0:
                print("Book is out of stock.")
                return

            remaining_quantity = quantity - 1

            # Update quantity
            stmt = """
                UPDATE books
                SET quantity = %s
                WHERE book_id = %s
            """

            value = (
                remaining_quantity,
                book_id
            )

            dbcursor.execute(stmt, value)
            dbobj.commit()

            print("Book issued successfully.")
            print("Remaining Quantity :", remaining_quantity)

        except Exception as e:
            print("Error...", e)
            dbobj.rollback()

        finally:
            dbobj.close()


    def return_book(self):
        print("----------------------")
        print(" Return Book")
        print("----------------------")

        try:
            book_id = int(input("Enter book id : "))
        except:
            print("Invalid book id.")
            return

        dbobj = database.connect_to_db()
        dbcursor = dbobj.cursor()

        try:
            # Check whether the book exists
            stmt = """
                SELECT title, quantity
                FROM books
                WHERE book_id = %s
            """

            dbcursor.execute(stmt, (book_id,))
            book = dbcursor.fetchone()

            if not book:
                print("Book not found.")
                return

            current_quantity = book[1] + 1

            # Update quantity
            stmt = """
                UPDATE books
                SET quantity = %s
                WHERE book_id = %s
            """

            value = (
                current_quantity,
                book_id
            )

            dbcursor.execute(stmt, value)
            dbobj.commit()

            print("Book returned successfully.")
            print("Current Quantity :", current_quantity)

        except Exception as e:
            print("Error...", e)
            dbobj.rollback()

        finally:
            dbobj.close()