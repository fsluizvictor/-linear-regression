import csv
from typing import List


def open_file_csv(file_name: str) -> List[List[float]]:
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        content_all = list()
        for row in spamreader:
            file_rows = list()
            for n in row:
                file_rows.append(float(n))
            content_all.append(file_rows)
    return content_all


def write_file_csv(file_name: str, content: List[str]):
    with open(file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for row in content:
            spamwriter.writerow(row)
