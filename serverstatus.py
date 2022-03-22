from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.playlostark.com/en-gb/support/server-status").text
soup = BeautifulSoup(page, 'lxml')

def getStatus(input):
    server_names = []
    status = []
    update_time = soup.find('div', class_ = 'ags-ServerStatus-content-lastUpdated').text.split()
    update_time.pop(6)
    s1 = " "
    s1 = s1.join(update_time)

    for snames in soup.find_all('div', class_ = 'ags-ServerStatus-content-responses-response-server-name'):
        server_names.append(snames.text.strip())

    for sstatus in soup.find_all('div', class_ = 'ags-ServerStatus-content-responses-response-server-status-wrapper'):
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

    modified = input.lower()

    print(directory)
    if modified in directory:
        return s1 + "\n" + input + "'s current status: " + directory[modified].upper()
    else:
        return "No results found. Please enter a valid server name"


print(getStatus('Neria'))
