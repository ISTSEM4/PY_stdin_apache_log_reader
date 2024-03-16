import ipaddress
import re
from lineAttributes import Attribute

# index of split words: 0       1 2             3               4         5        6         7             8        9
# a valid line has:{ip/address} - - {[DAY/MON/DD/YYYY:HH:MM:SS INT]} {"HTTPmthd + dir + HTTPversion"} returnedInfo INT


def is_valid_domain_or_ip(address):
    # Regular expression for validating domain address
    pattern = r"^(?:(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$"
    try:
        ipaddress.ip_address(address)
    except ValueError:
        return re.match(pattern, address) is not None
    else:
        return True


def is_valid_date_format(date_str):
    # Define regular expression pattern for the specified format
    pattern = r"\[\d{2}/(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}:\d{2}:\d{2}:\d{2} [-+]\d{4}\]"
    return re.match(pattern, date_str) is not None


def is_valid_name_format(name_str):
    return True


def is_valid_httpmthd_dir_httpversion_format(http_str):
    pattern = r'"(?:GET|POST|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH) ([^\s]+) HTTP/\d\.\d"'
    return re.match(pattern, http_str) is not None


def is_valid_http_response(response_str):
    pattern = (r"(?:100|101|102|103|200|201|202|203|204|205|206|207|208|226|300|301|302|303|304|305|306|307|308|400"
               r"|401|402|403|404|405|406|407|408|409|410|411|412|413|414|415|416|417|418|421|422|423|424|425|426|428"
               r"|429|431|451|500|501|502|503|504|505|506|507|508|510|511)")

    return re.match(pattern, response_str) is not None


def is_valid_bitnumber(bit_amm_str):
    pattern = r"^[0-9]+$"
    return re.match(pattern, bit_amm_str) is not None


def validate_line(line):
    line_divided = line.split(" ")

    if len(line_divided) != 10:
        raise TypeError("Incorrect ammount of parameters")

    if not is_valid_domain_or_ip(line_divided[0]):
        raise TypeError("Incorrect domain/ip")

    if not (is_valid_name_format(line_divided[1]) and is_valid_name_format(line_divided[2])):
        raise TypeError("Incorrect name/s")

    if not is_valid_date_format(line_divided[3] + " " + line_divided[4]):
        raise TypeError("Incorrect date format")

    if not is_valid_httpmthd_dir_httpversion_format(line_divided[5] + " " + line_divided[6] + " " + line_divided[7]):
        raise TypeError("Incorrect http mthd or dir or http version")

    if not is_valid_http_response(line_divided[8]):
        raise TypeError("Incorrect http response code")

    if not is_valid_bitnumber(line_divided[9]):
        raise TypeError("Incorrect bitnumber")


def get_time(line):
    return line[line.find(":") + 1:line.find(":") + 9]


def get_date(line):
    return line[line.find("[") + 1:line.find("[") + 17]


def get_time_zone(line):
    return line[line.find("[") + 26:line.find("]")]


def get_http_method(line):
    return re.search(r'"([A-Z]+)\s', line).group(1)


def get_path_info(line):
    return line[line.index(" ", line.find('"')) + 1:line.index(" ", line.index(" ", line.find('"')) + 1)]


def get_http_version(line):
    pass


def get_format_of_pulled(line):
    return get_path_info(line)[line.rfind(".") + 1:]


def is_pulled_visual_format(line):
    pattern = r"(?:gif|jpg|jpeg|xbm)"
    return re.search(pattern, line) is not None

def get_attribute(attrinute: Attribute, line):
    match attrinute.value:
        case 1:
            return line.split(" ")[0]
        case 2:
            return line.split(" ")[1]
        case 3:
            return line.split(" ")[2]
        case 4:
            return get_time(line)
        case 5:
            return get_date(line)
        case 6:
            return get_time_zone(line)
        case 7:
            return get_http_method(line)
        case 8:
            return get_path_info(line)
        case 9:
            return get_http_version(line)
        case 10:
            return line.split(" ")[8]
        case 11:
            return line.split(" ")[9]
