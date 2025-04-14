FROM python:3.11-slim

WORKDIR /app

# Sistem paketleri: ffmpeg dahil ediyoruz
RUN apt update && apt install -y ffmpeg

# Uygulama dosyaları
COPY . .

# Python bağımlılıkları
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "bot.main"]
