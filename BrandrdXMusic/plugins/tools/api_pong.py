import time
import psutil
import requests
from pyrogram import filters
from ERAVIBES import app


@app.on_callback_query(filters.regex("api_pong"))
async def api_pong(client, query):

    start = time.time()

    # ── PING CHECK ──────────────────────────────────────────────
    try:
        requests.get("https://google.com", timeout=5)
        ping = round((time.time() - start) * 1000, 2)
        api_ping = f"{ping} ms"
    except:
        api_ping = "FAILED"

    # ── CPU / RAM ───────────────────────────────────────────────
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    # ── SERVER STATUS ───────────────────────────────────────────
    server_status = "🟢 ONLINE" if cpu < 90 else "🔴 OVERLOAD"

    text = f"""
<b>💗 ERA VIBES — SYSTEM STATUS</b>

<b>📡 API PING:</b> {api_ping}
<b>🧠 CPU USAGE:</b> {cpu}%
<b>🗄 RAM USAGE:</b> {ram}%
<b>🖥 SERVER:</b> {server_status}

<b>✔ Everything looks good!</b>
"""

    await query.answer(text, show_alert=True)