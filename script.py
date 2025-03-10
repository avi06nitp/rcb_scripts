import time
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup WebDriver for cloud deployment
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Example usage
driver.get("https://www.google.com")
print("Title:", driver.title)

time.sleep(2)
driver.quit()

# Email Configuration
EMAIL = "avinash06nitp@gmail.com"
PASSWORD = "xetr xdko hmiw lrui"
TO_EMAIL = "avinash.singh3@phonepe.com"

def send_email():
    subject = "RCB Tickets Available!"
    body = "The Buy Now button is live! Visit https://shop.royalchallengers.com/ticket to book your tickets."
    
    message = f"Subject: {subject}\n\n{body}"
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, TO_EMAIL, message)

def check_tickets():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get("https://shop.royalchallengers.com/ticket")
    time.sleep(5)  
    
    try:
        buy_now_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'COMING SOON')]")
        if buy_now_buttons:
            print("Buy Now button found! Sending email...")
            send_email()
        else:
            print("Buy Now button not found yet.")
    except Exception as e:
        print("Error:", e)
    
    driver.quit()

# Run the script every 5 minutes
while True:
    check_tickets()
    time.sleep(60)  # Wait 5 minutes before checking again
