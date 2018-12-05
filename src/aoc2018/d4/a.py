import operator

from collections import namedtuple
from datetime import datetime

from aoc2018.data import load_input

AWAKE = "awake"
ASLEEP = "asleep"
OFFDUTY = "offduty"
GUARDS = dict()

Event = namedtuple('Event', ['guard', 'state', 'timestamp'])

class Guard(object):


    def __init__(self, id):
        self.id = id
        self.state = None
        self.state_at = None
        self.total_minutes_asleep = 0
        self.minutes_asleep_tallies = {m: 0 for m in range(60)}

    def apply_tallies(self, minutes):
        for minute in minutes:
            self.minutes_asleep_tallies[minute] += 1

    def awake(self, timestamp):
        if self.state is ASLEEP:
            asleep_for = int((timestamp - self.state_at).seconds/ 60)
            self.apply_tallies(range(self.state_at.minute, self.state_at.minute + asleep_for))
            self.total_minutes_asleep += asleep_for
        self.state = AWAKE
        self.state_at = timestamp

    def asleep(self, timestamp):
        self.state = ASLEEP
        self.state_at = timestamp

    def get_most_sleepy_minute(self):
        return max(self.minutes_asleep_tallies.items(), key=operator.itemgetter(1))


def get_guard(id):
    if id not in GUARDS:
        GUARDS[id] = Guard(id)
    return GUARDS[id]

def parse_timestamp(timestamp_value):
    return datetime.strptime(timestamp_value, '[%Y-%m-%d %H:%M]')

def get_most_sleepy():
    most_sleepy = None

    for guard in GUARDS.values():
        if most_sleepy is None:
            most_sleepy = guard
            continue
        if guard.total_minutes_asleep > most_sleepy.total_minutes_asleep:
            most_sleepy = guard

    return most_sleepy

def load_events():
    events = load_input(__file__)
    events.sort()
    return events

def process_events():
    current_guard = None

    for value in load_events():
        parts = value.split()
        timestamp = parse_timestamp(" ".join(parts[0:2]))

        if 'begins shift' in value:
            id = int(parts[3].replace("#", ""))
            current_guard = get_guard(id)

        if 'begins shift' in value or 'wakes up' in value:
            current_guard.awake(timestamp)
        elif 'falls asleep' in value:
            current_guard.asleep(timestamp)


def main():
    process_events()
    most_sleepy = get_most_sleepy()
    minute, _ = most_sleepy.get_most_sleepy_minute()
    print(most_sleepy.id * minute)

if __name__ == "__main__":
    main()
