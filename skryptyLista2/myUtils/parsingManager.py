import sys
import myUtils.apacheLogParser as parser
from myUtils.lineAttributes import Attribute

class ParsingManager:
    def __init__(self):
        self.lines_read = 0
        self.list_of_err = []

    def process_line(self, line):
        self.lines_read += 1

        try:
            parser.validate_line(line)

        except TypeError as e:
            # we remember all errors with their description
            self.list_of_err.append((line, e.args[0]))
            return False

        else:
            tuple_to_be = []
            for attribute in Attribute:
                tuple_to_be.append(parser.get_attribute(attribute, line))
            return tuple(tuple_to_be)

