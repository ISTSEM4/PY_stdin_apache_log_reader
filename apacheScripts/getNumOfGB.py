# b. Funkcja, która wypisuje sumaryczną liczbę danych wysłanych do hostów podaną w
# gigabajtach

import sys
from myUtils import apacheLogParser as parser, printer
from myUtils.lineAttributes import Attribute
from myUtils.parsingManager import ParsingManager


def main():
    parsing_manager = ParsingManager()

    num_of_bytes = 0

    for line in sys.stdin:
        if parsing_manager.process_line(line):
            num_of_bytes += int(parser.get_attribute(Attribute.RESPONSE_SIZE, line))

    num_of_gigabytes = round(num_of_bytes / 1024 / 1024 / 1024, 2)

    printer.automatic_print_task_result(
        "b",
        "Funkcja, która wypisuje sumaryczną liczbę danych wysłanych do hostów podaną w gigabajtach",
        f"Sum of data: {num_of_gigabytes} GB",
        parsing_manager.list_of_err,
        parsing_manager.lines_read,
        5
    )


if __name__ == "__main__":
    main()