
class CSVModule(object):

    def __init__(self, data_dictionary, filename):
        self.data_dictionary = data_dictionary
        self.file_name = filename

    def save_flats_to_file(self):
        with open(self.file_name, 'a') as f:
            flat_keys = self.data_dictionary[0].keys()
            f.write("{},{}\n".format('id',','.join(flat_keys)))
            for flat_id in sorted(self.data_dictionary.keys()):
                flat_dict = self.data_dictionary.get(flat_id)
                f.write("{}".format(flat_id))
                for flat_key in flat_keys:
                    f.write(",{}".format(flat_dict[flat_key]))
                f.write("\n")













