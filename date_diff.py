import datetime
ret = list(map(int,input().split(" ")))
due = list(map(int,input().split(" ")))
date_ret = datetime.datetime(ret[2],ret[1],ret[0])
date_due = datetime.datetime(due[2],due[1],due[0])

diff_days = (date_ret-date_due).days
diff_months = date_ret.month-date_due.month
diff_years = date_ret.year-date_due.year
print(diff_days,diff_months,diff_years)
if(diff_days > 0):
    if (diff_years > 0):
        print(10000)
    elif (diff_months > 0):
        print(diff_months * 500)
    else:
        print(diff_days * 15)
else:
    print(0)
