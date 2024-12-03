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
        await self.check_stream_status()  # Запускаем проверку статуса стрима

    async def check_stream_status(self):
        while True:
            streams = await self.fetch_streams(user_logins=initial_channels)
            current_streaming_channels = {stream.user.name for stream in streams}  # Используем stream.user.name

        # Проверяем, какие каналы начали или прекратили стрим
            new_streaming_channels = current_streaming_channels - self.streaming_channels
            stopped_streaming_channels = self.streaming_channels - current_streaming_channels

            if new_streaming_channels:
                self.streaming_channels.update(new_streaming_channels)
                print("Стрим запущен для:", new_streaming_channels)
                self.send_twitter_link.start()  # Запускаем рутину отправки ссылки

            if stopped_streaming_channels:
                self.streaming_channels.difference_update(stopped_streaming_channels)
                print("Стрим остановлен для:", stopped_streaming_channels)
            if not self.streaming_channels:
                self.send_twitter_link.stop()  # Останавливаем рутину, если нет стримов

            await asyncio.sleep(60)  # Проверять каждые 60 секунд

    @routines.routine(minutes=15)  # Отправка сообщения каждые 15 минут
    async def send_twitter_link(self):
        for channel_name in self.streaming_channels:
            channel = self.get_channel(channel_name)
            if channel:
                await channel.send(f'Все участники DOBRI сквада, ссылки на чаты в Telegram и Discord можешь найти здесь -> {dobri_link}')
                print(f"Ссылка на сайт ДОБРИ отправлена в {channel_name}")
            else:
                print(f"Канал {channel_name} не найден!")

    @commands.command(name='dobri')
    async def dobri(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name}, Ссылки на чат в Telegram и Discord тут -> {dobri_link}')

    @commands.command(name='добри')  # Альтернативное имя для кириллицы
    async def dobri_cyrillic(self, ctx: commands.Context):
        await self.dobri(ctx)  # Вызываем основную команду

bot = Bot()
bot.run()
