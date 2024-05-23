import discord
from discord.ext import commands
import random
import requests
import os
from settings import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, *content):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open('images/mem2.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command('karton')
async def karton(ctx):
    await ctx.send(f'''Простые фигурки животных из картона, в технике "квиллинг"
Эта поделка идеально подходит для того, чтобы сделать её вместе с детьми. Просто и увлекательно!
Для создания фигурок нам понадобится:
картон;
цветная бумага для декора;
ножницы;
клей;
фломастеры, цветные карандаши;
прочие элементы декора на ваше усмотрение.
                   

Мы расскажем, как сделать медвежонка в данной технике
Шаг 1. Нарезаем полоску из картона для будущего тела, лапок и ушей.
Шаг 2. Сворачиваем полоски в круги. Самый большой – тело медведя, круг поменьше – голова. Скручиваем шесть небольших кружочков. Это будут лапы и уши.
Шаг 3. С помощью клея надо склеить все детали воедино. На этом уже можно остановиться, но мы решили добавить нашему мишке глаза и нос, вырезанные из цветной бумаги. Можно добавить к медведю баночку вкусного меда или спелую ягоду. Все, как вам подсказывает фантазия!
Шаг 4: Радуемся результату! Наш мишка из обычного картона готов!''')
    

@bot.command('topcars')
async def topcars(ctx):
    await ctx.send(f'''Посмотрите на топ самых быстрых машин в мире
1.Bugatti Chiron Super Sport 300+, 490 км/ч
2.Koenigsegg Jesko Absolut, 447,19 км/ч
3.Rimac Nevera, 415 км/ч
4.SSC Tuatara, 508,73 км/ч
5.Hennessey Venom F5, 437 км/ч
6.Pininfarina Battista, 350 км/ч''')
                   
bot.run(token)
