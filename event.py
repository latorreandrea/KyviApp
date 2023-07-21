from kivy.app import App
from kivy.uix.button import Button

# class MainApp(App):
#     def build(self):
#         button = Button(
#                         text='Hello from Kivy',
#                         size_hint = (.5,.5),
#                         pos_hint={'center_x': .5, 'center_y': .5}
#                     )
#         button.bind(on_press=self.on_press_button)
#         return button
    
#     def on_press_button(self, instance):
#         print('bravo lo hai premuto!')

class ButtonApp(App):
    # def build(self):
    #     return Button()
    
    # def on_press_button(self):
    #     print('hai passato il bottone')
    def build(self):
        return Button()

    def on_press_button(self):
        print('You pressed the button!')

if __name__ == '__main__':
    # app = MainApp()
    # app.run()
    app = ButtonApp()
    app.run()