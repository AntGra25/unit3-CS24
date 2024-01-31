# Quiz041

## 1. Solution

### .py file

```.py
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton


class MyButton(MDFlatButton):
    pass


class quiz41(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        Window.size = (500, 500)
        pass

    def button_pressed(self, btn):
        self.count += 1
        if btn.text == '':
            if self.root.ids.game_header.text == "X Player's turn":
                btn.text = 'X'
                btn.md_bg_color = '#be0000'
                self.root.ids.game_header.text = "O Player's turn"
            elif self.root.ids.game_header.text == "O Player's turn":
                btn.text = 'O'
                btn.md_bg_color = '#edd79f'
                self.root.ids.game_header.text = "X Player's turn"

            if won() and btn.text != '':
                self.root.ids.game_header.text = f'{btn.text} Player won!'
            elif self.count == 9 and 'won' not in self.root.ids.game_header.text:
                self.root.ids.game_header.text = 'Tie!'

    def won(self) -> bool:
        win = False
        board = [
            [self.root.ids.btn00.text, self.root.ids.btn01.text, self.root.ids.btn02.text],
            [self.root.ids.btn10.text, self.root.ids.btn11.text, self.root.ids.btn12.text],
            [self.root.ids.btn20.text, self.root.ids.btn21.text, self.root.ids.btn22.text]
            ]

        for i in range(3):
            if all(board[i][j] == 'X' for j in range(3)) or all(board[j][i] == 'X' for j in range(3)):
                win = True
            elif all(board[i][j] == 'O' for j in range(3)) or all(board[j][i] == 'O' for j in range(3)):
                win = True
        if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2-i] == 'X' for i in range(3)):
            win = True
        elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2-i] == 'O' for i in range(3)):
            win = True

        if win:
            return True
        else:
            return False


test = quiz41()
test.run()

```

### .kv file

```.kv
Screen:
    size: 500, 500

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 0.8, 0.8
        pos_hint: {'center_x':.5, 'center_y':.5}
        md_bg_color: '#334455'

        MDLabel:
            id:game_header
            text: "X Player's turn"
            size_hint: 1, 0.25
            font_size: '24pt'
            halign: 'center'
            color: 'black'
            md_bg_color: 'white'

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.25

            MyButton:
                id:btn00
            MyButton:
                id:btn01
            MyButton:
                id:btn02

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.25

            MyButton:
                id:btn10
            MyButton:
                id:btn11
            MyButton:
                id:btn12

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.25

            MyButton:
                id:btn20
            MyButton:
                id:btn21
            MyButton:
                id:btn22


<MyButton>:
    size_hint: 1, 1
    font_size: '20pt'
    text_color: 'white'
    md_bg_color: '#81d4bc'
    on_press:
        app.button_pressed(self)

```
## 2. Proof of Work


https://github.com/AntGra25/unit3-CS24/assets/142757981/8f07aa48-cb07-424a-8cd9-ba50dc9063c2

https://github.com/AntGra25/unit3-CS24/assets/142757981/afc3df34-f69e-484a-8663-16155543cb62


## 3. UML Diagram

![Quiz041C](https://github.com/AntGra25/unit3-CS24/assets/142757981/2085d7ed-8477-4a3a-88dc-21895ec79b74)

