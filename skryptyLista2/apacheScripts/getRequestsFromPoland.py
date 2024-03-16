# h. Funkcja, która wypisuje na wyjście standardowe tylko żądania z Polski (tzn. hostów z
# nazwą domenową kończącą się .pl).

import sys
from myUtils import apacheLogParser as parser, testUseful, printer
from myUtils.lineAttributes import Attribute
from myUtils.parsingManager import ParsingManager


def main():
    parsing_manager = ParsingManager()

    requests_from_poland = []

    for line in sys.stdin:
        if parsing_manager.process_line(line):
            remote_host = parser.get_attribute(Attribute.REMOTE_HOST, line)
            if remote_host[remote_host.rfind(".") + 1:] == "pl":
                requests_from_poland.append(line)

    printer.automatic_print_task_result(
        "f",
        """h. Funkcja, która wypisuje na wyjście standardowe tylko żądania z Polski (tzn. hostów z
    nazwą domenową kończącą się .pl).""",
        f"Theese are them lines requested from Poland: {"\n".join(requests_from_poland)}",
        parsing_manager.list_of_err,
        parsing_manager.lines_read,
        5
    )


if __name__ == "__main__":
    main()
