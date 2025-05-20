import os
import django
import discord
from discord import Bot  # ✅ Explicit import
import requests
from config.settings import getEnv

env = getEnv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # adjust if your settings path is different
django.setup()

TOKEN = env("DISCORD_BOT_TOKEN")
DJANGO_WEBHOOK_URL = env("DJANGO_WEBHOOK_URL")
API_KEY = env("DISCORD_LOG_TOKEN")

intents = discord.Intents.default()
bot = Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

@bot.slash_command(name="lead", description="Update a lead's status")
async def lead_status(ctx, lead_id: int, status: str):
    print("🔐 Sending token:", API_KEY)
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"lead_id": lead_id, "status": status.lower()}

    try:
        response = requests.post(DJANGO_WEBHOOK_URL, json=payload, headers=headers)
        if response.status_code == 200:
            await ctx.respond(f"✅ Lead {lead_id} updated to `{status}`.")
        else:
            await ctx.respond(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        await ctx.respond(f"❌ Request failed: {str(e)}")

print("🎯 Starting bot...")
bot.run(TOKEN)