# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    if value > limit:
       status = "OVER LIMIT" 
    else:
       status="OK"
    return status

status=check(87, 100)

print(status)
