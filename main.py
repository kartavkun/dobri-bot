import asyncio
from twitchio.ext import commands, routines
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    print("Error: API_TOKEN not found. Please set it in your .env file.")
    exit()

initial_channels = [
    "kartav__", "ivango", "senyawei", "glebauster",
    "godroponika", "quizzzzz_", "vudek_", "pokemonyaaa", "25mosey",
    "majewskiosu", "f0rz__", "steisha_owo", "danon_osu", "skyfai_",
    "zoomqge", "lofkes_", "sandron", "kkanoyaa", "desuqe_",
    "dahujka_owo", "hober38_", "wavewyyy", "mitor0_",
    "zxbatonzx", "kartavkun"
]

dobri_link = "https://dobri.fun"

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=API_TOKEN, prefix='!', initial_channels=initial_channels)
        self.streaming_channels = set()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    @commands.command(name='dobri')
    async def dobri(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name}, Ссылки на чат в Telegram и Discord тут -> {dobri_link}')

    @commands.command(name='добри')  # Альтернативное имя для кириллицы
    async def dobri_cyrillic(self, ctx: commands.Context):
        await self.dobri(ctx)  # Вызываем основную команду

bot = Bot()
bot.run()
