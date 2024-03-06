from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from Unit3.Tasks.my_lib3 import DatabaseWorker, make_hash

db_name = "the_rok.db"
db = DatabaseWorker(name=db_name)

# query = """CREATE TABLE if NOT EXISTS staff(
#         id integer primary key,
#         name text not null,
#         email text not null,
#         password text not null,
#         position text not null)"""
#
# db.run_query(query)

print(db.search('SELECT * from staff', multiple=True))


class TheRok(MDApp):
    db = DatabaseWorker("the_rok.db")
    def build(self):
        Window.size = (800, 600)
        pass


class LoginScreen(MDScreen):
    def try_login(self):
        success = False
        uname = self.ids.uname.text
        upass = self.ids.upass.text
        udata = db.search(f"SELECT * from staff where uname = '{uname}' or email = '{uname}'", multiple=True)[0]
        if len(udata) > 0:
            real_uname = udata[2]
            real_email = udata[3]
            real_upass = udata[4]
            position = udata[5]
            if (real_uname == uname or real_email == uname) and real_upass == upass:
                success = True

        if success:
            if position == 'Owner':
                self.parent.current = 'Omenu'
            if position == 'Employee':
                self.parent.current = 'Cmenu'


class OwnerMenu(MDScreen):

    def button_pressed(self):
        pass


class CustomerServiceMenu(MDScreen):
    pass


class RegisterScreen(MDScreen):
    pass


class EmployeeInfo(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []

    def on_pre_enter(self, *args):
        column_names = [('id',40), ('Name',30), ('Username',30), ('Email',40), ('Password',100), ('Position', 30)]

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

    def update(self):
        data = TheRok.db.search(query='SELECT * from staff', multiple=True)
        self.data_tables.update_row_data(
            None, data
        )

    def row_pressed(self, table, cell):
        print(f"Values clicked {cell.text}")

    def checkbox_pressed(self, table, current_row):
        print(table, current_row)

    def save(self):
        name = self.ids.full_name.text
        email = self.ids.email.text
        position = self.ids.c_position.text
        print(name, email, position)
        save_query = f"""INSERT into staff (name, email, position)
        values({name}, {email}, {position}"""
        TheRok.db.run_query(query=save_query)
        self.update()


class RegisterCustomer(MDScreen):
    pass


class EmployeeInventory(MDScreen):
    pass


class OwnerInventory(MDScreen):
    pass


class OrderHistory(MDScreen):
    pass


class BackButton(MDRectangleFlatIconButton):
    pass


t = TheRok()
t.run()
