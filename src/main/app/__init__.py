import pathlib

from kivy.app import App
from kivy.uix.label import Label
from PIL import Image
import pytesseract

class MainApp(App):
    def build(self):

        imagePath = pathlib.Path(__file__).parent.parent / 'resources' / 'test.jpg'

        label = Label(text=pytesseract.image_to_string(Image.open(imagePath), lang='eng'),
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        return label


if __name__ == '__main__':
    app = MainApp()
    app.run()
