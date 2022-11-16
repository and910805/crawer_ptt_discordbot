import discord
from discord.ext import commands
import json
import random
import time
with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)


intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

client = discord.Client(intents=intents)

#---------------------------------當前時間格式化
now = time.localtime(time.time())
if int(now.tm_mday)<10:#11/01!=11/1
    string_date =str(now.tm_mon)+'/0'+str(now.tm_mday)
else:
    string_date =str(now.tm_mon)+'/'+str(now.tm_mday)
string_date2 =str(now.tm_mon)+'_'+str(now.tm_mday)#存txt名稱
string_hour =str(now.tm_hour)

string_minute =str(now.tm_min)
#-------------------------------------------

@bot.event
async def on_ready():
    print(">>Bot is online<<")


@bot.command()
async def ping(ctx):#ctx自動偵測說話那個人資料
    await ctx.send(f'{round(bot.latency*1000)}(ms)')#latency延遲
@bot.command()
async def 功能(ctx):
    await ctx.send('目前只有ping,ptt兩個指令，等之後慢慢推出')
    await ctx.send('```!ping```\n'+'```!ptt 位元數  例如!ptt 100\n但注意後面位元1<=n<=2000```')
@bot.command()
async def ptt(ctx,arg):
    file_name = "ptt_"+string_date2+'_'+string_hour
    f=open("./temp/" + file_name + ".txt", "r",encoding="utf-8") 
    await ctx.send(f.read(int(arg)))
    f.close()
   
bot.run(jdata['TOKEN'])#字典去找token

