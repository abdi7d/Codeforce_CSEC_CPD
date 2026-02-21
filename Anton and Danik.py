n = int(input())
s = input().strip()

# count how many times 'A' and 'D' appear
a_wins = s.count('A')
d_wins = s.count('D')

if a_wins > d_wins:
    print("Anton")
elif d_wins > a_wins:
    print("Danik")
else:
    print("Friendship")
