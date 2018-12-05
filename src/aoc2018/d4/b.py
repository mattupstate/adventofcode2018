from aoc2018.d4.a import GUARDS, process_events

def main():
    process_events()
    sleepiest_minute, count = 0, 0
    sleepiest_guard = None
    for guard in GUARDS.values():
        for m, c in guard.minutes_asleep_tallies.items():
            if c > count:
                sleepiest_minute = m
                count = c
                sleepiest_guard = guard
    print(sleepiest_guard.id * sleepiest_minute)

if __name__ == "__main__":
    main()
