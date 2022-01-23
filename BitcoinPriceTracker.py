from urllib.request import urlopen
import time

count = 0
maxCount = 10000000  # 10,000,000
fileCount = 0
maxFileCount = 10000  # 10,000

while True:
    url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'
    response = urlopen(url)
    webContent = response.read()
    file = open("output" + str(fileCount) + ".txt", "a")
    file.write(str(webContent) + '\n\n')
    # print(webContent)
    file.close()
    count += 1
    if count == maxCount:
        fileCount += 1
        count = 0
    if fileCount == maxFileCount:
        break
    time.sleep(60)
