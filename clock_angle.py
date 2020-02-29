'''
Write a function to calculate the smaller angle between the two handles of an analog clock,
given the hour and minute values.
Example input: (3, 20)
Expected output: 30
'''


def time_input_angle_output(hours_and_minutes_input):

    hours_and_minutes = ''.join(str(hours_and_minutes_input).split())

    if hours_and_minutes[0] == '0':
        hours_and_minutes = hours_and_minutes[1:]
    else:
        hours_and_minutes = hours_and_minutes

    hour_int = int(hours_and_minutes.split(':')[0])
    if hour_int > 12:
        hour_int = 24 - hour_int
    else:
        hour_int = hour_int
    # print(hours_and_minutes)

    minute_int = int(hours_and_minutes.split(':')[1])

    hour_degree = hour_int * 30

    minute_degree = minute_int * 6

    # optional: account for how many degrees the hour hand moves every minute
    # hour_degree = hour_degree + minute_degree * .083333333
    # print(round(hour_degree, 1))

    if abs(hour_degree - minute_degree) >= 180:
        return round(360 - abs((hour_degree - minute_degree)), 1)
    else:
        return round(abs(hour_degree - minute_degree), 1)


user_time_input = input('Enter the time (ex: 2:34) as integers with a ":" in between: ')

smaller_angle = time_input_angle_output(user_time_input)

print(smaller_angle)
