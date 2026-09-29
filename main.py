import os
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

import discord

TOKEN = os.getenv("DISCORD_TOKEN")

CHANNEL_ID = 1554511725762707496

TARGET = datetime(
    2026, 11, 4, 0, 0, 0,
    tzinfo=ZoneInfo("America/Toronto")
)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bubble Bot online as {client.user}")

    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print("Could not find countdown channel.")
        return

    message = await channel.send("🫧 Bubble Bot initializing...")

    while True:
        now = datetime.now(ZoneInfo("America/Toronto"))
        remaining = TARGET - now

        if remaining.total_seconds() <= 0:
            text = (
                "# ⚔️ WARCRAFT FOREVER ⚔️\n\n"
                "# 🔥 DEPLOYMENT COMPLETE 🔥\n\n"
                "**AZEROTH AWAITS**"
            )
        else:
            total = int(remaining.total_seconds())

            days = total // 86400
            hours = (total % 86400) // 3600
            minutes = (total % 3600) // 60
            seconds = total % 60

            text = (
                "# ⚔️ WARCRAFT FOREVER ⚔️\n"
                "### DEPLOYMENT COUNTDOWN\n\n"
                f"# `{days:02d} : {hours:02d} : {minutes:02d} : {seconds:02d}`\n"
                "### DAYS ・ HOURS ・ MINUTES ・ SECONDS\n\n"
                "🫧 **BUBBLE BOT ONLINE**"
            )

        try:
            await message.edit(content=text)
        except Exception as error:
            print(error)

        await asyncio.sleep(1.1)

client.run(TOKEN)
