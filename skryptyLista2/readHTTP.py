import sys
import apacheLogParser as parser
import lineAttributes
import printer

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


printer.automatic_print_task_result(
    "a.",
    ,
,
    list_of_err,
    num_of_lines,
    5
)