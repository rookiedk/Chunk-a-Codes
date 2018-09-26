#Given a list of intervals, output the number repeated the maximum number of times

sched = [(6,8), (6,12), (6,7), (7,8), (7,10), (8,9), (8,10), (9,12),
         (9,10), (10,11), (10, 12), (11, 12)]
sched2 = [(6.0,8.0), (6.5,12.0), (6.5,7.0), (7.0,8.0), (7.5,10.0), (8.0,9.0), (8.0,10.0), (9.0,12.0),
         (9.5,10.0), (10.0,11.0), (10.0, 12.0), (11.0, 12.0)]

def valueRepeatMaximum(schedule):
    
    #convert schedule to list of start/end marked as such
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))
    #Sort the list of times
    times.sort()
    maxcount, time = chooseVal(times)
    print "Number found most often in the list was ", time, "and it was repeated", maxcount, "times"

def chooseVal(times):
    rcount = 0
    maxcount = 0
    time = 0
    #Range through the times computing a running count of numbers
    for t in times:
        if t[1] == 'start':
            rcount = rcount + 1
        elif t[1] == 'end':
            rcount = rcount - 1
        if rcount > maxcount:
            maxcount = rcount
            time = t[0]
        
    return maxcount, time


valueRepeatMaximum(sched)
