def partition(distance, left, right, mid):
    idx = left
    newpos = 0

    print "in"
    for i in range(len(distance)):
        print distance[i]
    print mid, left, right
    for i in range(left, right+1):
        if distance[i][0] <= distance[mid][0]:
            distance[i], distance[idx] = distance[idx], distance[i]
            if  i == mid:
                newpos = idx
            idx += 1

    idx -= 1
    print idx, newpos
    distance[idx], distance[newpos] = distance[newpos], distance[idx]

    return idx




def quicksortk(distance, left, right, k):
    while left <= right:
        mid = left + (right-left)/2
        pivotIndex = partition(distance,left, right , mid)
        if pivotIndex == k:
            return
        elif pivotIndex > k:
            right = pivotIndex -1
        else:
            left = pivotIndex + 1

    return



def findKclosest(l, point, k):
    if not l or not point:
        return []

    distance = []
    for i in range(len(l)):
        distance.append([(pow(l[i][0]-point[0], 2)+ pow(l[i][1]-point[1], 2)), i])

    left = 0
    right = len(distance) -1
    quicksortk(distance, left, right, k)
    ret = []
    for i in range(k):
        ret.append(l[distance[i][1]])

    return ret

print findKclosest([[0, 0], [1, 1], [2, 1], [1, 2], [3, 3]], [1, 1], 3)
