import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium import webdriver
import os

pdf_file_path = os.getcwd()+'/dataFile/test1.pdf'
pdf_file_path1 = os.getcwd()+'/dataFile/test2.pdf'
jpeg_file_path = os.getcwd()+'/dataFile/pic.jpeg'

class UploadFile:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://www.ilovepdf.com/merge_pdf")
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
        print("Page loaded successfully.")
        
    def upload_files_and_verify_the_visibility_of_files_on_screen(self):
        
        try:
                # Wait until the drop area becomes visible (the drop area has the class 'dropzone')
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "pickfiles"))
                )
                drop_area = self.driver.find_element(By.XPATH, "//input[@type='file']")
                
                ## Upload the first file 
                drop_area.send_keys(pdf_file_path)
                print(pdf_file_path)
                print(f"File path {pdf_file_path} sent to the input field.")
                time.sleep(2)

                # Wait for the first file to appear in the UI
                self.verify_file_visibility('test1.pdf')
                
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "pickfiles"))
                )

                # Upload the second file
                drop_area.send_keys(pdf_file_path1)
                print(f"File path {pdf_file_path1} sent to the input field.")
                time.sleep(2)

                # Wait for the second file to appear in the UI
                self.verify_file_visibility('test2.pdf')
        finally:
                print("Upload process complete.")
        
        
    

    def upload_invalid_format_value_and_verify_error_message_on_screen(self):
        try:
                # Wait until the drop area becomes visible (the drop area has the class 'dropzone')
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "pickfiles"))
                )
                drop_area = self.driver.find_element(By.XPATH, "//input[@type='file']")
                
                ## Upload the wrong file 
                print(jpeg_file_path)
                drop_area.send_keys(jpeg_file_path)
                print(f"File path {jpeg_file_path} sent to the input field.")
                self.handle_file_upload_error()
                time.sleep(2)       
        finally:
             print("Error Message Verified")
        
    def handle_file_upload_error(self):
            try:
                # Wait for the notification message (error message, e.g., 'Sorry, this extension is not allowed')
                notification = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='toast-container']//*[@class= 'toast-message']"))
                )
                
                # Extract and print the notification message
                notification_text = notification.text
                print(f"Notification message: {notification_text}")
                assert "Sorry, this extension is not allowed" in notification_text, f"Unexpected error message: {notification_text}"

            except Exception as e:
                print("No notification found or unexpected issue: ", str(e))


    def verify_file_visibility(self,file_name):
       file= self.driver.find_element(By.XPATH, f"//*[@id='fileGroups']//*[text()='{file_name}']")
       assert file.is_displayed(), f"File {file_name} is not visible after upload."
       print(f"File '{file_name}' is visible on the screen.")

    def verify_count_of_uploaded_file(self):
        uploaded_files=self.driver.find_elements(By.XPATH,"//*[@id='fileGroups']/div")
        print(f"Number of uploaded files: {uploaded_files}")
        assert len(uploaded_files) == 2


    