'''
Given an array of time intervals (start, end)
for classroom lectures (possibly overlapping), 
find the minimum number of rooms required
'''

def numRooms(intervals):
    startTime = []
    endTime = []
    for start, end in intervals:
        startTime.append(start)
        endTime.append(end)
    startTime.sort()
    endTime.sort()
    i = 1
    j = 0
    roomNeeded = 1
    result = 1
    while i < len(startTime) and j < len(endTime):
        if startTime[i] <= endTime[j]:
            roomNeeded += 1
            i += 1
            if roomNeeded > result:
                result = roomNeeded
        else:
            roomNeeded -= 1
            j += 1 

    return result

print(numRooms([(30, 75), (0, 50), (60, 150)]))
print(numRooms([(30, 75), (0, 50), (10, 60), (60, 150)]))
print(numRooms([(900, 910), (940, 1200), (950, 1120), (1100, 1130), (1500, 1900), (1800, 2000)])) 
print(numRooms([(60, 150), (150, 170)]))
print(numRooms([(60, 150), (60, 150), (150, 170)]))