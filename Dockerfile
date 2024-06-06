FROM python:3.12.3

RUN apt update && apt install tzdata -y
ENV TZ="Europe/Rome"

# Installa le dipendenze del driver PostgreSQL
#RUN apt-get install -y libpq-dev \
#    && rm -rf /var/lib/apt/lists/*

# Imposta la directory di lavoro nel contenitore
WORKDIR /app

# Copia il file dei requisiti e installa le dipendenze
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia il codice dell'applicazione nella directory di lavoro del contenitore
COPY . .

# Comando di avvio dell'applicazione
CMD ["python", "main.py"]
