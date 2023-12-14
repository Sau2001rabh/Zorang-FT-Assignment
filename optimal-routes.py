import math, requests

#calculate the distance between point 'a' and point 'b'
def distance(a,b):
    x1,y1 = a[0],a[1]
    x2,y2 = b[0],b[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#Get data from url
response = requests.get("https://zorang-recrutment.s3.ap-south-1.amazonaws.com/addresses.json")
response = response.json() 

order = []
for i in response:
    order.append([i["latitude"],i["longitude"],i["_id"]])

#Location of store
x_store = 28.9428
y_store = 77.2276

#Binary search to minimize the total distance covered by delivery agents.
start = 0
end = 10**10
deliveries = []
while(start<=end):
    mid = start+(end-start)/2
    currorder = [[] for i in range(10)]
    def check(mid):
        total = 0
        curr = []
        for i in order:
            curr.append(i)
        sumDistance = 0
        a, b = x_store, y_store
        while(total<10 and len(curr)>0):
            dist = []
            index = 0
            for i,j,k in curr:
                dist.append([distance([i,j],[a,b]),i,j,k,index])
                index+=1
            dist.sort()
            sumDistance+=dist[0][0]
            finalDistance = distance([x_store,y_store],[dist[0][1],dist[0][2]])
            if sumDistance+finalDistance<=mid:
                a,b = dist[0][1],dist[0][2]
                currorder[total].append(dist[0][3])
                curr.pop(dist[0][4])
            else:
                total+=1
                sumDistance = 0
                a,b =  x_store,y_store
        if len(curr)==0:
            return currorder
        else:
            return False
    if check(mid): #delivery possible, copy order of deliveries 
        deliveries = currorder.copy()
        end = mid-1
    else:
        start = mid+1

remaining = 0
for i in deliveries:
    if len(i)==0:
        remaining+=1
l = []
for i in range(len(deliveries)):
    if remaining==0:
        break
    while(len(deliveries[i])>1 and remaining>0):
        l.append(deliveries[i].pop())
        remaining-=1
for i in range(len(deliveries)):
    if deliveries[i]==[]:
        deliveries[i].append(l.pop()) 

#Printing the Order of deliveries
print(deliveries) 
