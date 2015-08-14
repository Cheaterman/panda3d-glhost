'''
Panda Wrapper
=============

Minimalist wrapper around showbase, that ensure the good initialisation of Panda
and create custom lighting.
'''

from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, \
    LightAttrib, AmbientLight, DirectionalLight, \
    Vec3, Vec4

# they are still issues when clearning the window, so don't report error
# or panda will stop working - doesn't seem necessary anymore
#loadPrcFileData('', 'gl-force-no-error 1')

# force the usage of our special GL host display
loadPrcFileData('', 'load-display glhdisplay')

# we have a possibility to do supersampling ourself
# by rendering to a bigger size, and reduce it afterwise.
# but the antialiasing could be also done in shader
#loadPrcFileData('', 'win-size 1600 1200')

# deactivate that if you want to have more output about panda internals
#loadPrcFileData('', 'gl-debug true')
#loadPrcFileData('', 'notify-level spam')
#loadPrcFileData('', 'notify-level-ShowBase debug')
#loadPrcFileData('', 'default-directnotify-level debug')

class ModelShowbase(ShowBase):
    def __init__(self):
        # we must ensure that gl is ok before starting showbase initialization
        import kivy.core.gl
        from kivy.core.window import Window
        loadPrcFileData('', 'win-size %d %d' % Window.size)
        ShowBase.__init__(self)
        #self.render.setDepthTest(False, 100)
        self.setup_lights()

    def setup_lights(self):
        ambientLight = AmbientLight('ambient')
        ambientLight.setColor( Vec4( .5, .5, .5, 1 ) )
        render.setLight(render.attachNewNode(ambientLight))

        directionalLight = DirectionalLight('directional')
        directionalLight.setDirection( Vec3( -10, 10, -25 ) )
        directionalLight.setColor( Vec4( .1, .1, .1, 1 ) )
        render.setLight(render.attachNewNode(directionalLight))

    def load_model(self, filename):
        model = self.loader.loadModel(filename)
        model.reparentTo(self.render)
        return model

    def setupMouse(*largs):
        # needed, otherwise panda will break because of glh provider that
        # doesn't include mouse support
        pass

