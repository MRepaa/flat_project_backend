import json

class JSONfilter(object):

    def __init__(self, json_data, filter_market, market_value):
        self.json_data = json_data
        self.filter_market = filter_market
        self.market_value = market_value
        self.filtered_dict = {}

    def filter_flats_result(self):
        for k1, v1 in self.json_data.iteritems():
            for k2, v2 in v1.iteritems():
                v1 = json.dumps(v1)
                v1 = json.loads(v1)
                print(self.filter_market)
                print(v1[self.filter_market])
                output_dict = [x for x in v1.items() if v1[self.filter_market] == self.market_value]
                temporary_dict = {}
                for i in output_dict:
                    key = i[0]
                    value = i[1]
                    temporary_dict.update({key: value})
                    # print(temporary_dict)
                    self.filtered_dict.update({k1: temporary_dict})
        return self.filtered_dict



