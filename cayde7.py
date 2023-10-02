import lightbulb
import requests as req
bot = lightbulb.BotApp(token=open('./tokens/token_ds.txt', 'r').read(),
                 default_enabled_guilds=(int(open('./tokens/channel_id.txt', 'r').read())))

@bot.command
@lightbulb.command('msg_bot', 'Olá @everyone')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('*Olá, pessoal!*')


# TODO : verificar requisicao de parametro 
@bot.command
@lightbulb.command('d2', 'Mostra info da conta')# AQUI
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def init():
    pass
@init.child
@lightbulb.option('id','ID do usuario',type=int)
@lightbulb.command('id','Mostra info relacionadas ao ID')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def info(ctx):

    API_key = open('./tokens/BungieAPI_key.txt','r').read()
    url = f"https://www.bungie.net/Platform/User/GetBungieNetUserById/{ctx.options.id}"


    headers = {
    'x-api-key': f'{API_key}',
    'Authorization': 'Basic NDU0NTc6'
    }

    response = req.request("GET", url, headers=headers)

    await ctx.respond(response.text)

bot.run()