FROM python:3.11-slim

WORKDIR /app
LABEL authors="Carlos Viveros"
# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar tu aplicación
COPY . .

CMD ["python", "main.py"]
