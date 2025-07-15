# Use official Python image
FROM python:3.13

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files (for Django)
RUN python manage.py collectstatic --noinput

# Run Gunicorn
CMD ["gunicorn", "SOLIDIFY.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=4"]
