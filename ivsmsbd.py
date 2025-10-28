#!/usr/bin/env python3
import os, time, json, requests, threading, asyncio, html
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ======= CONFIG =======
BOT_TOKEN = "8150043265:AAG1_5sWNuRPfjBqg8i328XhSLTi3olt19c"
ADMIN_ID = 6958805951      # <-- Admin Telegram ID
CHAT_ID = -1002640997198       # <-- Group / Chat ID যেখানে SMS/OTP যাবে
DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ---------- COOKIES ----------
cookies = {
    '_ga': 'GA1.2.3683759.1761327663',
    '_fbp': 'fb.1.1761327662638.854017500414448963',
    '_gid': 'GA1.2.1292047156.1761495464',
    'cf_clearance': 'your_cf_clearance_here',
    '_gat_gtag_UA_191466370_1': '1',
    'XSRF-TOKEN': 'your_xsrf_token_here',
    'ivas_sms_session': 'your_session_here',
}

headers = {
    'authority': 'www.ivasms.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.ivasms.com/portal',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# ---------- TELEGRAM COMMANDS ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔸 IVA SMS Auto Monitor Running...")

async def update_cookies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global cookies
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Only admin can update cookies.")
        return

    text = update.message.text.replace("/cookies", "").strip()
    try:
        new_cookies = json.loads(text)
        cookies = new_cookies
        await update.message.reply_text("✅ Cookies updated successfully!")
    except Exception as e:
        await update.message.reply_text(f"❌ Invalid cookies format.\n\nError: {e}")


# ---------- OTP BLOCK BUILDER ----------
def country_flag_and_name_from_number(number):
    # সহজ version: country code থেকে flag তৈরি
    code = str(number)[:3]
    flag = "🌐"
    country = "Unknown"
    if code.startswith("+84"):
        flag = "🇻🇳"
        country = "Vietnam"
    elif code.startswith("+1"):
        flag = "🇺🇸"
        country = "USA"
    return flag, country

def build_styled_otp_block(number, sid, otp, message, timestamp, signature="@Sabbirsr347"):
    flag, country_name = country_flag_and_name_from_number(number)
    country_display = f"{flag} {country_name}" if country_name else flag
    block = (
        f"<b>🔐 OTP RECEIVED</b>\n"
        f"<pre>━━━━━━━━━━━━━━━━━━━━━</pre>\n"
        f"<b>🆔 SID     :</b> <code>{sid}</code>\n"
        f"<b>📱 Number  :</b> {country_display} <code>{number}</code>\n"
        f"<b>💬 Message :</b> <pre>{html.escape(message)}</pre>\n"
        f"<b>🔑 OTP    :</b> <code>{otp}</code>\n"
        f"<b>⏰ Time   :</b> <code>{timestamp}</code>\n"
        f"<pre>━━━━━━━━━━━━━━━━━━━━━</pre>\n"
        f"<i>🤖 Bot by {signature}</i>"
    )
    return block


# ---------- IVA SMS MONITOR ----------
def monitor_sms(app):
    print("[+] IVA SMS Monitor Started...")
    last_sms_ids = set()

    while True:
        try:
            r = requests.get("https://www.ivasms.com/portal/live/my_sms", cookies=cookies, headers=headers)
            
            if r.status_code in [401, 403] or "login" in r.text.lower():
                asyncio.run_coroutine_threadsafe(
                    app.bot.send_message(chat_id=ADMIN_ID, text="⚠️ IVA SMS cookies expired! Please update using /cookies {JSON}"),
                    app.loop,
                )
                print("[!] Cookies expired, waiting for admin update...")
                time.sleep(60)
                continue

            data = r.json()
            for sms in data.get("sms_list", []):
                sms_id = sms.get("id")
                sender = sms.get("from", "Unknown")
                number = sms.get("to", "Unknown")
                message = sms.get("message", "")
                otp = sms.get("otp", "N/A")
                created_at = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

                if sms_id not in last_sms_ids:
                    last_sms_ids.add(sms_id)
                    msg_block = build_styled_otp_block(number, sms_id, otp, message, created_at)
                    asyncio.run_coroutine_threadsafe(
                        app.bot.send_message(chat_id=CHAT_ID, text=msg_block, parse_mode="HTML"),
                        app.loop,
                    )

            time.sleep(5)

        except ValueError:
            print("[i] No new SMS at this moment...")
            time.sleep(5)
        except Exception as e:
            print(f"[x] Exception: {e}")
            time.sleep(5)


# ---------- MAIN ----------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cookies", update_cookies))

    thread = threading.Thread(target=monitor_sms, args=(app,), daemon=True)
    thread.start()

    print("[!] Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()