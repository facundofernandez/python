import os
from PIL import Image, ImageFilter

dir_img = "imagenes"
dir_new = os.path.join( "imagenes","imagen_new.jpg")

# im = Image.open(dir_img)
# im.filter(ImageFilter.GaussianBlur(2)).save( dir_new )



def create_thumbnail(size):
    if not os.path.exists( os.path.join(dir_img,str(size)) ):
        os.mkdir( os.path.join(dir_img,str(size)) )
    for f in os.listdir( dir_img ):
        if f.endswith(".jpg"):
            i = Image.open(os.path.join(dir_img,f))
            fn, fext = os.path.splitext(f)

            i.thumbnail( (size,size) )
            i.save(os.path.join(dir_img,"{}/{}_{}{}".format(size,fn, size,fext)))




create_thumbnail(200)