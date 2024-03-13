# "The Rok" basketball application

# Criteria A: Planning

## Problem Definition
My client is passionate about creating high quality basketballs that can be customized to fit everyone’s needs. However, since he is new to the field, he still lacks the software to track money, orders, and inventory. The machine he has for making the basketballs also needs supervision. This makes it necessary to complete these tasks manually, which takes a lot of time and can lead to errors that delay delivery of the product. This has become frustrating for both my client and his customers, which is why he requires an application that solves these issues. In addition, he wants to have a login and registration system in order to keep track of his employees. He also wants the application to distinguish between his account and his employees’ accounts so that certain functions of the application cannot be accessed by those without permission.

## Success Criteria
1. The application contains a login and registration feature that uses a username and an appropriate password. [login and registration system]
2. The application will differentiate between the accounts of the owner (my client) and their employees. [distinguish between his (the owner’s) account and his employees’ accounts]
3. The application allows the owner to track money, orders, and purchases [lacks software to track money, orders, and inventory]
4. The application allows the owner to track inventory [lacks software to track money, orders, and inventory]
5. The application features access to the machine that allows the owner to produce more basketballs [machine … also needs supervision]
6. The application allows users to customize the size, color, and type of their basketball [basketballs that can be customized to fit everyone’s needs]

## Approval from the client

