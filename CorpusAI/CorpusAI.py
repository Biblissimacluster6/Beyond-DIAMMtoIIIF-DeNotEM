import os
from imageai.Detection.Custom import CustomObjectDetection

input_folder = "MY_INPUT_FOLDER"
output_folder = "MY_OUTPUT_FOLDER"

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("PATH_TO_YOLO_MODEL")
detector.setJsonPath("PATH_TO_JSON_CONFIG")
detector.loadModel()

image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpeg', '.jpg', '.png'))]

for image_file in image_files:
    image_path = os.path.join(input_folder, image_file)
    output_imagepath = os.path.join(output_folder, os.path.splitext(image_file)[0] + ".jpeg")
    detections = detector.detectObjectsFromImage(input_image=image_path, output_image_path=output_imagepath, minimum_percentage_probability=45)

    print(f"Objets détectés dans {image_file}:")
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
