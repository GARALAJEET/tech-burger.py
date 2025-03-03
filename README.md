# 🍔 Tech Burger

**Tech Burger** is a console-based restaurant management system written in Python, using MySQL for data storage. It allows customers to view the menu, place orders, and cancel them, while shop owners can manage menu items and view orders.

---

## 📌 Features

### 🛍️ Customer Features
- View menu
- Place an order
- View all orders
- Cancel an order

### 🏪 Shop Owner Features
- Login authentication for the owner
- View menu items
- Add new menu items
- Update menu item prices
- Delete menu items
- View all orders
- Clear all orders

---

## 🛠️ Technologies Used
- **Python** (Core application logic)
- **MySQL** (Database for menu & orders management)
- **MySQL Connector** (To interact with the database)

---

## 🏗️ Installation & Setup

### 🔹 Prerequisites
- Python installed (Version 3.x recommended)
- MySQL Server installed
- `mysql-connector-python` package installed

### 🔹 Clone the Repository
```sh
git clone https://github.com/your-username/tech-burger.git
cd tech-burger
```

### 🔹 Install Dependencies
```sh
pip install mysql-connector-python
```

### 🔹 Configure the Database
1. Open MySQL and create the database:
```sql
CREATE DATABASE techburger;
```

2. Switch to the database:
```sql
USE techburger;
```

3. Create the `menu` table:
```sql
CREATE TABLE menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL
);
```

4. Create the `orders` table:
```sql
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    quantity INT,
    total_price FLOAT,
    FOREIGN KEY (item_id) REFERENCES menu(id) ON DELETE CASCADE
);
```

### 🔹 Run the Application
```sh
python techburger.py
```

---

## 🎮 How to Use
1. **Run the program**: The welcome screen appears.
2. **Choose your role**:
   - Customers can view the menu and place orders.
   - Shop owners need to log in to manage menu items and orders.
3. **Perform actions** based on your role.
4. **Exit** when done.

---

## 🎯 Future Enhancements
✅ Add a graphical user interface (GUI) using Tkinter or Flask.  
✅ Implement payment processing.  
✅ Add user authentication for customers.  
✅ Improve order tracking with timestamps.  
---
## 📞 Contact
For queries, reach out to:
📧 Email:riopatel2020@gmail.com
🔗 GitHub:https://github.com/GARALAJEET

