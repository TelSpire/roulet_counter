import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CounterWidget(BoxLayout):
    def __init__(self, orientation='vertical', **kwargs): # Добавили параметр orientation
        super().__init__(**kwargs)
        self.orientation = orientation # Используем переданную ориентацию
        self.count = 0
        self.label = Label(text=str(self.count))
        self.add_widget(self.label)

        self.increment_button = Button(text='+')
        self.increment_button.bind(on_press=self.increment)
        self.add_widget(self.increment_button)

        self.decrement_button = Button(text='-')
        self.decrement_button.bind(on_press=self.decrement)
        self.add_widget(self.decrement_button)

        self.reset_button = Button(text='Reset')
        self.reset_button.bind(on_press=self.reset)
        self.add_widget(self.reset_button)

    def increment(self, instance):
        self.count += 1
        self.label.text = str(self.count)

    def decrement(self, instance):
        self.count -= 1
        self.label.text = str(self.count)

    def reset(self, instance):
        self.count = 0
        self.label.text = str(self.count)


class MyApp(App):
    def build(self):
        main_layout = GridLayout(cols=2, rows=2, col_default_width=200)
        counter1 = CounterWidget(orientation='horizontal') # Горизонтальная ориентация для верхнего счетчика
        counter2 = CounterWidget()
        counter3 = CounterWidget()

        main_layout.add_widget(counter1)
        main_layout.add_widget(Label(size_hint_x=1))
        main_layout.add_widget(counter3)
        main_layout.add_widget(counter2)

        return main_layout


if __name__ == '__main__':
    MyApp().run()