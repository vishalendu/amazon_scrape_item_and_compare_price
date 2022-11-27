# amazon_scrape_item_and_compare_price
Python scripts to scrape an item price from Amazon.in and analyse price trend
  
-----------  
#scraper.py  
-----------  
uses beautifulsoap to get item and price information after searching amazon.in, (only the first result page)  
sample search is for iphone+model example iphone+12  
since I could not find a unique identifier for the item(sku) and price data. I have to again search for a keyword inside the values returned.  
  
``` if(sku.text.find('Apple')==0):```  
this like is additional search in the results of find operation. Its important to note that the results can change based on the css class, in case it is changed by Amazon.  
  
This script also creates/updates a sqlite db with the data from the query. Sample SQLite_amazon.db is attached.  
  
--------------  
#savetodb.py  
--------------  
This file has functions to create and update the sqlite table.  
    
  
-------------------   
#analyse_data.ipynb  
-------------------  
This is a sample jupyter script to compare the data returned.  
  
  
Python Packages used:  
~~~~~~~~~~~~~~~~~~~~~  
BeautifulSoup4  
requests  
datetime  
pandas  
sqlite3  
