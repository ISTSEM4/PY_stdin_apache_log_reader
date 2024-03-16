#e. Funkcja, która wypisuje na wyjście standardowe tylko wiersze z kodem odpowiedzi 200.

import sys
from myUtils import apacheLogParser as parser, printer
from myUtils.lineAttributes import Attribute
from myUtils.parsingManager import ParsingManager


def main():
    parsing_manager = ParsingManager()

    lines_with_200 = []

    for line in sys.stdin:
        if parsing_manager.process_line(line):
            if parser.get_attribute(Attribute.STATUS_CODE, line) == 200:
                lines_with_200.append(line)

    printer.automatic_print_task_result(
        "e",
        " Funkcja, która wypisuje na wyjście standardowe tylko wiersze z kodem odpowiedzi 200.",
        f"Theese are them lines with 200 status: {"\n".join(lines_with_200)}",
        parsing_manager.list_of_err,
        parsing_manager.lines_read,
        5
    )


if __name__ == "__main__":
    main()