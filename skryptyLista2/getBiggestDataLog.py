# c. Funkcja, która wypisuje na wyjście standardowe ścieżkę i rozmiar największego zasobu.

import sys
import apacheLogParser as parser
import lineAttributes
import printer

list_of_err = []
num_of_lines = 0
# TODO moznaby zrobic lepsze kryterium brania 1.
biggest_data_log = sys.stdin.readline()
for line in sys.stdin:
    try:
        num_of_lines += 1
        parser.validate_line(line)
    except TypeError as e:
        # we remember all errors with their description
        list_of_err.append((line, e.args[0]))
    else:
        if parser.get_attribute(lineAttributes.Attribute.RESPONSE_SIZE, line) > parser.get_attribute(
                lineAttributes.Attribute.RESPONSE_SIZE, biggest_data_log):
            biggest_data_log = line

printer.automatic_print_task_result(
    "c",
    "Funkcja, która wypisuje na wyjście standardowe ścieżkę i rozmiar największego zasobu",
    f"Biggest data pull: {parser.get_attribute(lineAttributes.Attribute.RESPONSE_SIZE, biggest_data_log)} Bytes \npath: {parser.get_attribute(lineAttributes.Attribute.PATH_INFO, biggest_data_log)}",
    list_of_err,
    num_of_lines,
    5
)
