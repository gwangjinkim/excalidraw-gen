FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your API code
COPY api/ /app/api/

# Install Python dependencies
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    pyyaml \
    python-multipart

# Install system dependencies for node-canvas (required by excalidraw_export)
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    build-essential \
    libcairo2-dev \
    libjpeg-dev \
    libpango1.0-dev \
    libgif-dev \
    librsvg2-dev \
    nodejs \
    npm \
 && rm -rf /var/lib/apt/lists/*

# Install excalidraw_export globally via npm
RUN npm install --global excalidraw_export

# Expose FastAPI port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
