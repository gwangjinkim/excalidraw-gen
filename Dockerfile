FROM python:3.11-slim

WORKDIR /app

COPY api/ /app/api/

RUN pip install fastapi uvicorn pyyaml python-multipart

# Add Node.js and excalidraw-export to your existing Python container
# Install all system-level dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    ca-certificates \
    git \
    chromium \
    nodejs \
    npm \
    libnss3 \
    libatk1.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libxshmfence1 \
    libgbm1 \
    libx11-dev \
    libgtk-3-0 \
    libxext6 \
    fonts-liberation \
    build-essential \
    libcairo2-dev \
    libpango1.0-dev \
    libjpeg-dev \
    libgif-dev \
    librsvg2-dev \
    pkg-config 

# Install working CLI renderer
RUN npm install --global excalidraw_export

EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
