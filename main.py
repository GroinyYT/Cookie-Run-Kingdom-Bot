import discord
from PIL import Image,ImageFont,ImageDraw
from discord.ext import commands
import textwrap


bot = commands.Bot(command_prefix="crk! ")

@bot.event
async def on_connect():
  print ("Bot is online")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Groiny's videos!"))


@bot.command()
async def fitness(ctx):
  await ctx.channel.send("The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.")

@bot.command()
async def youtube(ctx):
  await ctx.channel.send("Here is Groiny's Youtube: https://www.youtube.com/channel/UCheaJhbAn_Xcy2qtW4yBT-w")

@bot.command()
async def pullscreenfake(ctx, *, text = "No text entered"):

  img = Image.open("defbg.png")
  font = ImageFont.truetype("CookieRun Bold.otf",34)

  width, height = 980,492

  draw = ImageDraw.Draw(img)
  
  draw.text(
    xy=(width / 2, height / 2),
    text=text,
    fill="#5B56AA",
    font=font,
    anchor="mm",
    align="center"
    )
  img.save("text.png")
    

  await ctx.send(file = discord.File("text.png"))

token =("OTg5OTE2NTgzNzU1MzkwOTg2.GHvt31.mm1wSRvX1_7ba-bxXR3hmDxg2LMeBKI0noEv2w")
bot.run(token)
