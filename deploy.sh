#!/bin/bash

echo "🚀 DMB Botu deploy ediliyor..."

cp .env.example .env

docker build -t dmb .
docker run -d --name dmb --env-file .env dmb
