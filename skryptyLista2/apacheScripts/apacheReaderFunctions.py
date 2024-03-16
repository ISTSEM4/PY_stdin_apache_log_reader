import sys
import os

# Add the parent directory of the script to the Python path
script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(project_dir)

from myUtils.parsingManager import ParsingManager as parMan
from myUtils import apacheLogParser as parser
from myUtils.lineAttributes import Attribute
from itertools import groupby
from datetime import datetime
from myUtils import printer
from myUtils import testUseful


def read_log():
    parsing_manager = parMan()
    list_of_entries = []
    for line in sys.stdin:
        if parsing_manager.process_line(line):
            list_of_entries.append(parsing_manager.last_tuple_read)

    return list_of_entries, parsing_manager


def _read_log(string):
    list_of_entries = []
    string_split = string.splitlines()
    for line in string_split:
        try:
            parser.validate_line(line)
        except TypeError:
            pass
        else:
            list_of_entries.append(parser.turn_line_to_tuple(line))

    return list_of_entries


def sort_log(list_of_entries, attribute: Attribute = Attribute.STATUS_CODE):
    # key is the value that is compared
    list_of_entries.sort(key=lambda entry: entry[attribute.value - 1])


def get_entries_by_addr(list_of_entries, addr):
    if not parser.is_valid_domain_or_ip(addr):
        raise ValueError("Invalid address!!")

    return [entry for entry in list_of_entries if entry[Attribute.REMOTE_HOST.value - 1] == addr]


def get_entries_by_code(list_of_entries, code):
    if not parser.is_valid_http_response(code):
        raise ValueError("Invalid code!!")

    return [entry for entry in list_of_entries if entry[Attribute.STATUS_CODE.value - 1] == code]


def get_failed_reads(list_of_entries, divide_into_4xx_and_5xx=False):
    entries_in_4xx_format = [entry for entry in list_of_entries if
                             entry[Attribute.STATUS_CODE.value - 1].startswith('4')]
    entries_in_5xx_format = [entry for entry in list_of_entries if
                             entry[Attribute.STATUS_CODE.value - 1].startswith('5')]
    if divide_into_4xx_and_5xx:
        return entries_in_4xx_format, entries_in_5xx_format

    else:
        return entries_in_4xx_format + entries_in_5xx_format


def get_entries_by_extension(list_of_entries, extension):
    return [entry for entry in list_of_entries
            if extension == parser.get_format_of_path(entry[Attribute.PATH_INFO.value - 1])]


def print_entries(list_of_entries):
    print(list_of_entries)


def entry_to_dict(entry: tuple):
    return {Attribute(index + 1).name: attribute for index, attribute in enumerate(entry)}


def log_to_dict(list_of_entries):
    entries_mapped = []
    for entry in list_of_entries:
        y = entry_to_dict(entry)
        entries_mapped.append(y)
    x = lambda entry_mapped: entry_mapped[Attribute.REMOTE_HOST.name]
    groups = groupby(entries_mapped, x)
    return {key: list(value) for key, value in groups}


def get_addrs(addres_to_entries_mapped: dict):
    return addres_to_entries_mapped.keys()


def print_dict_entry_dates(address_to_entries_mapped):
    # user_info has (address, requests_number, first_request, last_request, 200_to_all_requests_ratio)

    for address, mapped_entry_group in address_to_entries_mapped.items():
        user_info = [
            address,
            len(mapped_entry_group),
            get_earliest_entry(mapped_entry_group),
            get_latest_entry(mapped_entry_group),
            get_200_to_rest_ratio(mapped_entry_group)
        ]
        printer.stdout_print(
            HOST_NAME=user_info[0],
            REQUEST_AMMOUNT=user_info[1],
            FIRST_ENTRY_DATE=user_info[2],
            LAST_ENTRY_DATE=user_info[3],
            RATIO_200_TO_REST=user_info[4]
        )


def get_200_to_rest_ratio(mapped_entries_group):
    amm_of_200_requests = 0
    all_req = 0
    for mapped_entry in mapped_entries_group:
        if mapped_entry[Attribute.STATUS_CODE.name] == 200:
            amm_of_200_requests += 1
        all_req += 1

    return amm_of_200_requests / all_req


def get_earliest_entry(mapped_entry_group):
    earliest_entry = mapped_entry_group[0]

    for mapped_entry in mapped_entry_group:
        if mapped_entry[Attribute.DATE.name] < earliest_entry[Attribute.DATE.name] and mapped_entry[
            Attribute.TIME.name] < earliest_entry[Attribute.TIME.name]:
            earliest_entry = mapped_entry

    return datetime.combine(earliest_entry[Attribute.DATE.name], earliest_entry[Attribute.TIME.name])


def get_latest_entry(mapped_entry_group):
    latest_entry = mapped_entry_group[0]

    for mapped_entry in mapped_entry_group:
        if mapped_entry[Attribute.DATE.name] > latest_entry[Attribute.DATE.name] and mapped_entry[Attribute.TIME.name] > \
                latest_entry[Attribute.TIME.name]:
            latest_entry = mapped_entry

    return datetime.combine(latest_entry[Attribute.DATE.name], latest_entry[Attribute.TIME.name])


if __name__ == '__main__':
    # log_as_list = read_log()[0]
    # sort_log(log_as_list)
    # d = log_to_dict(log_as_list)
    # print_dict_entry_dates(d)
    strang = testUseful.get_light_NASA()
    log_as_list = _read_log(strang)
    sort_log(log_as_list)
    d = log_to_dict(log_as_list)
    print_dict_entry_dates(d)
