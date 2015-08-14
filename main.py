from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty

from pandaview import PandaView

# AFTER ShowBase! Don't ask me why!
from kivy.animation import Animation


class Test(App):
    model = ObjectProperty(None)
    angle = NumericProperty(0)

    def build(self):
        self.root = root = Builder.load_string('''
PandaView:
    cam_pos: 0, -8, .5
        ''')

        self.model = root.load_model('Kivy.egg')

        root.msb.setBackgroundColor(0, 0, 0, 0)

        anim = Animation(
            angle=359,
            d=3
        ) + Animation(
            angle=0,
            d=0
        )
        anim.repeat = True
        anim.start(self)

        return root

    def on_angle(self, *args):
        self.model.setHpr(args[1], 0, 0)

Test().run()
