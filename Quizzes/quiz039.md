# Quiz039

## 1. Solution

### .py file

```.py
from kivymd.app import MDApp


class my_first_app(MDApp):
    def build(self):
        self.count = 0
        return

    def button_pressed(self):
        label = self.root.ids.my_label
        self.count += 1
        label.text = f"Count {self.count}"
        label.color = "red"


text = my_first_app()
text.run()
```

### .kv file
```.kv
Screen:
    size: 500, 500


    MDBoxLayout:
        id:my_layout
        orientation: "horizontal"
        size_hint: .7, .3
        pos_hint: {"center_x":.5, "center_y":.5}

        MDLabel:
            id:my_label
            text: "Count 0"
            size_hint: 0.5, 1
            font_size: "34pt"
            halign: "center"
            color: "red"
            md_bg_color: "#ADD8E6"

        MDRaisedButton:
            id:my_btn
            text: "Add +1"
            size_hint: 0.5, 1
            font_size: "34pt"
            color: "white"
            md_bg_color: "black"
            on_press:
                app.button_pressed()
```
## 2. Proof of Work

https://github.com/AntGra25/unit3-CS24/assets/142757981/41367ebe-28a7-4783-b8e2-b861b8aac7a1


## 3. UML Diagram

