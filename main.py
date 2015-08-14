from kivy.app import App
from kivy.lang import Builder
#from kivy.animation import Animation
from kivy.properties import ObjectProperty, NumericProperty

from pandaview import PandaView


class Test(App):
    model = ObjectProperty(None)
    angle = NumericProperty(0)

    def build(self):
        self.root = root = Builder.load_string('''
PandaView:
    id: view
    cam_pos: 0, -12, 1
    cam_lookat: 0, 0, .5
        ''')

        self.model = root.load_model('Kivy.egg')

        '''
        anim = Animation(
            angle=360,
            d=30
        ) + Animation(
            angle=0,
            d=0
        )
        anim.start(self)
        '''

        return root

    def on_angle(self, *args):
        self.model.setHpr(args[1], 0, 0)

Test().run()
