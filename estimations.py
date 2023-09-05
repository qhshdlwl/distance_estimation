import math
from models import *
from config import *

def depth_estimation(camera: Camera , object: DetectedObject):
  return object.height / math.tan(camera.ang_per_pixel[1] * object.bbox_height_in_pixels)

def distance_estimation(camera: Camera, object1: DetectedObject, object2: DetectedObject):
  pass
