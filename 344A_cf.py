import sys

def magnets():
    input = sys.stdin.read
    data = input().splitlines()
    count = 1  # Start with 1 because the first group always exists
    previous_last_char = data[1][1]

    for i in range(2, len(data)):
        if previous_last_char != data[i][0]:  # Check if the end of one magnet group differs from the start of the next
            count += 1
        previous_last_char = data[i][1]

    sys.stdout.write(str(count) + "\n")

magnets()