# Use a lightweight base image with Python
FROM python:3.12-slim

# Install dependencies and Google Chrome manually
RUN apt update && apt install -y curl unzip \
    && curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb \
    && apt install -y ./chrome.deb \
    && rm chrome.deb

# Set Chrome binary path for Selenium
ENV GOOGLE_CHROME_BIN=/usr/bin/google-chrome

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY script.py /app/script.py
WORKDIR /app

# Run the script
CMD ["python", "script.py"]
