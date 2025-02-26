from twitchio.ext import commands

dobri_link = "https://dobri.fun"

class TwitchBot(commands.Bot):

    def __init__(self, token, initial_channels):
        super().__init__(token=token, prefix='!', initial_channels=initial_channels)
        # self.streaming_channels = set()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    @commands.command(name='dobri')
    async def dobri(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name}, Ссылки на чат в Telegram и Discord тут -> {dobri_link}')

    @commands.command(name='добри')  # Альтернативное имя для кириллицы
    async def dobri_cyrillic(self, ctx: commands.Context):
        await self.dobri(ctx)  # Вызываем основную команду
