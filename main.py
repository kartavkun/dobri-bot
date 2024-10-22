from twitchio.ext import commands, routines
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    print("Error: API_TOKEN not found. Please set it in your .env file.")
    exit()

initial_channels = ["kartav__", "ivango", "senyawei", "v1llix_", "glebauster", "godroponika", "quizzzzz_", "vudek_", "pokemonyaaa", "25mosey", "mjewskiosu", "f0rz__", "steisha_owo", "sor0k4", "skyfai_", "zoomqge", "lofkes_", "sandron", "kkanoyaa", "desuqe_", "dahujka_owo", "hober38_", "modlessflash", "wavewyyy", "zxbatonzx"]

tg_chat = "https://t.me/+55sAWAXVXPQ2ZDY6"
discord_server = "https://discord.gg/CGz59AAGrU"

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=API_TOKEN, prefix='!', initial_channels=initial_channels)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User ID is | {self.user_id}')
        self.send_links.start()  # Запускаем рутину при готовности бота

    @routines.routine(minutes=15, iterations=0)  # Бесконечные итерации
    async def send_links(self):
        for channel in initial_channels:
            try:
                twitch_channel = self.get_channel(channel)
                if twitch_channel:
                    await twitch_channel.send(f'Вступай в чат DOBRI в ТГ - {tg_chat} и на Дискорд сервер - {discord_server}')
            except Exception:
                pass  # Игнорируем ошибки

    @commands.command(name='dobri')
    async def dobri(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name}, Чат в ТГ - {tg_chat} и Дискорд сервер - {discord_server}')

    @commands.command(name='добри')  # Альтернативное имя для кириллицы
    async def dobri_cyrillic(self, ctx: commands.Context):
        await self.dobri(ctx)  # Вызываем основную команду

bot = Bot()
bot.run()
