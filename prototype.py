import cv2
from models import Camera, DetectedHuman
from calculations import depth_estimation, distance_between_objects

def read_mock_yolo_results() -> list:
    # Mock data simulating two human detections
    # Replace this with your actual bounding box values
    return [(0, [50, 100, 150, 200]), (0, [200, 100, 250, 250])]

def visualize_distance(image_path: str, human1: DetectedHuman, human2: DetectedHuman, distance: float):
    image = cv2.imread(image_path)

    # Find mid-points of the bounding boxes to annotate
    mid1 = (int((human1.bbox[0] + human1.bbox[2]) / 2), human1.bbox[3])
    mid2 = (int((human2.bbox[0] + human2.bbox[2]) / 2), human2.bbox[3])

    # Draw bounding boxes and annotate the image with the calculated distance
    cv2.rectangle(image, (human1.bbox[0], human1.bbox[1]), (human1.bbox[2], human1.bbox[3]), (0, 255, 0), 2)
    cv2.rectangle(image, (human2.bbox[0], human2.bbox[1]), (human2.bbox[2], human2.bbox[3]), (0, 255, 0), 2)
    cv2.line(image, mid1, mid2, (0, 0, 255), 2)
    cv2.putText(image, f"{distance:.2f} meters", (mid1[0] + int((mid2[0] - mid1[0]) / 2), mid1[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow('Distance Visualization', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test_version():
    cam1 = Camera()
    yolo_results = read_mock_yolo_results()

    detected_humans = [DetectedHuman(bbox) for class_idx, bbox in yolo_results if class_idx == 0]

    if len(detected_humans) < 2:
        print("Not enough detected humans to proceed.")
        return

    # Estimate depths
    depth_human1 = depth_estimation(cam1, detected_humans[0])
    depth_human2 = depth_estimation(cam1, detected_humans[1])

    # Calculate the distance between the two humans
    distance = distance_between_objects(depth_human1, depth_human2)

    # Visualize the result on the image
    visualize_distance("path_to_your_test_image.jpg", detected_humans[0], detected_humans[1], distance)

test_version()
