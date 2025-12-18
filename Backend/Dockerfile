# Use a lightweight official Python image
FROM python:3.12-slim as base

# --- Stage 1: Install Tesseract and dependencies ---
# This block handles system-level dependencies required for OCR.
FROM base as builder

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install essential build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config

# Install Tesseract OCR and its core language data (English, 'eng')
# 'libtesseract-dev' is needed to build python bindings like 'pytesseract'.
# 'tesseract-ocr' is the executable.
# 'libleptonica-dev' is a dependency for Tesseract.
RUN apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-eng \
    libtesseract-dev \
    libleptonica-dev && \
    rm -rf /var/lib/apt/lists/*

# --- Stage 2: Application Setup ---
FROM builder as final

# Create and set the working directory for the application
WORKDIR /app

# Copy the Tesseract executable and its data files from the builder stage
# This helps keep the final image as small as possible.
# Note: Since Tesseract is installed via apt-get in the 'builder' stage, 
# we rely on the final image being based on 'builder' to retain these system binaries.

# Copy Python requirements file
COPY requirements.txt .

# Install Python dependencies (e.g., pytesseract, Pillow, FastAPI/Flask)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
# Ensure your API code, e.g., 'app/' directory, 'main.py', etc., is present.
COPY ./app ./app

# Expose the port your API runs on (commonly 80 or 8000)
# Change this if your application uses a different port.
EXPOSE 5000

# Command to run your API application
# Replace 'main:app' with the entry point specific to your framework (e.g., Flask, FastAPI)
# Example for FastAPI/Uvicorn:
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]