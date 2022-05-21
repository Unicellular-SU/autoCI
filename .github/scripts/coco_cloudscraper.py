import cloudscraper

scraper = cloudscraper.create_scraper()

url = "https://www.cocomanga.com/js/custom.js"
js = scraper.get(url).text
print(js)


f = open("decrypted.js", "w")
f.write(js)
f.close()
