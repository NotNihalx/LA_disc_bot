#Imports

import hikari
import lightbulb

fun_plugin = lightbulb.Plugin("fun", "random shit")

#Pray

prayer_count = 0

# pray to taiga's altar
@fun_plugin.command()
@lightbulb.command('pray', 'Gets server status')
@lightbulb.implements(lightbulb.SlashCommand)
async def offerPrayer(ctx):
    fname = hikari.File('./images/prayge.jpg')
    global prayer_count
    prayer_count += 1
    embed = hikari.Embed(
        title="*The Altar of Taiga has recieved your prayers and blesses upon you good rng!*\n",
        color = '#f3a6f7')
    embed.set_image(fname)
    embed.set_footer(str(prayer_count) + " prayer(s) offered to the Altar of Taiga\n")
    await ctx.respond(embed=embed)


def load(bot):
    bot.add_plugin(fun_plugin)

def unload(bot):
    bot.remove_plugin(fun_plugin)