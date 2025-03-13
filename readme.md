# Docker Setup Guide

## 1. Build Docker Containers

```bash
# Build the Docker containers
docker-compose build
```

## 2. Start Docker Containers

```bash
# Start the Docker containers
docker-compose up -d
```

## 3. Install Llama Model in Ollama Container

```bash
# Access the Ollama container
docker exec -it ollama bash

# Pull and run the Llama model
ollama pull llama3:3b
ollama run llama3:3b
```

## 4. Run the Chainlit App

Once the Llama model is running, you can access the Chainlit app.

Open your browser and go to:

[http://localhost:8000](http://localhost:8000)

Enjoy building with Chainlit and Llama! 🚀

