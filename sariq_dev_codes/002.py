# n = 5
# for a in range(n):
#     print(str(a+1)[::],end='')
xrange = []
for t in xrange(int(input())):
    try:
        a,b = map(int,raw_input().split())
        print(a/b)
    except ZeroDivisionError as e:
        print('Error Code: %s' %e)
    except ValueError as e:
        print('Error Code: %s' %e)
