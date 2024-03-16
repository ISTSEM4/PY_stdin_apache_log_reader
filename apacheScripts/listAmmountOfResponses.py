# a. Funkcja, która wypisuje na wyjście standardowe liczbę żądań z kodem:
# a. 200,
# b. 302
# c. 404.

import sys
from myUtils import apacheLogParser as parser, printer
from myUtils.lineAttributes import Attribute
from myUtils.parsingManager import ParsingManager


def main():
    parsing_manager = ParsingManager()
    # each element in list is the ammount of corresponding http status code in match case
    list_of_responses = [0, 0, 0]

    for line in sys.stdin:
        if parsing_manager.process_line(line):
            match int(parser.get_attribute(Attribute.STATUS_CODE, line)):
                case 200:
                    list_of_responses[0] += 1
                case 302:
                    list_of_responses[1] += 1
                case 404:
                    list_of_responses[2] += 1

    printer.automatic_print_task_result(
        "a",
        "Funkcja, która wypisuje na wyjście standardowe liczbę żądań z kodem",
        f"a. {list_of_responses[0]}\nb. {list_of_responses[1]}\nc. {list_of_responses[2]}",
        parsing_manager.list_of_err,
        parsing_manager.lines_read,
        5
    )


if __name__ == "__main__":
    main()