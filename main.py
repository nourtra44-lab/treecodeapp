from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import os

class TreeCodeModifierApp(App):
    def build(self):
        self.title = "معدل الأكواد للهاتف"
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        layout.add_widget(Label(text="الصق الكود هنا:", size_hint=(1, 0.1), color=(1,1,1,1)))

        self.input_text = TextInput(text='', font_size=14, size_hint=(1, 0.4))
        layout.add_widget(self.input_text)

        btn = Button(text="تعديل الكود", size_hint=(1, 0.15), background_color=(0, 0.7, 1, 1))
        btn.bind(on_release=self.modify_code)
        layout.add_widget(btn)

        layout.add_widget(Label(text="النتيجة:", size_hint=(1, 0.1), color=(1,1,1,1)))

        self.output_text = TextInput(text='', font_size=14, size_hint=(1, 0.4), readonly=True)
        layout.add_widget(self.output_text)

        return layout

    def modify_code(self, instance):
        original_code = self.input_text.text
        if not original_code.strip():
            self.output_text.text = "الرجاء لصق كود أولاً!"
            return

        lines = original_code.split('\n')
        new_code = ""
        for line in lines:
            if 'google.colab' in line or 'files.upload()' in line:
                continue
            if 'path = ' in line and '.jpg' in line:
                line = 'path = "/storage/emulated/0/Download/image.jpg"'
            new_code += line + '\n'

        self.output_text.text = new_code

if __name__ == '__main__':
    TreeCodeModifierApp().run()