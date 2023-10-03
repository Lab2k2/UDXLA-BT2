import os
import cv2
import uuid

class ImageController:
    def __init__(self, upload_folder):
        self.upload_folder = upload_folder
        self.create_upload_folder()

    def create_upload_folder(self):
        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)

    def upload_image(self, file):
        if file:
            file_extension = file.filename.split(".")[-1]
            unique_filename = str(uuid.uuid4()) + "." + file_extension
            image_path = os.path.join(self.upload_folder, unique_filename)
            file.save(image_path)
            return image_path

    def convert_to_gray(self, image_path):
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image_path = os.path.join(self.upload_folder, "gray_" + os.path.basename(image_path))
        cv2.imwrite(gray_image_path, gray_image)
        return gray_image
