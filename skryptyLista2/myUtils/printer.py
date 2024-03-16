import sys


def print_task_result(task_index, task_name, task_value):
    print("------------------------------------------\n" +
          task_index +
          ".\n" +
          task_name +
          ": \n\n" +
          str(task_value) +
          "------------------------------------------\n"
          )


def prettify_task_value(most_relevant_info, errors, num_of_lines, error_limit):
    errors_to_string = ""
    for errPair in errors[:error_limit]:
        errors_to_string += f"Invalid line: {errPair[0]}, {errPair[1]} has been thrown\n"

    return (most_relevant_info+"\n\nAmmount of lines: " +
            str(num_of_lines)+f"\n\nList of errors({len(errors)}) in lines: \n"+errors_to_string)


def automatic_print_task_result(task_index, task_name, most_relevant_info, errors, num_of_lines, error_limit):
    print_task_result(task_index, task_name, prettify_task_value(most_relevant_info, errors, num_of_lines, error_limit))


def stdout_print(**kwargs):
    for description, content in kwargs.items():
        print(f"{description}: \n{content}\n")