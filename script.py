import os
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ✅ Download & Install Chrome for Railway
os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
os.system("apt update && apt install -y ./google-chrome-stable_current_amd64.deb")

# ✅ Configure Chrome Options for Railway
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"  # ✅ Tell Selenium where Chrome is installed

# ✅ Start WebDriver with the manually installed Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://www.google.com")
print("Title:", driver.title)

time.sleep(2)
driver.quit()

EMAIL = "avinash06nitp@gmail.com"
PASSWORD = "xetr xdko hmiw lrui"  # Use an App Password, NOT your actual password
TO_EMAILS = ["avinash.singh3@phonepe.com", "avinashsinghmindhunter@gmail.com"]  # Add more TO recipients
CC_EMAILS = ["krishnakant.alcheringa@gmail.com", "avinashs.ug19.ce@nitp.ac.in","dhritisood19@gmail.com","tanushreepathak@gmail.com"] 

def send_email():
    subject = "Royal Challengers Bangalore Tickets Available!"
    body = "RCB Tickets are LIVE! Do not miss the thrill of watching the game unfold right in front of your eyes. Book your tickets now: https://shop.royalchallengers.com/ticket Secure your seats before they are gone! See you at the stadium! Cheers, Avinash"
    
    message = f"Subject: {subject}\n\n{body}"
    
    recipients = TO_EMAILS + CC_EMAILS

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, recipients, message)

    print("✅ Email sent successfully!")

def check_tickets():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/google-chrome"  # ✅ Use installed Chrome

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://shop.royalchallengers.com/ticket")
    time.sleep(5)

    try:
        buy_now_buttons = driver.find_elements(By.XPATH, "//button[normalize-space(text())='COMING']")
        if buy_now_buttons:
            print("🎟️ Buy Now button found! Sending email...")
            send_email()
        else:
            print("⏳ Buy Now button not found yet.")
    except Exception as e:
        print("❌ Error:", e)
    
    driver.quit()

if __name__ == "__main__":
    check_tickets()
