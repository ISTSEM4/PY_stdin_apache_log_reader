# g. Funkcja, które wypisuje na wyjście standardowe tylko zasoby pobierane w piątek.

import sys
from myUtils import apacheLogParser as parser, testUseful, printer
from myUtils.lineAttributes import Attribute
from myUtils.parsingManager import ParsingManager
import datetime


def main():
    parsing_manager = ParsingManager()

    friday_requests = []

    for line in sys.stdin:
        if parsing_manager.process_line(line):
            date = datetime.datetime.strptime(parser.get_attribute(Attribute.DATE, line), "%d/%b/%Y")
            if date.weekday() == 4:
                friday_requests.append(line)

    printer.automatic_print_task_result(
        "f",
        "Funkcja, która wypisuje na wyjście standardowe zasoby pobierane pomiędzy 22 a 6 rano.",
        f"Theese are them lines requested at fridays: {"\n".join(friday_requests)}",
        parsing_manager.list_of_err,
        parsing_manager.lines_read,
        5
    )


if __name__ == "__main__":
    main()