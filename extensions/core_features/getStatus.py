#Imports

import hikari
import lightbulb
from bs4 import BeautifulSoup
import requests


# GET SERVER STATUS

serverstatus_plugin = lightbulb.Plugin("server_status", "Grab the server status of any server")

@serverstatus_plugin.command
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
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title= title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "valtan":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "akkan":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "rohendel":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "bergstorm":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title= title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "enviska":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "shandi":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "azena":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "avesta":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "ladon":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "sasha":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "zosma":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "una":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "galatur":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "kharmine":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "adrinne":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "vykas":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "regulus":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "karta":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "elzowin":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "aldebaran":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "danube":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "neria":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "calvasus":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "asta":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "sceptrum":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "inanna":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "antares":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "mokoko":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "kadan":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "thirain":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "wei":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "procyon":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "thaemine":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "brelshaza":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "trixion":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "zinnervale":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "slen":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "beatrice":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "sirius":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "nineveh":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "rethramis":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "stonehearth":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "petrania":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "tortoyk":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "shadespire":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "punika":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "moonkeep":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "tragon":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "kazeros":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "vern":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "arcturus":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "agaton":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "yorn":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "kurzan":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "Gienah":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "Feiton":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case "prideholme":
            ans = formatResults(ser_name, directory, s1)
            title = str(ctx.options.servername) + ans
            embed = hikari.Embed(
                title=title,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

        case _:
            print("Invalid servername")
            output = "Could not find server " + ctx.options.servername + " . Please try again."
            embed = hikari.Embed(
                title=output,
                color='#f3a6f7')

            await ctx.respond(embed=embed)

def load(bot):
    bot.add_plugin(serverstatus_plugin)

def unload(bot):
    bot.remove_plugin(serverstatus_plugin)