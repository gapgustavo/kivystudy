from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyForm(GridLayout):
    def __init__(self, **kwargs):
        super(MyForm, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Nome:'))
        self.name_input = TextInput(multiline=False)
        self.add_widget(self.name_input)

        self.add_widget(Label(text='Telefone:'))
        self.phone_input = TextInput(multiline=False)
        self.add_widget(self.phone_input)

        self.submit_button = Button(text='Enviar')
        self.submit_button.bind(on_press=self.on_submit)
        self.add_widget(self.submit_button)

    def on_submit(self, instance):
        name = self.name_input.text
        phone = self.phone_input.text
        print(f'Nome: {name}\nTelefone: {phone}')


class MyApp(App):
    def build(self):
        return MyForm()


if __name__ == '__main__':
    MyApp().run()