![SCemail](https://github.com/AntGra25/unit3-CS24/assets/142757981/f95c3f20-fc82-4d38-82f8-fdbb009fb012)

![SCapproval](https://github.com/AntGra25/unit3-CS24/assets/142757981/2169d80c-11ba-44d8-a0ed-fb27fb355c74)

## Design Statement
I will develop an application for the use of the company staff. The application will feature an interactive GUI (Graphical User Interface) and will be developed in Python and KivyMD over the period of 4 weeks. Information useful to the company and necessary for the application will be stored in an SQLite database.

# Criteria B: Design

## System Diagram
![SystemDiagram](https://github.com/AntGra25/unit3-CS24/assets/142757981/e4ac173b-99e4-4774-8934-ffd3b2e118d2)

## Wireframe Diagram
![Wireframe diagram U3](https://github.com/AntGra25/unit3-CS24/assets/142757981/7611fdfc-213a-483b-9169-1fcc0c581be4)

## ER Diagram
![ERD](https://github.com/AntGra25/unit3-CS24/assets/142757981/554aee6e-52e2-4934-b5a2-d3d261b2bdc0)

## UML Diagram
![UML](https://github.com/AntGra25/unit3-CS24/assets/142757981/dbbd4686-c325-4745-a062-ac5973ef22a5)
![UML2](https://github.com/AntGra25/unit3-CS24/assets/142757981/66f7299c-ad17-4153-af0e-1ad9b21f61a5)


## Test Plan
| Description                               | Test Type                    | Input                                                                                                                                                                                                                                                                                                            | Expected Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Login System                              | Functional: Unit test        | 1. Run the program 2. Enter the username and password  3. Click the eye icon 4. Click 'Signup' button  5. Click 'Login' button                                                                                                                                                                                   | After entering the username and password correctly, the user should be directed to the menu. They should be directed to a different menu based on their accounts. When typing in the password, there should be asterisks covering the text. The text should be uncovered by clicking the eye icon. After clicking the 'Signup' button. The user should be directed to the Registration screen.                                                                                                                                                                                                                                                                                    |
| Registration System                       | Functional: Integration test | 1. Run the program 2. Click the 'Signup' button 3. Enter the required information 4. Click the eye icons 5. Click the 'Submit' button 6. Click the 'Cancel' button                                                                                                                                               | After entering all of the information correctly  and clicking the 'Submit' button, the user should have their username and password saved to a database and be directed to the Login screen. If the user enters a set of name and email that is not registered in the database and clicks the 'Submit' button, they should be prompted to enter the information again. If the user enters a different input in the two password fields, they should be prompted to enter the information again. Clicking the eye icons should reveal the passwords, which are normally hidden by asterisks. After clicking the 'Cancel' button, the user should be directed to the Login screen.  |
| Employee Information/ Registration System | Functional: Integration test | 1. Run the program 2. Click the 'Signup' button after entering the owner's credentials 3. Click the 'Employee information/registration' button 4. Enter the name, email address and position fields and click the 'save' button 5. Click the checkboxes and click the 'remove' button 6. Click the 'back' button | The user should be able to view the information stored in the 'staff' table. The user should be able to fill out the textboxes and store this information in the 'staff' table after clicking the 'save' button. The user should be able to click the checkboxes and delete the selected rows from the 'staff' table after clicking the 'remove' button. The user should be able to go back to the menu screen after clicking the 'back' button                                                                                                                                                                                                                                   |
| Inventory System                          | Functional: Unit test        | 1. Run the program 2. Click the 'Signup' button 3. Click the 'Inventory' button 4. Click the 'back' button                                                                                                                                                                                                       | The user should be able to view the information in the 'inventory' table. After clicking the 'back' button, the user should be directed to the menu corresponding to the account that they are logged into.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Order Materials System                    | Functional: Integration test | 1. Run the program 2. Click the 'Signup' button after entering the owner's credentials 3. Click the 'Order materials' button 4. Enter the required information in the textfields or through the dropdown menus 5. Click the 'save' button 6. Click the 'back' button                                             | The user should be able to fill out which material they want to purchase and the amount they want to purchase. There should be a label showing the cost of such an order. Clicking the 'save' button should update the 'inventory' table and the 'transactions' table. Clicking the 'back' button should direct the user to the menu screen.                                                                                                                                                                                                                                                                                                                                      |
| Transaction History System                | Functional: Unit test        | 1. Run the program 2. Click the 'Signup' button after entering the owner's credentials 3. Click the 'Transaction history' button 4. Click the 'back' button                                                                                                                                                      | The user should be able to view the 'transactions' table in order of the latest transaction. After clicking the 'back' button, the user should be directed to the menu screen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Sign Out System                           | Functional: Unit test        | 1. Run the program 2. Click the 'Signup' button after entering the owner's credentials 3. Click the 'Sign out' button                                                                                                                                                                                            | The user should be taken back to the Login screen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Creating Orders System                    | Functional: Integration test | 1. Run the program 2. Click the 'Signup' button after entering an employee's credentials 3. Click the 'Place order' button 4. Fill out the dropdown menus and the textfield 5. Click the 'place' button 6. Click the 'reset' button 7. Click the 'back' button                                                   | The user should fill out the dropdown menus and the textfield. The 'customer' dropdown menu should show the names of all registered customers in the dropdown. After entering the right information and clicking the 'place' button, the information should be saved in the 'orders'  table and 'transactions' table should be updated. This should not work if the CVV entered does not correspond to the selected customer. Clicking the 'reset' button should remove all of the information already entered. Clicking the 'back' button should direct the user to the menu screen.                                                                                             |
| Fulfilling Orders System                  | Functional: Integration test | 1. Run the program 2. Click the 'Signup' button after entering an employee's credentials 3. Click the 'Orders' button 4. Click the checkboxes and click the 'fulfill' button 5. Click the 'back' button                                                                                                         | The user should be able to view the 'orders' table. After clicking some of the checkboxes the material cost of fulfilling the selected orders should be shown. After clicking the 'fulfill' button, the selected rows should be removed from the 'orders' table and the 'inventory' table should be updated. After clicking the 'back' button, the user should be directed to the menu screen.                                                                                                                                                                                                                                                                                    |
| Customer Registration System              | Functional: Integration test | 1. Run the program 2. Click the 'Signup' button after entering an employee's credentials 3. Click the 'Register customer' button 4. Fill out the textfields 5. Click the 'save' button 6. Click the 'reset' button 7. Click the 'back' button                                                                    | The user should be able to fill out the textfields and save the entered information into the 'customer' table  after clicking the 'save' button. Clicking this button should also direct the user to the menu screen. Clicking the 'reset' button should remove all of the already entered information from the textfields. Clicking the 'back' button should direct the user to the menu screen                                                                                                                                                                                                                                                                                  |

# Criteria C: Development

## List of Techniques Used
* OOP (Object Oriented Programming)
* KivyMD
* SQLite
* Functions
* If statements

## TheRok.py

### Imports
```.py
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatIconButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import OneLineListItem
from kivymd.uix.snackbar import Snackbar
from Unit3.Tasks.my_lib3 import DatabaseWorker
```

The code starts by importing several necessary libraries. The libraries related to kivymd will be used to help make the GUI and add different types of widgets to it. The 'my_lib3' library contains the 'DatabaseWorker' class which will help to access the SQLite database. This class uses the sqlte3 library in order to enable this.

### App
```.py
class TheRok(MDApp):
    db = DatabaseWorker("the_rok.db")
    def build(self):
        Window.size = (800, 600)
```

This class is a subclass of MDApp and represents the main application. In it, the connection to the database is established through the DatabaseWorker class and saved to the 'db' variable. This makes it easily accessible in the later parts of the code. The 'build' method is also used to set the window size with the help of the 'Window' class

### BaseTableScreen
```.py
class BaseTableScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []

    def on_pre_enter(self, *args):
        column_names = self.get_column_names()
        self.data_tables = MDDataTable(
            size_hint=(.8, .5),
            pos_hint={'center_x': .5, 'top': .8},
            use_pagination=False,
            check=True,
            column_data=column_names,
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def get_column_names(self):
        return []

    def row_pressed(self, table, cell):
        print(f"Values clicked {cell.text}")

    def checkbox_pressed(self, table, current_row):
        print(table, current_row)

    def update(self):
        pass
```

As I will be using tablescreens to present data throughout the whole project, I decided to create a template for them with this class. It has many placeholder methods and variables that are to be edited when creating a child class.

### Login System
```.py
class LoginScreen(MDScreen):
    def try_login(self):
        success = False
        uname = self.ids.uname.text
        upass = self.ids.upass.text
        udata = TheRok.db.search(f"SELECT * from staff where uname = '{uname}' or email = '{uname}'", multiple=True)
        if len(udata) > 0:
            udata = udata[0]
            real_uname = udata[2]
            real_email = udata[3]
            real_upass = udata[4]
            position = udata[5]
            if (real_uname == uname or real_email == uname) and real_upass == upass:
                success = True

        if success:
            self.ids.uname.text = ''
            self.ids.upass.text = ''
            if position == 'Owner':
                self.parent.current = 'Omenu'
            if position == 'Employee':
                self.parent.current = 'Cmenu'

    def toggle_password_visibility(self):
        self.ids.upass.password = not self.ids.upass.password
```


### Registration System
```.py
class RegisterScreen(MDScreen):
    def try_register(self):
        name = self.ids.n_name.text
        email = self.ids.n_email.text
        uname = self.ids.n_uname.text
        password = self.ids.n_password.text
        password_conf = self.ids.nc_password.text
        udata = TheRok.db.search(f"SELECT * from staff where name = '{name}' and email = '{email}' and password is null",
                                 multiple=True)
        if len(udata) > 0:
            if password == password_conf:
                save_query = f"UPDATE staff set uname = '{uname}', password = '{password}' where name = '{name}'"
                TheRok.db.run_query(save_query)
                self.parent.current = 'login'
            else:
                self.ids.nc_password.error = True
                self.ids.nc_password.helper_text = "Password does not match"
        else:
            Snackbar(text="No account with this name and email is registered", bg_color=(1,0,0,1)).open()

    def toggle_password_visibility(self):
        self.ids.n_password.password = not self.ids.n_password.password
        self.ids.nc_password.password = not self.ids.nc_password.password

```


### Menus
```.py
class OwnerMenu(MDScreen):
    pass


class EmployeeMenu(MDScreen):
    pass
```

### Staff Management System
```.py
class EmployeeInfo(BaseTableScreen):
    def get_column_names(self):
        return [('id', 40), ('Name', 30), ('Username', 30), ('Email', 40), ('Password', 100), ('Position', 30)]

    def update(self):
        data = TheRok.db.search(query='SELECT * from staff', multiple=True)
        self.data_tables.update_row_data(
            None, data
        )

    def save(self):
        name = self.ids.full_name.text
        email = self.ids.email.text
        position = self.ids.c_position.text
        print(name, email, position)
        save_query = f"""INSERT into staff (name, email, position)
        values('{name}', '{email}', '{position}')"""
        TheRok.db.run_query(query=save_query)
        self.update()
```

### Customer Registration System

```.py
class RegisterCustomer(MDScreen):
    def save_customer(self):
        name = self.ids.name.text
        email = self.ids.email.text
        address = self.ids.address.text
        card = self.ids.card.text
        expiration = self.ids.expiration.text
        cvv = self.ids.cvv.text

        save_query = f"""INSERT INTO customer (name, email, address, card, expiration, cvv)
                         VALUES('{name}', '{email}', '{address}', '{card}', '{expiration}', '{cvv}')"""
        TheRok.db.run_query(query=save_query)

    def reset_fields(self):
        self.ids.name.text = ''
        self.ids.email.text = ''
        self.ids.address.text = ''
        self.ids.card.text = ''
        self.ids.expiration.text = ''
        self.ids.cvv.text = ''
```


## TheRok.kv

### ScreenManager

```.kv
ScreenManager:
    LoginScreen:
        name: 'Login'
    RegisterScreen:
        name: 'Register'
    OwnerMenu:
        name: 'Omenu'
    EmployeeMenu:
        name: 'Cmenu'
    EmployeeInfo:
        name: 'EmployeeInfo'
    RegisterCustomer:
        name: 'CustomerReg'
```

### MDIconButton

```.kv
MDIconButton:
    icon: "eye-off" if root.ids.upass.password else "eye"
    on_release: root.toggle_password_visibility()
```

### MDTextField

```.kv
MDTextField:
        id: email
        hint_text: 'Email'
        pos_hint: {'center_x':.5, 'top':.7}
        size_hint_x: .8
```
