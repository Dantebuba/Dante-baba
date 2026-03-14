#!/bin/bash

echo "Termux için hazırlıklar başlıyor..."

# Paket listesini güncelle
pkg update -y && pkg upgrade -y

# Python'u kur
pkg install python -y

# Gerekli kütüphaneleri kur
pip install -r requirements.txt

echo "Kurulum tamamlandı!"
echo "Botu çalıştırmak için: cd tg_bot && python main.py"
