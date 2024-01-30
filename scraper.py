import bs4,requests,sqlite3
def scraper(page):
    site = f'https://www.jumia.co.ke/flash-sales/?page={page}#catalog-listing'
    req = requests.get(site)
    if req.status_code == 200:
        soup = bs4.BeautifulSoup(req.text,'lxml')
        items = soup.select('.name')
        item_prices = soup.select('.prc')

        item = [x.get_text() for x in items]
        prices = [i.get_text() for i in item_prices]

        clean_prices = []

       # filtering the prices data to remain with prices in integer form 
        
        for k in prices:
            text = k.split('KSh')
            text = text[-1]
            text = text.replace(',','')
            clean_prices.append(int(text))
        
        for j in range(len(item)):
            curr.execute('INSERT INTO Flash_Sale_Items (item,item_price) VALUES (?,?)',(item[j],clean_prices[j]))
        conn.commit()
        


conn = sqlite3.connect('goodsdata.sqlite')
curr = conn.cursor()

curr.execute("CREATE TABLE IF NOT EXISTS Flash_Sale_Items(item_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,item TEXT,item_price INTEGER)")    

# scrape mutiple pages of the site
for num in range(8):
    scraper(num)
conn.close()
