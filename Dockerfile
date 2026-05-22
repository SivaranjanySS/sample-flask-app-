# Stage 1: Builder
# Use a Python slim image for a smaller base and faster builds.
FROM python:3.10-slim-buster AS builder

# Set the working directory in the container
WORKDIR /app

# Set up a virtual environment to encapsulate dependencies
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install production dependencies
# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runner
# Use the same slim Python image for consistency and minimal size
FROM python:3.10-slim-buster AS runner

# Set the working directory
WORKDIR /app

# Copy the virtual environment from the builder stage
ENV VIRTUAL_ENV=/opt/venv
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the application code
COPY . .

# Expose the port the application runs on
EXPOSE 5000

# Create a non-root user and switch to it for security best practices
RUN adduser --system --no-create-home appuser
USER appuser

# Command to run the application using Gunicorn
# This assumes your Flask application instance is named 'app'
# and is defined in 'app.py' at the root of your project (e.g., `app.py:app`).
# Adjust 'app:app' if your entry point or Flask app variable differs (e.g., 'wsgi:app').
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]