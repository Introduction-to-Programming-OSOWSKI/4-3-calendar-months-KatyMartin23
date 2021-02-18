def calender (m):
    for i in range(0, 12):
        if m == months[i]:
            return i + 1
    return m + " is not a planet"

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

print (calender("hello"))

