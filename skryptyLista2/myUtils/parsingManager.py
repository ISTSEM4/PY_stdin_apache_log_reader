import sys
import myUtils.apacheLogParser as parser
from myUtils.lineAttributes import Attribute


class ParsingManager:
    def __init__(self):
        self.lines_read = 0
        self.list_of_err = []
        self.last_tuple_read = None

    def process_line(self, line):
        self.lines_read += 1

        try:
            parser.validate_line(line)

        except TypeError as e:
            # we remember all errors with their description
            self.list_of_err.append((line, e.args[0]))

            return False

        else:
            self.last_tuple_read = parser.turn_line_to_tuple(line)

            return True
