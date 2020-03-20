from prettytable import PrettyTable


def open_file(filename):
    csv_file = open(filename, 'r')
    csv_file_lines = csv_file.readlines()
    return csv_file_lines


def produce_table_titles(csv_file_lines):
    line_1 = csv_file_lines[0]
    line_1 = line_1.split(',')
    table_content = PrettyTable([line_1[0], line_1[1], line_1[2], line_1[3], line_1[4], line_1[5], line_1[6]])
    return table_content


def split_lines_and_add_table_content(table_content):
    lines = []
    for line in lines:
        line = line.split(',')
        lines.append(line)
    for a in range(1, len(lines)):
        table_content.add_row(a)
    return table_content



def generate_html_file(table_content):
    html_code = table_content.get_html_string()
    html_file = open('table.html', 'w')
    html_file = html_file.write(html_code)
    return html_file


def main():
    csv_file_in_lines = open_file('flats_info.csv')
    titles_of_table = produce_table_titles(csv_file_in_lines)
    table_content = split_lines_and_add_table_content(csv_file_in_lines)
    print table_content
    print "Generowanie pliku html z pliku csv"
    generate_html_file(titles_of_table)



if __name__ == '__main__':
    main()