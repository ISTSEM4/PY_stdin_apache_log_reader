import sys
import apacheLogParser as parser


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
            return True

