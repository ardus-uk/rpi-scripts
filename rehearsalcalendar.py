from datetime import datetime as dt
import datetime

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

firstrehearsal = "07/09/23"

dtfr = dt.strptime(firstrehearsal, "%d/%m/%y")

d = datetime.timedelta(days=7)
nxt = dtfr

for y in range(52):
    print ('* '+custom_strftime('%A, %B {S}, %Y', nxt))
    nxt = d+nxt