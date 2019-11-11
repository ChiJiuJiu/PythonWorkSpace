count=0

def   move(n,X,Y,Z):
    if n==0:
        return
    global  count
    move(n-1,X,Z,Y)
    count+=1
    print('the {0} time,current n={1},move {2}->{3}'.format(count,n,X,Z))

    move(n-1,Y,X,Z)


if __name__ == '__main__':
    move(11,'X','Y','Z')