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
TO_EMAILS = ["avinash.singh3@phonepe.com", "avinashsinghmindhunter@gmail.com"]  # Add more TO recipients
CC_EMAILS = ["krishnakant.alcheringa@gmail.com", "avinashs.ug19.ce@nitp.ac.in"] 

def send_email():
    subject = "Royal Challengers Bengaluru IPL Tickets Available!"
    
    body = """\
    <html>
    <head>
        <title>RCB Tickets Available!</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
            <h2 style="color: #e31837; text-align: center;">🔥 RCB Tickets Available – Grab Yours Now! 🎟️</h2>
            
            <p>Hey <strong>Cricket Fan,</strong></p>

            <p>Big news! <strong>RCB tickets are LIVE! 🎉</strong> Don’t miss the electrifying experience of watching the game live in the stadium.</p>

            <p style="text-align: center; font-size: 18px;">
                👉 <a href="https://shop.royalchallengers.com/ticket" target="_blank" style="color: #e31837; text-decoration: none; font-weight: bold;">
                    Book Your Tickets Now!
                </a>
            </p>

            <p style="text-align: center;">Hurry! seats are filling fast. Thank me later 😉</p>

            <p>Cheers,</p>
            <p><strong>Avinash Singh</strong></p>
        </div>
    </body>
    </html>
    """

    message = f"Subject: {subject}\nMIME-Version: 1.0\nContent-Type: text/html\n\n{body}"
    recipients = TO_EMAILS + CC_EMAILS
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, recipients, message)
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
        buy_now_buttons = driver.find_elements(By.XPATH, "//button[contains(translate(text(), 'BUY NOWTICKETS', 'buy nowtickets'), 'buy')]")
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
