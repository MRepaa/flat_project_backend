from Parser import Parser
import BeautifulSoup



class OLXParser(object):

    def __init__(self, html_content):
        self.html_content = html_content
        self.soup_html = BeautifulSoup.BeautifulSoup(self.html_content)
        self.html_flats = self.find_flats()
        self.flats = {}
        self.flat_title = ''
        self.link = ''
        self.to_negotiate = ''
        self.price = ''
        self.city_district = ''
        self.renting_or_selling = ''
        self.image= ''
        self.rooms = ''

    def find_flats(self):
        return self.soup_html.findAll('div', {'class': 'offer-wrapper'})

    def collect_flats_info(self):
        for i, flat in enumerate(self.html_flats):
            flat = Flat(flat)
            self.flat_title = flat.title_of_flat()
            self.link = flat.link()
            self.to_negotiate = flat.to_negotiate()
            self.price = flat.price()
            self.city_district = flat.city_disctrict()
            self.renting_or_selling = flat.renting_or_selling()
            self.image = flat.the_image()
            self.rooms = flat.number_of_rooms()
            self.add_flat(i)

    def add_flat(self, id_flat):
        self.flats.update({id_flat: {'flat_title': self.flat_title, 'link': self.link, 'to_negotiate': self.to_negotiate,
                                 'price': self.price, 'city_district': self.city_district,
                                 'renting_or_selling': self.renting_or_selling, 'image':self.image, 'rooms':self.rooms}})

    def get_flats_info(self):
        return self.flats


class Flat(Parser):

    def __init__(self, flat):
        self.flat = flat
        #print self.flat


    def title_of_flat(self):
        flat_title = self.flat.find("strong").getText()
        return flat_title.replace(',',' ').encode('utf=8')

    def link(self):
        flat_link = self.flat.find('a')
        flat_link = flat_link['href'].encode('utf=8')
        return flat_link

    def to_negotiate(self):
        span_key = self.flat.find('span', {'class': 'normal inlblk pdingtop5 lheight16 color-2'})
        if span_key:
            to_negotiate = span_key.getText().encode('utf=8')
        else:
            to_negotiate = None
        return to_negotiate

    def price(self):
        flat_price = self.flat.find('p', {'class': 'price'}).findChild().getText()
        return flat_price.encode('utf=8')

    def city_disctrict(self):
        small_keys = self.flat.findAll('small', {'class': 'breadcrumb x-normal'})
        for key in small_keys:
            span_key = key.find('span')
            if span_key:
                span_content = span_key.getText()
                if ',' in span_content:
                    return span_content.replace(',',':').encode('utf=8')

    def renting_or_selling(self):
        flat_renting_or_selling = self.flat.find('small', {'class': 'breadcrumb x-normal'}).getText()
        return flat_renting_or_selling.encode('utf=8')

    def the_image(self):
        image = self.flat.find('img', {'class':'fleft'})
        try:
            image=image.get('src')
        except:
            image=image

        return image





