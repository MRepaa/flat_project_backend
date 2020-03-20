
from Parser import Parser
import BeautifulSoup
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests



class OtoDomParserNew(Parser):

    def __init__(self, html_content):
        self.html_content = html_content
        self.soup_html = BeautifulSoup.BeautifulSoup(self.html_content)
        self.html_flats = self.find_flats()
        self.html_image = self.find_image()
        self.flats = {}
        self.flat_title = ''
        self.link = ''
        self.to_negotiate = ''
        self.price = ''
        self.city_district = ''
        self.renting_or_selling = ''
        self.area = ''
        self.rooms = ''
        self.image = ''
        self.market = ''



    def find_flats(self):
        find_flats = []
        for offer_item in self.soup_html.findAll('div', {'class': 'offer-item-details'}):
            if offer_item.find('span', {'class': 'offer-item-title'}):
                find_flats.append(offer_item)


        return find_flats

    def find_image(self):
        find_image = []
        for offer_item in self.soup_html.findAll('figure', {'class': 'offer-item-image'}):
            find_image.append(offer_item)

        image_list = []
        for image in find_image:
            image_list.append(image)

        return image_list


    def collect_flats_info(self):
        for i, flat in enumerate(self.html_flats):
            flat = Flat(flat)
            self.id_flat = i
            self.flat_title = flat.title_of_flat()
            self.link = flat.link()
            self.to_negotiate = flat.to_negotiate()
            self.price = flat.price()
            self.city_district = flat.city_disctrict()
            self.renting_or_selling = flat.renting_or_selling() #replace
            self.area = flat.the_area()
            self.rooms = flat.numbers_of_rooms()
            self.market=flat.type_of_market()
            # self.add_flat(i)



            for i, image in enumerate(self.html_image):
                image = Image(image)
                self.image = image.the_image()
                self.image_id = i

                if self.id_flat == self.image_id:
                    self.add_flat(i)






    def add_flat(self, id_flat):
        self.flats.update({id_flat: {'flat_title': self.flat_title, 'link': self.link, 'to_negotiate': self.to_negotiate,
                                 'price': self.price, 'city_district': self.city_district,
                                 'renting_or_selling': self.renting_or_selling, 'area':self.area, 'market':self.market, 'rooms':self.rooms,
                                     'image':self.image}})

    def get_flats_info(self):
        return self.flats


class Flat(Parser):

    def __init__(self, flat):
        self.flat = flat

    def title_of_flat(self):
        flat_title = self.flat.find('span', {'class':'offer-item-title'}).getText()
        return flat_title.replace(',',' ').encode('utf=8')

    def link(self):
        flat_link = self.flat.find('a')
        single_link = flat_link['href'].encode('utf=8')
        return flat_link['href'].encode('ascii', 'ignore').decode('ascii')

    def to_negotiate(self):
        span_key = self.flat.find('span', {'class': 'normal inlblk pdingtop5 lheight16 color-2'})
        if span_key:
            to_negotiate = span_key.getText().encode('utf=8')
        else:
            to_negotiate = None
        return to_negotiate

    def price(self):
        flat_price = self.flat.find('li', {'class': 'offer-item-price'}).getText()
        return flat_price.encode('utf=8').replace(',', '.')

    def city_disctrict(self):
        city_district = self.flat.find('p').getText().encode('1252', 'ignore').decode('1252')
        city_district = city_district.replace(',','').replace(u'Mieszkanie na sprzeda',"")
        city_district = city_district.replace(',','').replace(u'Mieszkanie na wynajem',"")

        return city_district.replace(':','').encode('utf=8')

    def renting_or_selling(self):
        flat_renting_or_selling = self.flat.find('p').getText().encode('1252', 'ignore').decode('1252')
        return flat_renting_or_selling.split(':')[0].encode('utf=8')

    def the_area(self):
        area= self.flat.find("li",{'class':'hidden-xs offer-item-area'}).getText().encode('1252', 'ignore').decode('1252')
        return "".join(area.encode('utf=8')).replace(',', '.')


    def numbers_of_rooms(self):
        rooms = self.flat.find("li",{'class':'offer-item-rooms hidden-xs'}).getText()
        return rooms

    def type_of_market(self):
        market = 'nowy'
        return market



class Image(object):

    def __init__(self, image):
        self.image = image

    def the_image(self):
        image = self.image.find('span', {'class':'img-cover lazy'})
        image = image.get('data-src')
        return image




