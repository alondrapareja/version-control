import datetime
def print_time(path):
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(path,'a') as file:
        file.write(current_datetime + '\n')

print_time('/repo/version-control/docs/version.md')