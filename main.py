import time
import requests
import os


def notify(title, text):
    os.system("""
              osascript -e 'display dialog "{}" with title "{}"'
              """.format(text, title))


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"


def get_adidas_stock(sku):
    print(f"Checking availability for {sku}")
    availability_url = f"https://www.adidas.com.br/api/products/{sku}/availability"
    availability = requests.get(availability_url, headers={"User-Agent": user_agent}).json()
    return {size['size']: size['availability_status'] for size in availability['variation_list']}


def verify_product_availability(sku, wanted_sizes):
    stock = get_adidas_stock(sku)
    for wanted_size in wanted_sizes:
        if stock[wanted_size] == "IN_STOCK":
            notify("ACHOU!", f"TEM {wanted_size} KRL!!!")


if __name__ == '__main__':
    while True:
        verify_product_availability(sku="HK7417", wanted_sizes=["P", "M"])
        time.sleep(60)
