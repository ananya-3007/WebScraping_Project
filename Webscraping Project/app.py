import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        'product_url': 'https://www.flipkart.com/samsung-galaxy-s24-fe-5g-graphite-128-gb/p/itme960199e26f23?pid=MOBH4ZG33EBNZKS7&lid=LSTMOBH4ZG33EBNZKS751CITE&marketplace=FLIPKART&q=m31s+samsung&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&fm=Search&iid=fe4253dd-6786-4403-b1ed-c22224204d96.MOBH4ZG33EBNZKS7.SEARCH&ppt=sp&ppn=sp&ssid=w90qjsep5s0000001743337857711&qH=fd5342c3c31e8bfe',
        'Name': 'Samsung Galaxy s24',
        'target_price': 40000
    },
    {
        'product_url': 'https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&lid=LSTMOBGTAGPTB3VS24WCTBCFM&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=1049121e-9212-4cd4-974a-6fba354060ea.MOBGTAGPTB3VS24W.SEARCH&ppt=pp&ppn=pp&ssid=caqv3bwi740000001743518386958&qH=0b3f45b266a97d70',
        'Name': 'Iphone',
        'target_price':50000
    },
    {'product_url':'https://www.flipkart.com/samsung-galaxy-s24-fe-5g-graphite-256-gb/p/itme960199e26f23?pid=MOBH92ADENNW264G&lid=LSTMOBH92ADENNW264GL2SZDV&marketplace=FLIPKART&q=m31+samsung&store=tyy%2F4io&srno=s_1_8&otracker=search&otracker1=search&fm=Search&iid=46e86508-9c6f-4c68-bb64-57a11d1f3baa.MOBH92ADENNW264G.SEARCH&ppt=sp&ppn=sp&ssid=vvsf7vvfjk0000001743518208199&qH=9c4c838c862c74c4',
     'Name' : 'Samsung Galaxy FE 5g',
     'target_price': 47000
     },
    {'product_url':'https://www.flipkart.com/redmi-13-5g-hawaiian-blue-128-gb/p/itmede93b8d7b1a4?pid=MOBH45GGFZNWZMK6&lid=LSTMOBH45GGFZNWZMK6NXS5CG&marketplace=FLIPKART&q=redmi&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=5e3cf698-3c48-4150-8db4-138f685e0bf9.MOBH45GGFZNWZMK6.SEARCH&ppt=sp&ppn=sp&ssid=omoozainv40000001743530709031&qH=9b6bf0057c19bd94',
     'Name':'REDMI 13 5G ',
     'target_price':13000
     },
    {
        'product_url':'https://www.flipkart.com/vivo-t3-pro-5g-sandstone-orange-256-gb/p/itmcf52c1fcffbf3?pid=MOBH3XHR46RHEMVH&lid=LSTMOBH3XHR46RHEMVHQKBFEZ&marketplace=FLIPKART&q=vivo&store=tyy%2F4io&srno=s_1_5&otracker=search&otracker1=search&fm=Search&iid=6bd565a3-69a5-45ab-9dbd-04bdf32b2757.MOBH3XHR46RHEMVH.SEARCH&ppt=pp&ppn=pp&ssid=vh5hjjy6k00000001743530817268&qH=b09207f5c299c427',
        'Name':'Vivo T3 Pro 5G ',
        'target_price':20000
    }

]


def product_price_section(URL):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')

    # Use the class 'Nx9bqj CxhGGd' to find the price
    product_price = soup.find("div", {"class": "Nx9bqj CxhGGd"})  # Updated to use the correct class name

    if product_price:
        return product_price.get_text().strip()  # Get the price text and remove leading/trailing spaces


result_file=open('Price_Page.txt','w')
try:
    # Loop through products and fetch their price
    for every_product in products_to_track:
        product_price_returned = product_price_section(every_product.get('product_url'))
        print(f"Price of {every_product['Name']}: {product_price_returned}")

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(my_product_price)
        print(my_product_price)

        # logic to find whether which phone is available in best price
        if (my_product_price < every_product.get('target_price')):
            print('Available in best offers')
            result_file.write(every_product.get('Name') +'- \t'+  str(my_product_price)+'\n')
        else:
            print('Still the same')
finally:
    result_file.close()










