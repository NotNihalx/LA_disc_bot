import lightbulb
import hikari

from dotenv import load_dotenv
import os

var = os.getenv('KEY')

from bs4 import BeautifulSoup
import requests
import logging

# Token

bot = lightbulb.BotApp(token= var, default_enabled_guilds=(367059007070011403))

# Event Handlers:

@bot.listen(hikari.GuildMessageCreateEvent)

async def printmsg(event):
    print(event.content)

@bot.command
@lightbulb.option('servername', 'Name of server')
@lightbulb.command('serverstatus', 'Gets server status')
@lightbulb.implements(lightbulb.SlashCommand)

async def getServer(ctx: lightbulb.context) -> None:
    page = requests.get("https://www.playlostark.com/en-gb/support/server-status").text
    soup = BeautifulSoup(page, 'html.parser')

    server_names = []
    status = []
    update_time = soup.find('div', class_='ags-ServerStatus-content-lastUpdated').text.split()
    update_time.pop(6)
    s1 = " "
    s1 = s1.join(update_time)

    for snames in soup.find_all('div', class_='ags-ServerStatus-content-responses-response-server-name'):
        server_names.append(snames.text.strip())

    for sstatus in soup.find_all('div', class_='ags-ServerStatus-content-responses-response-server-status-wrapper'):
        converted = str(sstatus)
        if "--good" in converted:
            status.append("Good")

        if "--busy" in converted:
            status.append("Busy")

        if "--full" in converted:
            status.append("Full")

        if "--maintenance" in converted:
            status.append("In Maintenance")

    directory = {}
    for i in range(len(server_names)):
        directory[server_names[i].lower()] = status[i]

    ser_name = ctx.options.servername.lower()

    def formatResults(server_name, table, format_str):
        emote = ''
        if directory[ser_name] == "Good":
            emote = " :green_square: "

        elif directory[ser_name] == "Busy":
            emote = ' :yellow_square: '

        elif directory[ser_name] == "Full":
            emote = ' :red_square: '

        else:
            emote = ' :tools: '

        return "'s current status: " + directory[ser_name].upper() + emote + "\n" + "\n" + s1

    match ser_name:
        case "mari":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "valtan":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "akkan":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "rohendel":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "bergstorm":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "enviska":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "shandi":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "azena":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "avesta":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "ladon":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "sasha":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "zosma":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "una":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "galatur":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "kharmine":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "adrinne":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "vykas":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "regulus":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "karta":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "elzowin":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "aldebaran":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "danube":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "neria":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "calvasus":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "asta":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "sceptrum":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "inanna":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "antares":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "mokoko":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "kadan":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "thirain":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "wei":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "procyon":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "thaemine":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "brelshaza":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "trixion":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "zinnervale":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "slen":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "beatrice":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "sirius":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "nineveh":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "rethramis":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "stonehearth":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "petrania":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "tortoyk":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "shadespire":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "punika":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "moonkeep":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "tragon":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "kazeros":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "vern":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "arcturus":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "agaton":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "yorn":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "kurzan":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "Gienah":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "Feiton":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case "prideholme":
            ans = formatResults(ser_name, directory, s1)
            await ctx.respond(ctx.options.servername + ans)

        case _:
            print("Invalid servername")
            output = "Could not find server " + ctx.options.servername + " . Please try again."
            await ctx.respond(output)

bot.run()