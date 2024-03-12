# a. Funkcja, która wypisuje na wyjście standardowe liczbę żądań z kodem:
# a. 200,
# b. 302
# c. 404.

import sys
import apacheLogParser as parser
import lineAttributes
import printer

list_of_responses = [0, 0, 0]
list_of_err = []
num_of_lines = 0

for line in sys.stdin:
    try:
        num_of_lines += 1
        parser.validate_line(line)
    except TypeError as e:
        # we remember all errors with their description
        list_of_err.append((line, e.args[0]))
    else:
        match int(parser.get_attribute(lineAttributes.Attribute.STATUS_CODE, line)):
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
    list_of_err,
    num_of_lines,
    5
)

