import re


result_regex = r"^(.*) INFO: Informed scheduler that task (.*) has status\s+ (DONE|FAILED)"
starting_regex = r"^(.*) INFO: \[pid \d+\] Worker Worker(.*) running\s\s\s(.*)"

with open('ignored/puppet.log') as log_file:
    for log_line in log_file:
        m = re.search(starting_regex, log_line)
        if m:
            print(m.group(0))
        m = re.search(result_regex, log_line)
        if m:
            print(m.group(0))
