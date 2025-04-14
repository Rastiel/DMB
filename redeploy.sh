#!/bin/bash

echo "🔄 Kodlar GitHub'dan çekiliyor..."
git pull origin main

echo "📄 Ortam dosyası kopyalanıyor..."
cp .env.example .env

echo "🐳 Docker imajı yeniden oluşturuluyor..."
docker build -t dmb .

echo "♻️ Bot yeniden başlatılıyor..."
docker stop dmb
docker rm dmb
docker run -d --name dmb --env-file .env dmb
