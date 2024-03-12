# b. Funkcja, która wypisuje sumaryczną liczbę danych wysłanych do hostów podaną w
# gigabajtach

import sys
import apacheLogParser as parser
import lineAttributes
import printer

list_of_err = []
num_of_lines = 0
num_of_bytes = 0

for line in sys.stdin:
    try:
        num_of_lines += 1
        parser.validate_line(line)
    except TypeError as e:
        # we remember all errors with their description
        list_of_err.append((line, e.args[0]))
    else:
        num_of_bytes += int(parser.get_attribute(lineAttributes.Attribute.RESPONSE_SIZE, line))


printer.automatic_print_task_result(
    "b",
    "Funkcja, która wypisuje sumaryczną liczbę danych wysłanych do hostów podaną w gigabajtach",
f"Sum of data: {round(num_of_bytes/1024/1024/1024, 2)} GB",
    list_of_err,
    num_of_lines,
    5
)