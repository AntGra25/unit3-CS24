# Quiz042

## 1. Solution

### .py file

```.py
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class mystery(MDApp):
    def build(self):
        Window.size = (500, 500)


class MysteryPageA(MDScreen):
    def message1(self):
        print('This is mystery page B, you pressed the button')


class MysteryPageB(MDScreen):
    def message2(self):
        print('This is mystery page A, you pressed the button')


test = mystery()
test.run()

```


### .kv file

```.kv
ScreenManager:
    MysteryPageA:
        name: 'A'
        md_bg_color: 'white'
    MysteryPageB:
        name: 'B'
        md_bg_color: 'white'


<MysteryPageA>:
    MDLabel:
        text: 'Mystery Page A'
        font_size: '30pt'
        halign: 'center'
    MDFloatingActionButton:
        icon: "pencil-outline"
        style: 'standard'
        on_press:
            root.parent.current = 'B'
            root.message1()

<MysteryPageB>:
    MDLabel:
        text: 'Mystery Page B'
        font_size: '30pt'
        halign: 'center'
    MDFloatingActionButton:
        icon: "pencil-outline"
        style: 'standard'
        on_press:
            root.parent.current = 'A'
            root.message2()

```
## 2. Proof of Work


https://github.com/AntGra25/unit3-CS24/assets/142757981/bf0cb6b7-961a-413f-9ebd-9e8ffd969a11


![Quiz042 2](https://github.com/AntGra25/unit3-CS24/assets/142757981/aff9f833-c3d1-4242-82d8-12e2fbc45596)


## 3. UML Diagram

