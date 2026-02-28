
# # Stage 1: Build environment
# FROM python:3.12.6 AS builder

# # Set environment variables to avoid Python from writing pyc files and buffering
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set working directory
# WORKDIR /app

# # Copy only the requirements to leverage Docker cache for dependencies
# COPY requirements.txt .

# # Add an argument to specify the environment
# ARG ENVIRONMENT=local

# # Upgrade pip and install dependencies into a specific path (/install)
# RUN pip install --upgrade pip && \
#     pip install --prefix="/install" -r requirements.txt

# # Stage 2: Production environment
# FROM python:3.12.6-slim AS final

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set working directory
# WORKDIR /app

# # Copy the dependencies from the builder stage to the final stage
# COPY --from=builder /install /usr/local

# # Copy the application source code to the final stage
# COPY . /app/

# # Expose the port for the Django application
# EXPOSE 8000

# # Define the default command to run your application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Stage 1: Build environment
FROM python:3.12.6 AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Stage 2: Production runtime
FROM python:3.12.6-slim AS final

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install required shared libraries (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /usr/local /usr/local

# Copy project files
COPY . .

# Optional for production: collect static files
RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
