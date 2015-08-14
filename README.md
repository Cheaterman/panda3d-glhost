# panda3d-glhost
Panda3D GLHost patch allows Panda3D to run inside another GL toolkit.
Example usage:

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from pandaview import PandaView


class Test(App):
    def build(self):
        self.root = root = Builder.load_string('''
PandaView:
    id: view
    cam_pos: 0, -12, 1
    cam_lookat: 0, 0, .5
        ''')

        root.load_model('Kivy.egg')

        return root

Test().run()
