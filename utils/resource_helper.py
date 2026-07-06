import os

class ResourceHelper:
    @staticmethod
    def upload_file(filename):
        return os.path.abspath(
            os.path.join("resources", "uploads", filename))

    @staticmethod
    def download_file(filename):
        return os.path.abspath(
            os.path.join("resources", "downloads", filename))

    @staticmethod
    def image_file(filename):
        return os.path.abspath(
            os.path.join("resources", "images", filename))
    
# Usage of the methods
'''from utils.resource_helper import ResourceHelper
file = ResourceHelper.upload_file("resume.pdf")
driver.find_element(*self.upload_button).send_keys(file)'''