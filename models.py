from config import *

# ===== Camera Class =====
class Camera:
    def __init__(self, vfov=VFOV, hfov=HFOV, height=CAMERA_HEIGHT, tilt_ang=TILT_ANGLE, f_length=FOCAL_LENGTH, res_x=RES_X, res_y=RES_Y):
        self.f_length = f_length
        self.res_x = res_x
        self.res_y = res_y
        self.hfov = hfov
        self.vfov = vfov
        self.height = height
        self.tilt_ang = tilt_ang

class Object:
    def __init__(self, height: float, bbox: list):
        self.height = height
        self.bbox = bbox
    
    def set_detected_size(self, height_in_pixels, width_in_pixels):
        self.height_in_pixels = height_in_pixels
        self.width_in_pixels = width_in_pixels

class Human(Object):
    pass  # Additional human-specific attributes/methods can be added here

class Forklift(Object):
    pass  # Additional forklift-specific attributes/methods can be added here
