# DMB - Discord Müzik Botu

YouTube linki üzerinden ses çalıp Discord sesli kanallarına yayın yapan özel bot.  
Docker içinde çalışmak üzere tasarlandı.

## Kurulum
```bash
docker build -t dmb .
docker run --env-file .env dmb
```
