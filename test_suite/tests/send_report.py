import yagmail
import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

# Load environment variables
load_dotenv()

# Fetch credentials and email details from .env file
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
receiver_emails = os.getenv("RECEIVER_EMAILS").split(",")  # Convert CSV string to list

# Define file paths
html_file = "HTMLReportName.html"
screenshot_file = "Test_Report_Screenshot.png"

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the HTML file in the headless browser
driver.get(f"file:///{os.path.abspath(html_file)}")  # Local file path

# Wait for the page to fully load
time.sleep(3)

# Take a screenshot and save it as a PNG image
driver.save_screenshot(screenshot_file)

# Optionally, crop the image to focus on the report area (if necessary)
# image = Image.open(screenshot_file)
# cropped_image = image.crop((0, 0, 800, 600))  # Define your crop coordinates
# cropped_image.save(screenshot_file)

# Close the WebDriver
driver.quit()

# Email details
subject = "Automated Test Report for Digitree"
body = "Hello, please find the attached screenshot of the test report."

# Sending email using Outlook SMTP
yag = yagmail.SMTP(
    sender_email, 
    sender_password, 
    host="smtp.office365.com", 
    port=587,  # Port 587 for STARTTLS
    smtp_starttls=True,
    smtp_ssl=False
)

# Send the email with the screenshot attached
yag.send(
    to=receiver_emails,  # Accepts a list of email addresses
    subject=subject,
    contents=body,
    attachments=screenshot_file
)

print("Email sent successfully!")
