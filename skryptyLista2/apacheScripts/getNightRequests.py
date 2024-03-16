#f. Funkcja, która wypisuje na wyjście standardowe zasoby pobierane pomiędzy 22 a 6 rano.

import sys
from myUtils import apacheLogParser as parser, testUseful, printer
from myUtils.lineAttributes import Attribute
from myUtils.parsingManager import ParsingManager


def main():
    parsing_manager = ParsingManager()

    night_requests = []

    for line in sys.stdin:
        if parsing_manager.process_line(line):
            if int(parser.get_attribute(Attribute.TIME)[:2]) >= 22 or int(parser.get_attribute(Attribute)[:2]) <= 6:
                night_requests.append(line)

    printer.automatic_print_task_result(
        "f",
        "Funkcja, która wypisuje na wyjście standardowe zasoby pobierane pomiędzy 22 a 6 rano.",
        f"Theese are them lines requested at night time: {"\n".join(night_requests)}",
        parsing_manager.list_of_err,
        parsing_manager.lines_read,
        5
    )


if __name__ == "__main__":
    main()