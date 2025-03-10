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

# Example usage
driver.get("https://www.google.com")
print("Title:", driver.title)

time.sleep(2)
driver.quit()

# ✅ Email Configuration (Use App Password, Not Real Password)
EMAIL = "avinash06nitp@gmail.com"
PASSWORD = "xetr xdko hmiw lrui"  # Use an App Password, NOT your actual password
TO_EMAIL = "avinash.singh3@phonepe.com"

def send_email():
    subject = "RCB Tickets Available!"
    body = "The Buy Now button is live! Visit https://shop.royalchallengers.com/ticket to book your tickets."
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, TO_EMAIL, message)
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error sending email:", e)

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
        buy_now_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'COMING SOON')]")
        if buy_now_buttons:
            print("🎟️ Buy Now button found! Sending email...")
            send_email()
        else:
            print("⏳ Buy Now button not found yet.")
    except Exception as e:
        print("❌ Error:", e)
    
    driver.quit()

# ✅ Run script once (Railway Cron Job will handle scheduling)
if __name__ == "__main__":
    check_tickets()
