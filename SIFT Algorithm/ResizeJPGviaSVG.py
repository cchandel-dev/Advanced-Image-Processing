#convert jpeg to svg resize and then convert back to jpeg
import  jpype, os
import pandas as pd
import  asposecells     
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg
os.environ['JAVA_HOME'] = r'C:\\Program Files\\Java\\jdk-19'
jpype.startJVM() 
from asposecells.api import Workbook
img_path = os.path.join( os.path.dirname(__file__), "leaf-classification\\images")
img_resized_path = os.path.join( os.path.dirname(__file__), "leaf-classification-jpg-resized")
train = pd.read_csv(os.path.join( os.path.dirname(__file__), "leaf-classification\\mapping.csv"))
for i in range(len(train)):
    workbook = Workbook(os.path.join(img_path, str(train.id[i]) + ".jpg"))
    workbook.save(os.path.join(os.path.dirname(__file__), "leaf-classification-svg", "{}.svg".format(train.id[i])))
    img = svg2rlg(os.path.join(os.path.dirname(__file__), "leaf-classification-svg", "{}.svg".format(train.id[i])))
    img.width = 300
    img.height = 300
    renderPM.drawToFile(img, os.path.join(img_resized_path,'{}.jpg'.format(train.id[i])), 'JPG')
jpype.shutdownJVM()