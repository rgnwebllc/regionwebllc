import discord
import requests
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DJANGO_WEBHOOK_URL = os.getenv("DJANGO_WEBHOOK_URL")
API_KEY = os.getenv("DISCORD_LOG_TOKEN")

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

@bot.slash_command(name="lead", description="Update a lead's status")
async def lead_status(ctx, lead_id: int, status: str):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"lead_id": lead_id, "status": status.lower()}

    response = requests.post(DJANGO_WEBHOOK_URL, json=payload, headers=headers)

    if response.status_code == 200:
        await ctx.respond(f"✅ Lead {lead_id} updated to `{status}`.")
    else:
        await ctx.respond(f"❌ Error: {response.json().get('error')}")

bot.run(TOKEN)
