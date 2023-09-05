import math
from config import VFOV, HFOV, CAMERA_HEIGHT, TILT_ANGLE, FOCAL_LENGTH, RES_X, RES_Y, HEIGHT_HUMAN, HEIGHT_FORK

class Camera:
    """ 
    Camera class representing the specifications of a camera setup.
    {arguments}
    vfov : vertical field of view [degrees]
    hfov : horizontal field of view [degrees]
    height : height of camera setup from ground [m]
    tilt_ang : vertially tilted angle [degrees]
    f_length : focal length of the lens [m]
    res_x : x component of resolution []
    res_y : y component of resolution []
    """

    def __init__(self, vfov=VFOV, hfov=HFOV, height=CAMERA_HEIGHT, tilt_ang=TILT_ANGLE, f_length=FOCAL_LENGTH, res_x=RES_X, res_y=RES_Y):
        self.f_length = f_length
        self.res_x = res_x
        self.res_y = res_y
        self.hfov = hfov
        self.vfov = vfov
        self.height = height
        self.tilt_ang = tilt_ang

    def ang_per_pixel(self) -> tuple:
        """ 
        Get (horizontal, vertical) angle per pixel in radian.
        """
        ang_per_pixel_x = (self.hfov / self.res_x) * math.pi / 180
        ang_per_pixel_y = (self.vfov / self.res_y) * math.pi / 180
        return ang_per_pixel_x, ang_per_pixel_y

class PhysicalObject:
    """ 
    Base class for objects in the scene.
    """

    def __init__(self, height: float, width=None):
        self.height = height
        self.width = width

class Human(PhysicalObject):
    """ 
    Class representing a human in the scene.
    """

    def __init__(self, height=HEIGHT_HUMAN, width=None):
        super().__init__(height, bbox)

class Forklift(PhysicalObject):
    """ 
    Class representing a forklift in the scene.
    """

    def __init__(self, height=HEIGHT_FORK, width=None):
        super().__init__(height, width)

class DetectedObject:
    def __init__(self, class_idx: int, bbox: list):
        self.class_idx = class_idx
        self.bbox = bbox
        # We can link it to a physical object if needed
        self.physical_object = None
        if class_idx == "human":
            self.physical_object = Human()
        elif class_idx == "forklift":
            self.physical_object = Forklift()
    
class DetectedHuman(DetectedObject):
    def __init__(self, bbox: list):
        super().__init__(0, bbox)
        self.real_world_height = HEIGHT_HUMAN

    # ... any specific methods or attributes for detected humans ...


class DetectedForklift(DetectedObject):
    def __init__(self, bbox: list):
        super().__init__(1, bbox)
        self.real_world_height = HEIGHT_FORKLIFT