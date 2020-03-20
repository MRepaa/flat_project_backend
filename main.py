import requests
from OLXParser import OLXParser
from OtoDomParser import OtoDomParser
from OtoDomParserNew import OtoDomParserNew
from OtoDomParserOld import OtoDomParserOld
from JSONfilter import JSONfilter
import json
import os


oto_dom_html_new = 'https://www.otodom.pl/sprzedaz/nowe-mieszkanie/?search%5Bdescription%5D=1&search%5Bcity_id%5D=39'
oto_dom_html_old ='https://www.otodom.pl/sprzedaz/mieszkanie/?search%5Bfilter_enum_market%5D%5B0%5D=secondary&search%5Bdescription%5D=1&search%5Bcity_id%5D=39'
oto_dom_html_renting ='https://www.otodom.pl/wynajem/mieszkanie/'


def main():
    filter_market = 'market'
    market_value = 'rynek wtorny'


    oto_dom_page_selling_new = requests.get(oto_dom_html_new)
    oto_dom_page_selling_old = requests.get(oto_dom_html_old)
    oto_dom_page_renting = requests.get(oto_dom_html_renting)

    parsers = [

        OtoDomParserNew(oto_dom_page_selling_new.content),
        OtoDomParserOld(oto_dom_page_selling_old.content),
        OtoDomParser(oto_dom_page_renting.content)
    ]

    results = []
    for parser in parsers:
        parser.collect_flats_info()
        flats = parser.get_flats_info()
        json_flats = json.dumps(flats)

        if filter_market and market_value:
            FlatFilter = JSONfilter(flats, filter_market, market_value)
            filtered_result = FlatFilter.filter_flats_result()
            results.append(filtered_result)
        else:
            results.append(flats)
    print(len(results))
    filtered_result = dict(enumerate(results))
    print(filtered_result)


    # for i in results:
    #     if i != {}:
    #         filtered_result = i
    # print filtered_result


if __name__ == '__main__':
    main()

