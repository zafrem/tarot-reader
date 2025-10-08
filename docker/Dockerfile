# Tarot Reader Docker Image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install the package
RUN pip install --no-cache-dir .

# Set the entrypoint
ENTRYPOINT ["python", "-m", "tarot_reader"]

# Default command (show help)
CMD ["--help"]
