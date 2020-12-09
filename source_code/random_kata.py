def snail(a):

     start=0
     end=len(a)-1

     x=0
     y=-1


     res=[]
     while start<=end:
        while y<end:
            y+=1
            res.append(a[x][y])

        while x<end:
            x+=1
            res.append(a[x][y])

        while  y>start:
            y-=1
            res.append(a[x][y])

        while x>start+1:
            x -= 1
            res.append(a[x][y])

        start += 1
        end -=1
     return (res)

a= [
    [1, 2, 3, 4 ],
    [5, 6, 7, 8 ],
    [9, 10,11,12],
    [13,14,15,16]
    ]

print(snail(a))

a= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
   ]
print(snail(a))
