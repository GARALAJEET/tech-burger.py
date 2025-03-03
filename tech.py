
import mysql.connector

class TechBurger:
    def __init__(self):
        self.owner_id = "admin"
        self.owner_password = "techburger123"
        self.db_connection = self.connect_db()

    def connect_db(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="rio2603",
                database="techburger"
            )
            return conn
        except mysql.connector.Error as e:
            print(f"❌ Database Connection Failed: {e}")
            exit()

    def display_welcome(self):
        print("\n🍔🔥 Welcome to TECH BURGER! 🔥🍔")
        print("Where taste meets technology! 😋\n")

    def get_user_role(self):
        print("Are you a...\n")
        print("1️⃣ Hungry Customer (No login needed, just order and eat! 🍟)")
        print("2️⃣ Mighty Shop Owner (Login required! 🏪)")
        print("3️⃣ Just Browsing... (Exit 🚪)")
        
        choice = input("\nEnter your choice (1/2/3): ")
        return choice

    def owner_login(self):
        print("\n🔑 Welcome, Mighty Shop Owner! Please log in.")
        user_id = input("Enter Owner ID: ")
        password = input("Enter Password: ")

        if user_id == self.owner_id and password == self.owner_password:
            print("\n✅ Access Granted! Welcome, Boss! 🏆")
            return True
        else:
            print("\n❌ Access Denied! Are you an imposter? 🤨")
            return False

    def display_menu(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT id, name, price FROM menu")
        items = cursor.fetchall()

        print("\n🍽️ MENU 🍽️")
        for item in items:
            print(f"{item[0]}. {item[1]} - ₹{item[2]}")
        return items

    def add_menu_item(self):
        name = input("\nEnter new item name: ")
        price = float(input("Enter price: "))

        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO menu (name, price) VALUES (%s, %s)", (name, price))
        self.db_connection.commit()

        print(f"\n✅ {name} added to the menu!")

    def update_menu_item(self):
        self.display_menu()
        item_id = input("\nEnter item ID to update price: ")
        new_price = float(input("Enter new price: "))

        cursor = self.db_connection.cursor()
        cursor.execute("UPDATE menu SET price = %s WHERE id = %s", (new_price, item_id))
        self.db_connection.commit()

        print("\n✅ Price Updated Successfully!")

    def delete_menu_item(self):
        self.display_menu()
        item_id = input("\nEnter item ID to delete: ")

        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM menu WHERE id = %s", (item_id,))
        self.db_connection.commit()

        print("\n✅ Item Removed from Menu!")

    def view_orders(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT orders.id, menu.name, orders.quantity, orders.total_price FROM orders "
                       "JOIN menu ON orders.item_id = menu.id")
        orders = cursor.fetchall()
        for order in orders:
                print(f"orders_ID: {order[0]}  Name:{order[1]}   quantity:{2}   total_price:{order[3]}\n")
        bill_filename = f"order.txt"
        with open(bill_filename, "w",encoding="utf-8") as bill_file:
            bill_file.write("🍔🔥 TECH BURGER orders 🔥🍔\n")
            bill_file.write("---------------------------------\n")
            for order in orders:
                bill_file.write(f"orders_ID: {order[0]}  Name:{order[1]}   quantity:{2}   total_price:{order[3]}\n")
            bill_file.write("---------------------------------\n")
        print(f"📜 All Orders  saved as {bill_filename} 📜")

    def clear_orders(self):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM orders")
        self.db_connection.commit()

        print("\n✅ All orders have been cleared!")
    def cancel_order(self):
        self.view_orders()
        order_id = input("\nEnter the Order ID to cancel: ")

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
        order = cursor.fetchone()

        if order:
            cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
            self.db_connection.commit()
            print(f"\n✅ Order ID {order_id} has been canceled successfully!")
        else:
            print("\n❌ Invalid Order ID! Please try again.")

    def order_item(self):
        self.display_menu()
        order_id = input("\nEnter the item number to order: ")
        quantity = int(input("Enter quantity: "))

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT name, price FROM menu WHERE id = %s", (order_id,))
        item = cursor.fetchone()

        if item:
            total_price = item[1] * quantity
            print(f"\n🛒 Ordered: {item[0]} (x{quantity}) - Total: ₹{total_price}")

            cursor.execute("INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)",
                           (order_id, quantity, total_price))
            self.db_connection.commit()
            bill_filename = f"Bill.txt"
            with open(bill_filename, "w",encoding="utf-8") as bill_file:
                bill_file.write("🍔🔥 TECH BURGER BILL 🔥🍔\n")
                bill_file.write("---------------------------------\n")
                bill_file.write(f"Item: {item[0]}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Total Price: ₹{total_price}\n")
                bill_file.write("---------------------------------\n")
                bill_file.write("Thank you for ordering from Tech Burger!\n")
            print(f"📄 Bill saved as {bill_filename}")

            print("\n✅ Order Placed Successfully!\n")
        else:
            print("\n❌ Invalid Item! Try again.")
            
   

    def start(self):
        self.display_welcome()
        while True:
            choice = self.get_user_role()

            if choice == "1":
                while True:
                    print("\n1️⃣ View Menu")
                    print("2️⃣ Place Order")
                    print("3️⃣ View Orders")
                    print("4️⃣ Cancel Order")
                    print("5️⃣ Exit")

                    customer_choice = input("\nEnter your choice: ")

                    if customer_choice == "1":
                        self.display_menu()
                    elif customer_choice == "2":
                        self.order_item()
                    elif customer_choice == "3":
                        self.view_orders()
                    elif customer_choice == "4":
                        self.cancel_order()
                    elif customer_choice == "5":
                        print("\n👋 Thank you for visiting Tech Burger! 🍔")
                        break
                    else:
                        print("\n❌ Invalid Choice! Try again.")

            elif choice == "2":
                if self.owner_login():
                    while True:
                        print("\n🔹 Owner Menu 🔹")
                        print("1️⃣ View Menu")
                        print("2️⃣ Add New Item")
                        print("3️⃣ Update Item Price")
                        print("4️⃣ Delete Item")
                        print("5️⃣ View Orders")
                        print("6️⃣ Clear Orders")
                        print("7️⃣ Exit Owner Panel")

                        owner_choice = input("\nEnter your choice: ")

                        if owner_choice == "1":
                            self.display_menu()
                        elif owner_choice == "2":
                            self.add_menu_item()
                        elif owner_choice == "3":
                            self.update_menu_item()
                        elif owner_choice == "4":
                            self.delete_menu_item()
                        elif owner_choice == "5":
                            self.view_orders()
                        elif owner_choice == "6":
                            self.clear_orders()
                        elif owner_choice == "7":
                            print("\n🔒 Exiting Owner Panel... Back to main menu.")
                            break
                        else:
                            print("\n❌ Invalid Choice! Try again.")

            elif choice == "3":
                print("\n🚪 Exiting... Come back when you're hungry! 🍟👋")
                break
            else:
                print("\n❌ Invalid choice! Try again!\n")

# Run the app
if __name__ == "__main__":
    app = TechBurger()
    app.start()

