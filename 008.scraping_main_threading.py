import datetime
import json
import requests
import concurrent.futures


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Is-Ajax-Request": "X-Is-Ajax-Request",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}

url = "https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1=1"
r = requests.get(url=url, headers=headers)

pages_count = r.json()["pageCount"]

data_list = []


def get_data(page):
    start_time = datetime.datetime.now()
    url = f"https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1={page}"

    r = requests.get(url=url, headers=headers)
    data = r.json()
    items = data["items"]

    possible_stores = ["discountStores", "fortochkiStores", "commonStores"]
    for item in items:
        total_amount = 0

        item_name = item["name"]
        item_price = item["price"]
        item_img = f'https://roscarservis.ru{item["imgSrc"]}'
        item_url = f'https://roscarservis.ru{item["url"]}'

        stores = []
        for ps in possible_stores:
            if ps in item:
                if item[ps] is None or len(item[ps]) < 1:
                    continue
                else:
                    for store in item[ps]:
                        store_name = store["STORE_NAME"]
                        store_price = store["PRICE"]
                        store_amount = store["AMOUNT"]
                        total_amount += int(store["AMOUNT"])

                        stores.append(
                            {
                                "store_name": store_name,
                                "store_price": store_price,
                                "store_amount": store_amount
                            }
                        )

        data_list.append(
            {
                "name": item_name,
                "price": item_price,
                "url": item_url,
                "img_url": item_img,
                "stores": stores,
                "total_amount": total_amount
            }
        )

    print(f"[INFO] Обработал {page}/{pages_count}")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_data, range(1, pages_count + 1))

cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

with open(f"data_{cur_time}.json", "w") as file:
    json.dump(data_list, file, indent=4, ensure_ascii=False)
