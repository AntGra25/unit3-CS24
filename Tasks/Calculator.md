# Calculator task

## 1. Solution

```.kv
Screen:
    size: 250, 500

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1

        MDLabel:
            id:output
            text: '0'
            size_hint: 1, 2/7
            font_size: '34pt'
            halign: 'right'
            color: 'white'
            md_bg_color: '#595857'

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 1/7

            MDRaisedButton:
                id:AC
                text: "AC"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#69696a'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:+/-
                text: "+/-"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#69696a'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:%
                text: "%"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#69696a'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:÷
                text: "÷"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#f2a43c'
                on_press:
                    app.button_pressed()

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 1/7

            MDRaisedButton:
                id:7
                text: "7"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:8
                text: "8"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:9
                text: "9"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:×
                text: "×"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#f2a43c'
                on_press:
                    app.button_pressed()

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 1/7

            MDRaisedButton:
                id:4
                text: "4"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:5
                text: "5"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:6
                text: "6"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:−
                text: "−"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#f2a43c'
                on_press:
                    app.button_pressed()

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 1/7

            MDRaisedButton:
                id:1
                text: "1"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:2
                text: "2"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:3
                text: "3"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:+
                text: "+"
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#f2a43c'
                on_press:
                    app.button_pressed()

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 1/7

            MDRaisedButton:
                id:0
                text: "0"
                size_hint: 0.5, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:.
                text: "."
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#828283'
                on_press:
                    app.button_pressed()

            MDRaisedButton:
                id:=
                text: "="
                size_hint: 0.25, 1
                font_size: '30pt'
                color: 'white'
                md_bg_color: '#f2a43c'
                on_press:
                    app.button_pressed()


```

## 2. Proof of Work

![Calculator](https://github.com/AntGra25/unit3-CS24/assets/142757981/e94a6486-7317-4111-b7d8-400ed6b2bd13)
