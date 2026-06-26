from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.animation import Animation
from kivy.core.window import Window

# Define las dimensiones de la pantalla para simular un celular
Window.size = (360, 640)

# Interfaz gráfica en lenguaje KV
KV = '''
ScreenManager:
    id: sm
    CalcScreen:
    HistoryScreen:

<CalcScreen>:
    name: "calc"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.1, 0.05, 0.15, 1  # Fondo morado muy oscuro
        
        # --- BARRA SUPERIOR --- 
        MDTopAppBar:
            title: "Kuromi Calculadora"
            left_action_items: [["calculator", lambda x: None]]
            right_action_items: [["history", lambda x: app.switch_to_history()]]
            elevation: 2
            md_bg_color: 0.8, 0.2, 0.6, 1  # Rosa fuerte / Magenta

        # --- ÁREA DE LA IMAGEN ANIMADA ---
        MDFloatLayout:
            size_hint_y: 0.35
            
            # Usamos AsyncImage para cargar desde el enlace de Pinterest
            AsyncImage:
                id: kuromi_img
                source: "https://i.pinimg.com/736x/e0/92/99/e092998644ad57af9f1d93bbe4332635.jpg"
                size_hint: None, None
                size: "180dp", "180dp"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                allow_stretch: True
                keep_ratio: True

        # --- PANTALLA DE RESULTADOS ---
        MDBoxLayout:
            size_hint_y: 0.15
            padding: ["20dp", "10dp"]
            md_bg_color: 0.15, 0.08, 0.2, 1  # Fondo un poco más claro que el principal
            MDLabel:
                id: display
                text: "0"
                halign: "right"
                valign: "center"
                font_style: "H3"
                theme_text_color: "Custom"
                text_color: 1, 0.7, 0.9, 1  # Texto rosa claro
                bold: True

        # --- TECLADO NUMÉRICO ---
        MDGridLayout:
            cols: 4
            spacing: "10dp"
            padding: "20dp"
            size_hint_y: 0.50

            # Fila 1
            MDFillRoundFlatButton:
                text: "AC"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.7, 0.1, 0.3, 1  # Rojo/Magenta oscuro
                on_release: app.clear_all()
            MDFillRoundFlatButton:
                text: "C"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.5, 0.1, 0.4, 1  # Morado oscuro
                on_release: app.delete_last()
            MDFillRoundFlatButton:
                text: "("
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.4, 0.1, 0.5, 1
                on_release: app.append_to_display("(")
            MDFillRoundFlatButton:
                text: ")"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.4, 0.1, 0.5, 1
                on_release: app.append_to_display(")")

            # Fila 2
            MDFillRoundFlatButton:
                text: "7"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("7")
            MDFillRoundFlatButton:
                text: "8"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("8")
            MDFillRoundFlatButton:
                text: "9"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("9")
            MDFillRoundFlatButton:
                text: "/"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.8, 0.2, 0.6, 1  # Rosa brillante para operaciones
                on_release: app.append_to_display("/")

            # Fila 3
            MDFillRoundFlatButton:
                text: "4"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("4")
            MDFillRoundFlatButton:
                text: "5"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("5")
            MDFillRoundFlatButton:
                text: "6"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("6")
            MDFillRoundFlatButton:
                text: "*"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.8, 0.2, 0.6, 1
                on_release: app.append_to_display("*")

            # Fila 4
            MDFillRoundFlatButton:
                text: "1"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("1")
            MDFillRoundFlatButton:
                text: "2"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("2")
            MDFillRoundFlatButton:
                text: "3"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("3")
            MDFillRoundFlatButton:
                text: "-"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.8, 0.2, 0.6, 1
                on_release: app.append_to_display("-")

            # Fila 5
            MDFillRoundFlatButton:
                text: "."
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display(".")
            MDFillRoundFlatButton:
                text: "0"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.3, 0.1, 0.4, 1
                on_release: app.append_to_display("0")
            MDFillRoundFlatButton:
                text: "="
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 1, 0.4, 0.7, 1  # Rosa claro intenso para el Igual
                on_release: app.calculate_result()
            MDFillRoundFlatButton:
                text: "+"
                size_hint: 1, 1
                font_size: "24sp"
                md_bg_color: 0.8, 0.2, 0.6, 1
                on_release: app.append_to_display("+")

<HistoryScreen>:
    name: "history"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.1, 0.05, 0.15, 1
        
        MDTopAppBar:
            title: "Historial Kuromi"
            left_action_items: [["arrow-left", lambda x: app.switch_to_calc()]]
            right_action_items: [["trash-can", lambda x: app.clear_history()]]
            elevation: 2
            md_bg_color: 0.8, 0.2, 0.6, 1
            
        ScrollView:
            MDList:
                id: history_list
'''

class CalcScreen(MDScreen):
    pass

class HistoryScreen(MDScreen):
    pass

class KuromiCalcApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        # Esta función arranca la animación de la imagen al abrir
        self.animar_kuromi()

    def animar_kuromi(self):
        # Obtenemos la imagen de Kuromi
        img = self.root.get_screen("calc").ids.kuromi_img
        
        # Animación de flotar (subir y bajar suavemente)
        animacion = Animation(pos_hint={"center_y": 0.55}, duration=1.5, t='in_out_sine') + \
                    Animation(pos_hint={"center_y": 0.45}, duration=1.5, t='in_out_sine')
        
        animacion.repeat = True
        animacion.start(img)

    def append_to_display(self, text):
        display = self.root.get_screen("calc").ids.display
        if display.text == "0" or display.text == "Error":
            display.text = text
        else:
            display.text += text

    def clear_all(self):
        self.root.get_screen("calc").ids.display.text = "0"

    def delete_last(self):
        display = self.root.get_screen("calc").ids.display
        if len(display.text) > 1 and display.text != "Error":
            display.text = display.text[:-1]
        else:
            display.text = "0"

    def calculate_result(self):
        display = self.root.get_screen("calc").ids.display
        expression = display.text
        try:
            # Protegemos contra evaluar vacío
            if expression.strip() == "" or expression == "0":
                return
            
            result = str(eval(expression))
            display.text = result
            self.add_to_history(f"{expression} = {result}")
        except Exception:
            display.text = "Error"

    def add_to_history(self, item_text):
        history_list = self.root.get_screen("history").ids.history_list
        # Agregamos el item con formato de color rosa claro usando código HEX
        item = OneLineListItem(text=f"[color=#ffb6c1]{item_text}[/color]") 
        history_list.add_widget(item)

    def clear_history(self):
        history_list = self.root.get_screen("history").ids.history_list
        history_list.clear_widgets()

    def switch_to_history(self):
        self.root.current = "history"
        self.root.transition.direction = "left"

    def switch_to_calc(self):
        self.root.current = "calc"
        self.root.transition.direction = "right"

if __name__ == "__main__":
    KuromiCalcApp().run()