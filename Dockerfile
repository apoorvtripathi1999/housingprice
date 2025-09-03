# -----------------------------------------------------------------------------
# Stage 1: Builder
# Purpose: Install dependencies in a controlled environment. This stage will be
# discarded, leaving only the necessary artifacts for the final image.
# -----------------------------------------------------------------------------
FROM python:3.11-slim as builder

# Set environment variables to optimize Python and pip behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install build-time dependencies in a single layer and clean up afterward
# to keep this layer as small as possible.
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc g++ build-essential && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment, which isolates dependencies
RUN python -m venv /opt/venv
# Add the venv to the PATH, so commands run from it directly
ENV PATH="/opt/venv/bin:$PATH"

# Copy only the requirements file first to leverage Docker's layer caching.
# This layer will only be rebuilt if requirements.txt changes.
COPY requirements.txt .

# Install Python dependencies into the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------------------------------------------------------
# Stage 2: Production
# Purpose: Create the final, lightweight image with only the application and
# its runtime dependencies.
# -----------------------------------------------------------------------------
FROM python:3.11-slim as production

# Set environment variables for the production environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Point to the virtual environment's binaries
    PATH="/opt/venv/bin:$PATH"

# Copy the populated virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Create a dedicated, non-root user and group for the application
# Running as a non-root user is a critical security best practice.
RUN addgroup --system app && adduser --system --group app

# Set the working directory for the application
WORKDIR /app

# Copy the application source code.
# Thanks to the .dockerignore file, this will now only copy the
# necessary files (e.g., app.py, pages/, etc.)
COPY . .

# Change ownership of the application files to the new non-root user
RUN chown -R app:app /app

# Switch the context to run subsequent commands as the 'app' user
USER app

# Expose the port that Streamlit will run on
EXPOSE 8501

# Add a health check to ensure the container is running properly
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Define the command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
