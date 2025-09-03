# Twitter/X 連結轉換 Telegram Bot

這是一個簡單的 Telegram 機器人，專門用於將推特（Twitter/X）的貼文連結自動轉換為 **https://www.google.com/url?sa=E\&source=gmail\&q=vxtwitter.com** 連結，以解決部分 Telegram 客戶端無法正常預覽推文內容的問題。

## 功能

  * 當使用者傳送一個推特貼文連結時，機器人會自動回覆一個轉換後的 **vxtwitter** 連結。
  * 轉換後的連結能讓 Telegram 預覽功能正常運作，顯示貼文中的圖片或影片。

## 如何使用

### 前置作業

1.  **取得你的 Bot Token**：
      * 在 Telegram 中，與 **@BotFather** 對話。
      * 使用 `/newbot` 指令來創建一個新的機器人。
      * BotFather 會提供一個 Bot Token，例如：`1234567890:ABC-DEF1234ghIkl-7890jkl`。

### 部署

1.  **設定環境變數**：

      * 在你的部署環境中，設定一個名為 `TELEGRAM_BOT_TOKEN` 的環境變數，並將你的 Bot Token 值填入。
      * 或者，你也可以直接在 `bot.py` 檔案中，將 `TELEGRAM_BOT_TOKEN` 變數的值替換為你的 Bot Token。

2.  **執行程式**：

      * 確保你已安裝所需的 Python 函式庫，可使用 `pip install python-telegram-bot` 進行安裝。
      * 執行 `python bot.py` 來啟動機器人。

## 原始碼說明

  * `bot.py`：
      * `TELEGRAM_BOT_TOKEN`：用於儲存你的 Bot Token。
      * `twitter_regex`：一個正規表達式，用來匹配任何 `twitter.com` 或 `x.com` 的貼文連結。
      * `handle_link_conversion` 函數：這是機器人的主要處理器，它會接收到連結後，使用 `re.sub` 將 `x.com` 或 `twitter.com` 替換為 `vxtwitter.com`，然後將新連結回覆給使用者。
      * `main` 函數：設定並啟動機器人，註冊 `MessageHandler` 來處理符合 `twitter_regex` 的文字訊息。
