import logging
import config
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Loglama ayarları (Botun durumunu takip etmek için)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Merhaba {user.first_name}! Ben senin Telegram botunum.\n"
        "Termux üzerinde başarıyla çalışıyorum. Yardım için /yardim yazabilirsin."
    )

# /yardim komutu
async def yardim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Mevcut komutlar:\n"
        "/start - Botu başlatır\n"
        "/yardim - Bu mesajı gösterir\n"
        "/id - Telegram ID'nizi gösterir"
    )

# /id komutu
async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"Telegram ID'niz: {user_id}")

# Gelen mesajlara yanıt veren fonksiyon
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Sadece admin mesaj gönderdiğinde yanıt ver (Opsiyonel güvenlik)
    if update.effective_user.id == config.ADMIN_ID:
        await update.message.reply_text(f"Mesajını aldım: {update.message.text}")
    else:
        await update.message.reply_text("Üzgünüm, bu bot sadece sahibine yanıt verir.")

if __name__ == '__main__':
    # Botu oluşturma
    application = ApplicationBuilder().token(config.BOT_TOKEN).build()

    # Komut işleyicileri
    start_handler = CommandHandler('start', start)
    yardim_handler = CommandHandler('yardim', yardim)
    id_handler = CommandHandler('id', get_id)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    # İşleyicileri ekleme
    application.add_handler(start_handler)
    application.add_handler(yardim_handler)
    application.add_handler(id_handler)
    application.add_handler(echo_handler)

    print("Bot başlatılıyor...")
    # Botu çalıştır
    application.run_polling()
