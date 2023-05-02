def interval_scheduling(events):
    # Remove events with invalid duration
    valid_events = []
    invalid_events = []
    for start, end in events:
        if start < end:
            valid_events.append((start, end))
        else:
            invalid_events.append((start, end))
            print(f"Invalid event: {start}-{end}. Start time should be less than end time.")
    # Sort valid events in ascending order of their ending times
    sorted_events = sorted(valid_events, key=lambda x: x[1])
    # Initialize variables
    count = 0
    last_end_time = 0
    selected_events = []
    num_swaps = 0
    # Loop through events
    for event in sorted_events:
        # If event can be scheduled, select it and update variables
        if event[0] >= last_end_time:
            count += 1
            last_end_time = event[1]
            selected_events.append(event)
        # Keep track of the number of swaps
        if sorted_events.index(event) != valid_events.index(event):
            num_swaps += 1    
    # Return maximum number of events that can be scheduled, the selected events, and the number of swaps
    return count, selected_events, num_swaps, invalid_events

events = [(1, 3), (2, 5), (13, 9), (6, 8)]
max_events, selected_events, num_swaps, invalid_events = interval_scheduling(events)
print("Total events that can be done: ", max_events)
print(selected_events)
print("Total swaps that are done: ", num_swaps)
print("Invalid events: ", invalid_events)
