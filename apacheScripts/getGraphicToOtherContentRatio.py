#d. Funkcja, wypisująca stosunek pobrań grafiki (zasoby kończące się na *.gif, *.jpg, *.jpeg,
# *.xbm) do pozostałych zasobów.

import sys
from myUtils import apacheLogParser as parser, testUseful, printer
from myUtils.lineAttributes import Attribute
from myUtils.parsingManager import ParsingManager


def main():
    parsing_manager = ParsingManager()

    lines_in_visual_format = 0

    for line in sys.stdin:
        if parsing_manager.process_line(line):
            if parser.is_pulled_visual_format(line):
                lines_in_visual_format += 1

    the_ratio = round(lines_in_visual_format / (parsing_manager.lines_read - lines_in_visual_format), 2)

    printer.automatic_print_task_result(
        "d",
        """Funkcja, wypisująca stosunek pobrań grafiki (zasoby kończące się na *.gif, *.jpg, *.jpeg,
    # *.xbm) do pozostałych zasobów.""",
        f"The visual content to non visual content ratio is: {the_ratio} v/nonv",
        parsing_manager.list_of_err,
        parsing_manager.lines_read,
        5
    )


if __name__ == "__main__":
    main()