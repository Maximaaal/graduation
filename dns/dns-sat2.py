import os.path
import matplotlib.image as mpimg
import numpy

IMAGE_PATH = "./yee.png"
timestamp = os.path.getmtime( IMAGE_PATH )

class UpdatedImage:
    def __init__( self, filename ):
        self.filename    = filename
        self.last_update = 0         # trigger initial load
        self.image       = None      # final surface
        self.reLoadImage()           # make sure we load once, first
    
    def drawAt( self, window, position ):
        """ Draw the image to the screen at the given position """
        window.blit( self.image, position )

    def reLoadImage( self ):
        """ Load in the image iff it has changed on disk """
        current_file_time = os.path.getmtime( self.filename )
        if ( current_file_time > self.last_update ):
            self.last_update = current_file_time
            img_crop = mpimg.imread( self.filename )

crop_image = UpdatedImage( "./yee.png" )

running = True
while running:
    screen.fill((30,30,30))

    crop_image.reLoadImage()
    crop_image.drawAt( screen, ( 850, 360 ) )