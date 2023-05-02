def activity_selection(start_times, finish_times):
    n = len(start_times)
    activities = list(zip(start_times, finish_times))
    activities.sort(key=lambda x: x[1]) # sort activities by finish time
    
    selected_activities = []
    last_finish_time = -1
    
    for i in range(n):
        if activities[i][0] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]
    
    return selected_activities

def main():
    start_times = [1, 3, 0, 5, 8, 5]
    finish_times = [2, 4, 6, 7, 9, 9]

    selected_activities = activity_selection(start_times, finish_times)
    
    print("Selected Activities:")
    for activity in selected_activities:
        print("Start Time:", activity[0], "\tFinish Time:", activity[1])

if __name__ == "__main__":
    main()
