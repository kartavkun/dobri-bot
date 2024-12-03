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
    "kartav__", "ivango", "senyawei", "v1llix_", "glebauster",
    "godroponika", "quizzzzz_", "vudek_", "pokemonyaaa", "25mosey",
    "majewskiosu", "f0rz__", "steisha_owo", "sor0k4", "skyfai_",
    "zoomqge", "lofkes_", "sandron", "kkanoyaa", "desuqe_",
    "dahujka_owo", "hober38_", "modlessflash", "wavewyyy", "mitor0_",
    "zxbatonzx"
]

# initial_channels = ["kartavkun"]

get_channels = 
    "kartav__", "ivango", "senyawei", "v1llix_", "glebauster",
    "godroponika", "quizzzzz_", "vudek_", "pokemonyaaa", "25mosey",
    "majewskiosu", "f0rz__", "steisha_owo", "sor0k4", "skyfai_",
    "zoomqge", "lofkes_", "sandron", "kkanoyaa", "desuqe_",
    "dahujka_owo", "hober38_", "modlessflash", "wavewyyy", "mitor0_",
    "zxbatonzx"

# get_channels = "kartavkun"

dobri_link = "https://dobri.fun"

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=API_TOKEN, prefix='!', initial_channels=initial_channels)
        self.streaming = False

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        await self.check_stream_status()  # Запускаем проверку статуса стрима

    async def check_stream_status(self):
        while True:
            streams = await self.fetch_streams(user_logins=initial_channels)
            if streams and not self.streaming:
                self.streaming = True
                await self.send_message('Стрим начался! Присоединяйтесь!')
                print("Стрим запущен")
                self.send_twitter_link.start()  # Запускаем рутину отправки ссылки
            elif not streams and self.streaming:
                self.streaming = False
                await self.send_message('Стрим завершен. Спасибо за просмотр!')
                print("Стрим отключен")
                self.send_twitter_link.stop()  # Останавливаем рутину отправки ссылки
            await asyncio.sleep(10)  # Проверять каждые 60 секунд

    @routines.routine(seconds=15)  # Отправка сообщения каждые 30 секунд
    async def send_twitter_link(self):
        await self.send_message(f'Все участники DOBRI сквада, ссылки на чаты в Telegram и Discord можешь найти здесь -> {dobri_link}')
        print("Ссылка на сайт ДОБРИ отправлена")

    async def send_message(self, message):
        channel = self.get_channel(get_channels)
        if channel:
            await channel.send(message)
        else:
            print("Канал не найден!")

    @commands.command(name='dobri')
    async def dobri(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name}, Ссылки на чат в Telegram и Discord тут -> {dobri_link}')

    @commands.command(name='добри')  # Альтернативное имя для кириллицы
    async def dobri_cyrillic(self, ctx: commands.Context):
        await self.dobri(ctx)  # Вызываем основную команду

bot = Bot()
bot.run()
