import time
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Email Configuration (DO NOT use personal password)
EMAIL = "avinash06nitp@gmail.com"
PASSWORD = "xetr xdko hmiw lrui"  # Use an App Password, NOT your real password
TO_EMAIL = "avinash.singh3@phonepe.com"

# Function to send an email
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

# Function to check ticket availability
def check_tickets():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode for cloud
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://shop.royalchallengers.com/ticket")
    time.sleep(5)  # Give some time to load the page

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

# Run script once (for Railway deployment)
if __name__ == "__main__":
    check_tickets()

