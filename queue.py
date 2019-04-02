# Enter your code here. Read input from STDIN. Print output to STDOUT
# N will be the number of queries
N = int(input())
# l will be the list
l =[]
# Operations of the individual queries
for i in range(0,N):
    # Reading of the queries user
    l1= list(map(int,input().split()))
    # If queue is the "1" enqueue element x into the end of the queue.
    if l1[0]==1:
        l.append(l1[1])
    # If queue is the "2" dequeue element x into the front of the queue.
    elif l1[0]==2:
        l.pop(0)
    # If queue is the "3" print the element at the front of the queue
    else:
        print(l[0])
    
