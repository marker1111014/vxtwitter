import logging
import re
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

# 設定日誌記錄
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# 設定
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')  # 請替換為您的 Bot Token

# 正規表達式來匹配 Twitter (X) 連結
twitter_regex = re.compile(
    r"^(https?:\/\/)?(www\.)?(x|twitter)\.com\/\S+\/status\/\d+.*$",
    re.IGNORECASE
)

async def handle_link_conversion(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """處理 Twitter/X 連結並將其轉換為 vxtwitter 連結。"""
    original_link = update.effective_message.text
    
    # 使用 re.sub 進行替換
    converted_link = re.sub(
        r"^(https?:\/\/)?(www\.)?(x|twitter)\.com",
        "https://vxtwitter.com",
        original_link,
        flags=re.IGNORECASE
    )
    
    if original_link != converted_link:
        logger.info(f"將連結轉換為: {converted_link}")
        await update.effective_message.reply_text(
            converted_link,
            reply_to_message_id=update.effective_message.message_id
        )

def main() -> None:
    """主函數，啟動機器人。"""
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # 註冊處理器，僅處理符合正規表達式的文字訊息
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(twitter_regex), handle_link_conversion))

    logger.info("機器人已啟動，正在輪詢更新...")
    application.run_polling()

if __name__ == "__main__":
    main()