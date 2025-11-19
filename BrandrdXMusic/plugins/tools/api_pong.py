import time
import aiohttp

@app.on_callback_query(filters.regex("yt_api"))
async def yt_api_status(_, q):
    start = time.time()

    # Example API — replace with your actual YT API endpoint
    api_url = "https://yourapi.com/yt/status"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as resp:
                data = await resp.json()   # <-- if API returns JSON
    except:
        data = {"status": "DOWN"}   # fallback

    ping = round((time.time() - start) * 1000, 2)

    text = f"""
「 𝐘𝐓-𝐏𝐋𝐀𝐘 𝐀𝐏𝐈 𝐒𝐓𝐀𝐓𝐔𝐒 」

📡 **API STATUS:** `{data.get('status', 'UNKNOWN')}`
📨 **ENDPOINT:** `{api_url}`

⚡ **PING:** `{ping} ms`
⏱ **CHECKED:** `{time.strftime('%I:%M:%S %p')}`

{"🟩 EVERYTHING IS FINE" if data.get("status") == "OK" else "🟥 API DOWN"}
"""

    await q.message.edit(text, reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("OK", callback_data="close")]]
    ))