#convert jpeg to svg resize and then convert back to jpeg
import  jpype, os
import pandas as pd
import  asposecells     
from reportlab.graphics import renderPM, renderSVG
from svglib.svglib import svg2rlg
from reportlab.lib.units import inch, cm

def scale(drawing, size_x, size_y):
    """
    Scale a reportlab.graphics.shapes.Drawing()
    object while maintaining the aspect ratio
    """
    scaling_x = size_x / drawing.width
    scaling_y = size_y / drawing.height
    drawing.width = size_x
    drawing.height = size_y
    drawing.scale(scaling_x, scaling_y)
    return drawing

os.environ['JAVA_HOME'] = r'C:\\Program Files\\Java\\jdk-19'
jpype.startJVM() 
from asposecells.api import Workbook
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.abspath(os.path.join(dir_path, os.pardir))
img_path = os.path.join( parent_path, "Dataset & Modified Datasets\\leaf-classification\\images")
img_resized_path = os.path.join( parent_path, "Dataset & Modified Datasets\\leaf-classification-jpg-resized")
img_zoom_path = os.path.join( parent_path, "Dataset & Modified Datasets\\leaf-classification-jpg-zoom")
img_svg_path = os.path.join(parent_path, "Dataset & Modified Datasets\\leaf-classification-svg")
train = pd.read_csv(os.path.join(parent_path, "Dataset & Modified Datasets\\leaf-classification\\mapping.csv"))
for i in range(len(train)):
    workbook = Workbook(os.path.join(img_path, str(train.id[i]) + ".jpg"))
    workbook.save(os.path.join(img_svg_path, "{}.svg".format(train.id[i])))
    img = svg2rlg(os.path.join(img_svg_path, "{}.svg".format(train.id[i])))
    renderPM.drawToFile(scale(img, 300, 300), os.path.join(img_resized_path,'{}.jpg'.format(train.id[i])), 'JPG')
    zoom_img = svg2rlg(os.path.join(img_svg_path, "{}.svg".format(train.id[i])))
    zoom_img.height = 300
    zoom_img.width = 300
    renderPM.drawToFile(zoom_img, os.path.join(img_zoom_path,'{}.jpg'.format(train.id[i])), 'JPG')
jpype.shutdownJVM()