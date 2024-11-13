import pytest
from object.ilovepdf_details_object import UploadFile

from selenium import webdriver




@pytest.mark.usefixtures("driver") 
class TestFileUpload:

    def test_upload_valid_files_and_verify_count(self, driver):
        #Initialize the UploadFile class with the driver 
        upload = UploadFile(driver)
        upload.navigate()  # Navigate to the page
        upload.upload_files_and_verify_the_visibility_of_files_on_screen()
        upload.verify_count_of_uploaded_file()

    def test_upload_invalid_file_and_verify_error(self, driver):
        upload = UploadFile(driver)
        upload.navigate()  # Navigate to the page
        upload.upload_invalid_format_value_and_verify_error_message_on_screen()

    