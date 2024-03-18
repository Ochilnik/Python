""" #!/usr/bin/env python3 """
import re
import operator
import csv

# Create empty dictionsry
error = {}
sorterror = {}
per_user = {}
sper_user = {}

#Reading log file
f = open('syslog.log')
loglines = f.readlines()
f.close()
#print(loglines)

#Sort loglines on errors
for logline in loglines:
    if re.search(r"ERROR ", logline):
        #Determinate name of errors
        i = logline.rindex(r"ERROR ")
        log1 = logline[i:]
        log2 = log1.replace("ERROR ", "")
        log3 = re.sub(r" \(\w.*\)\n", "", log2)
        if log3 not in error:
            error[log3] = 0
        error[log3] += 1
sorterror = sorted(error.items(), key=operator.itemgetter(1),  reverse=True)        
error = sorterror
#print(error)

#Sort loglines on users
i = 0
e = 0
for logline in loglines:
    #Determinate name of user
    lng = re.search(r"\(\w.*\)", logline)
    long = lng[0]
    user = long[1:-1]
    #Count errors
    if user not in per_user:
        per_user[user] = 0, 0
    i, e = per_user[user]
    if re.search(r"ERROR", logline):
        e += 1
    if re.search(r"INFO", logline):          
        i += 1
    per_user[user] = i, e

sper_user = sorted(per_user.items(), key=operator.itemgetter(0),  reverse=False)
per_user = sper_user
# print(per_user)

#Write error_message.csv
with open('error_message.csv', 'w', newline='') as csvfile1:
    ewriter = csv.writer(csvfile1) #, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    ewriter.writerow(['Error', 'Count'])
    ewriter.writerows(error)

#Write user_statistics.csv
lst = []
with open('user_statistics.csv', 'w', newline='') as csvfile2:
    ewriter = csv.writer(csvfile2, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    ewriter.writerow(['Username', 'INFO', 'ERROR'])
    
    for lst in per_user:
        key, val = lst
        i, e = val
        ewriter.writerow([key, i, e])



#re.sub(r"'\(|\)'", "",
#sorterror = sorted(error.items(), key=operator.itemgetter(1),  reverse=True)        
#error = sorterror
#print(error)
#log1, log2, log3 = logline.rpartition(':')
# re.search(r"ticky: INFO: ([\w ]*) ", line)
# re.search(r"ticky: ERROR: ([\w ]*) ", line)
# sorted(fruit.items())
# sorted(fruit.items(), key=operator.itemgetter(0))
# sorted(fruit.items(), key=operator.itemgetter(1))
# sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)
#sper_user_i = sorted(per_user_i.items(), key=operator.itemgetter(0),  reverse=False)
#per_user_i = sper_user_i
#print(per_user_i)

"""
#Sort loglines on users
for logline in loglines:
    #Determinate name of user
    lng = re.search(r"\(\w.*\)", logline)
    long = lng[0]
    user = long[1:-1]
    #Count errors
    if re.search(r"ERROR", logline):          
        if user not in per_user_e:
            per_user_e[user] = 0
        per_user_e[user] += 1
    #Count info
    if re.search(r"INFO", logline):          
        if user not in per_user_i:
            per_user_i[user] = 0
        per_user_i[user] += 1
sper_user_e = sorted(per_user_e.items(), key=operator.itemgetter(0),  reverse=False)
per_user_e = sper_user_e
sper_user_i = sorted(per_user_i.items(), key=operator.itemgetter(0),  reverse=False)
per_user_i = sper_user_i

print(per_user_e)
print(per_user_i)
"""