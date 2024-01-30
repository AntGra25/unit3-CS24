# Quiz040

## 1. Solution

### .py file

```.py
from kivymd.app import MDApp


class quiz40(MDApp):
    def build(self):
        pass

    def button_pressed(self):
        label = self.root.ids.my_label
        btn = self.root.ids.my_btn
        if label.md_bg_color == [1, 1, 1, 1]:
            label.md_bg_color = 'black'
            label.color = 'white'
            btn.md_bg_color = 'white'
            btn.text_color = 'black'
            btn.text = 'Light mode'
        else:
            label.md_bg_color = 'white'
            label.color = 'black'
            btn.md_bg_color = 'black'
            btn.text_color = 'white'
            btn.text = 'Dark mode'


text = quiz40()
text.run()

```


### .kv file

```.kv
Screen:
    size: 500, 500

    MDLabel:
        id:my_label
        text: "Your Name"
        size_hint: 1, 1
        font_size: "64pt"
        halign: "center"
        color: "black"
        md_bg_color: "white"

    MDRaisedButton:
        id:my_btn
        text: "Dark mode"
        size_hint: 0.1, 0.05
        pos_hint: {'left': 1, 'bottom': 1}
        font_size: "10pt"
        text_color: "white"
        md_bg_color: "black"
        on_press:
            app.button_pressed()

```
## 2. Proof of Work


https://github.com/AntGra25/unit3-CS24/assets/142757981/24dcc01c-bdba-45ee-a108-42ab127228a5

