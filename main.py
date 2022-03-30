
#KEYS
import os
var = os.getenv('KEY')
tempvar = "OTU1NjAzNjU5ODgwODA4NDg5.YjkFQg.Uo2JlK9j8FnuLC6ndck3jCBdUdY" #delete this

# IMPORTS
import lightbulb
import hikari


# BASIC BOT SET UP

bot = lightbulb.BotApp(token= tempvar,
        default_enabled_guilds=(367059007070011403, 221193300344832001, 256614629260787724),
        ignore_bots = True,
        help_slash_command=True)


# EXTENSIONS

bot.load_extensions_from("./extensions/", must_exist=True, recursive=True)

#RUN

@bot.listen(hikari.GuildMessageCreateEvent)

async def printmsg(event):
    print(event.content)

if __name__ == "__main__":

    bot.run(
            status=hikari.Status.ONLINE,
            activity=hikari.Activity(
                name=("Lost Ark API Waiting Room"),
                type=hikari.ActivityType.PLAYING
                )
            )