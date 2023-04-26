import disnake
from disnake.ext import commands


TOKEN = input('Enter Your Token Here : ')

bot = commands.Bot()


@bot.event
async def on_ready():
    print(
        f'OK.\n I login in  {bot.user.name} \n Add bot in your server and use /active command \n\n Invite Link : https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands'
    )


@bot.slash_command()
async def active(inter):
    await inter.response.send_message('''Wait 24 hours and then receive your badge:
   Get your badge: https://discord.com/developers/active-developer 
    Github: https://github.com/PixerDev''')


bot.run(TOKEN)
