from bs4 import BeautifulSoup

from scrapping.utils import external_data, locators


class ProductScrapper:

    def __init__(self, link):
        self.link = link
        self.page_content = BeautifulSoup(external_data.get_hml_data(link), "html.parser")

    def get_product_data(self):
        soup = self.page_content
        product_name = soup.select_one('div[class*=' + locators.CLASS_PRODUCT_NAME + ']').text
        product_tag = soup.select_one('div[class*=' + locators.CLASS_PRODUCT_BRAND + ']')
        product_brand =  product_tag.find('a', recursive=False).text
        product_span = soup.select_one('div[class*=' + locators.CLASS_PRODUCT_ID + ']')
        product_code = product_span.find('span', recursive=False).text
        product_code = product_code[product_code.index(":")+2:]
        product_specifications = soup.select_one('div[class*=' + locators.CLASS_PRODUCT_SPECIFICATION + ']')
        product_price = 0
        if product_specifications is not None:
            product_price_tag = soup.select_one('li[data-internet-price]')
            product_price = product_price_tag.attrs['data-internet-price']
        product_data = {
            "name": product_name,
            "code": product_code,
            "brand": product_brand,
            "price": product_price
        }
        return product_data

    def get_product_feature_data(self):
        soup = self.page_content
        product_information = soup.select_one('div[class*=' + locators.CLASS_PRODUCT_INFORMATION + ']')
        product_features = dict()
        if product_information is not None:
            feature_list = product_information.select_one('ul')
            for li_tag in feature_list.find_all('li'):
                ft = li_tag.text
                key = ft[:ft.find(":")]
                value = ft[ft.find(":") + 2:]
                product_features[key] = value
        return product_features

