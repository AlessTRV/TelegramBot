## Project Overview

This project implements a simple Telegram bot using the Pyrogram library. The bot is containerized using Docker, making it easy to deploy and run in any environment.

## Features

- **Start Command**: Greets the user with a personalized message.
- **Help Command**: Provides a list of available commands.
- **Developer Command**: Displays developer information.
- **Ping Command**: Measures and returns the bot's latency.

## Requirements

- Docker
- Docker Compose (optional)

### Environment

```env
TELEGRAM_API_ID=
TELEGRAM_API_HASH=
TELEGRAM_BOT_TOKEN=
```


## Docker Setup

### Dockerfile

The `Dockerfile` defines the environment in which the bot will run.

```dockerfile
FROM python:3.12.3

RUN apt update && apt install tzdata -y
ENV TZ="Europe/Rome"

# Imposta la directory di lavoro nel contenitore
WORKDIR /app

# Copia il file dei requisiti e installa le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'applicazione nella directory di lavoro del contenitore
COPY . .

# Comando di avvio dell'applicazione
CMD ["python", "main.py"]
