# bot.py

import discord
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get tokens and API endpoint from env
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DJANGO_WEBHOOK_URL = os.getenv("DJANGO_WEBHOOK_URL")
API_KEY = os.getenv("DISCORD_LOG_TOKEN")

# Check environment variables
if not all([TOKEN, DJANGO_WEBHOOK_URL, API_KEY]):
    raise RuntimeError("❌ Missing environment variables.")

# Set up bot with default intents
intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

# Define allowed statuses
ALLOWED_STATUSES = ["new", "contacted", "converted", "lost"]

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

@bot.slash_command(name="lead", description="Update a lead's status (e.g., /lead 12 contacted)")
async def lead_status(ctx, lead_id: int, status: str):
    status = status.lower()
    if status not in ALLOWED_STATUSES:
        await ctx.respond(f"❌ Invalid status. Choose from: {', '.join(ALLOWED_STATUSES)}", ephemeral=True)
        return

    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"lead_id": lead_id, "status": status}

    try:
        response = requests.post(DJANGO_WEBHOOK_URL, json=payload, headers=headers, timeout=5)

        if response.status_code == 200:
            await ctx.respond(f"✅ Lead {lead_id} updated to `{status}`.")
        else:
            await ctx.respond(f"❌ Error: {response.json().get('error') or response.text}", ephemeral=True)

    except Exception as e:
        await ctx.respond(f"⚠️ Request failed: {str(e)}", ephemeral=True)

# Start bot
bot.run(TOKEN)
