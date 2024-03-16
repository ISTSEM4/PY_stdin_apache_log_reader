# c. Funkcja, która wypisuje na wyjście standardowe ścieżkę i rozmiar największego zasobu.

import sys
from myUtils import apacheLogParser as parser, testUseful, printer
from myUtils.lineAttributes import Attribute
from myUtils.parsingManager import ParsingManager


def main():
    parsing_manager = ParsingManager()

    biggest_data_log = testUseful.make_valid_with_small_bytes()

    for line in sys.stdin:
        if parsing_manager.process_line(line):
            if parser.get_attribute(Attribute.RESPONSE_SIZE, line) > parser.get_attribute(
                    Attribute.RESPONSE_SIZE, biggest_data_log):
                biggest_data_log = line

    printer.automatic_print_task_result(
        "c",
        "Funkcja, która wypisuje na wyjście standardowe ścieżkę i rozmiar największego zasobu",
        f"Biggest data pull: {parser.get_attribute(Attribute.RESPONSE_SIZE, biggest_data_log)} Bytes \npath: {parser.get_attribute(Attribute.PATH_INFO, biggest_data_log)}",
        parsing_manager.list_of_err,
        parsing_manager.lines_read,
        5
    )


if __name__ == "__main__":
    main()
    sys.stdout.write("AAAAA")