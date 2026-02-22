username = input().strip()

# Count distinct characters using a set
distinct_count = len(set(username))

if distinct_count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
