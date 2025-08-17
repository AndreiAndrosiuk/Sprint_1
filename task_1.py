time = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0

time_values = time.split(',')

for values in time_values:

    time_parts = values.split()

    for part in time_parts:

        if 'h' in part:
            total_minutes += int(part.replace('h', '')) * 60

        elif 'm' in part:
            total_minutes += int(part.replace('m', ''))

        elif 's' in part:
            seconds = int(part.replace('s', ''))

            if seconds % 60 == 0:
                total_minutes += seconds // 60

print(total_minutes)