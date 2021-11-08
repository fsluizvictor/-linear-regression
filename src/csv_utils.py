import csv
from typing import List


def open_file_csv(file_name: str) -> List[List[str]]:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        file_rows = list()
        for row in spamreader:
            content_row = row
            if row.__contains__(','):
                content_row = str(row).split(',')
            file_rows.append(content_row)
    return file_rows


def write_file_csv(file_name: str, content: List[str]):
    with open(file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for row in content:
            spamwriter.writerow(row)
