from collections import deque


def first_non_repeating_letter(string_stream):
    frequency = {}
    queue = deque()
    for stream in string_stream:
        if stream not in frequency.keys():
            frequency[stream] = 1
        else:
            frequency[stream]+= 1
        queue.append(stream)
        while len(queue)!=0 and frequency[queue[0]]>1:
              queue.popleft()
        if len(queue)==0:
            print(-1,end=" ")
        else:
            print(queue[0],end=" ")


first_non_repeating_letter("aabccxb")
    