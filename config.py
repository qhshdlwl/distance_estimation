# ========= Camera Configuration =========

# Focal length of the camera in meters
FOCAL_LENGTH = 0.004

# Resolution of the camera
RESOLUTION = {
    'x': 1920,  # width in pixels
    'y': 1080   # height in pixels
}

# Field of view of the camera in degrees
FOV = {
    'horizontal': 79,
    'vertical': 43
}

# Height of the camera from the ground in meters
CAMERA_HEIGHT = 1.5

# Tilt angle of the camera in degrees
TILT_ANGLE = 10

# ========= Default Object Heights =========

# Default heights for objects in meters
DEFAULT_OBJECT_HEIGHTS = {
    'person': 1.7,
    'car': 1.5,
    'bike': 1.0
}

# ========= YOLOv5 Configuration =========

# Path to the pre-trained YOLOv5 model weights
YOLO_MODEL_PATH = "path/to/yolov5/model.weights"

# Path to the YOLOv5 configuration file
YOLO_CONFIG_PATH = "path/to/yolov5/config.cfg"

# Confidence threshold for object detection
CONFIDENCE_THRESHOLD = 0.5

# ========= Visualization Configuration =========

# Whether to show bounding boxes on detected objects
SHOW_BOUNDING_BOXES = True

# Whether to display calculated distances on the image
SHOW_DISTANCES = True

# Whether to save the annotated image
SAVE_ANNOTATED_IMAGE = True

# Directory where annotated images will be saved
OUTPUT_DIRECTORY = "path/to/save/annotated/images"
