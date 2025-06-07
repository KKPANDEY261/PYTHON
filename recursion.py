
#recursive function
def help(n):
    if n == 0:
        return
    print(n)
    help(n-1)
help(10)