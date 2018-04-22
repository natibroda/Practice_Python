# This programme simulates NHS STP recruitment system - candidates are presented with a corresponding interview score 
# and a list of locations in order of preference. Highest scoring candidate gets their first location preference, next one gets their 
# first location preference, unless it's already taken, then they get their second choice etc.
# Once all locations are filled applicants are added to the reserve list.


# dictionary
candidates = {
'Anna': [41, ['Newcastle', 'Leeds', 'Birmingham']],
'Mark': [45, ['London', 'Cambridge', 'Birmingham']],
'Steven': [38, ['Cambridge', 'London', 'Sheffield', 'Leeds', 'Newcastle']],
'Natalia': [40, ['Newcastle', 'Leeds', 'Cambridge', 'Birmingham', 'Sheffield']],
'Amanda': [43, ['Cambridge', 'London', 'Birmingham', 'Leeds']],
'Tracy': [44, ['London', 'Cambridge', 'Birmingham']],
'Alex': [42, ['London', 'Cambridge', 'Birmingham', 'Sheffield', 'Leeds',
'Newcastle']]
}

# store scores in a list to sort them
scores = []
for candidate in candidates:
    score = candidates[candidate][0]
    scores.append(candidates[candidate][0])

# print(sorted(scores))

# loop through candidates & find the highest score
# rank candidates according to score and store in a list from highest to
# lowest rank - count is used to iterate through all candidates in dictionary

lowest_to_highest = sorted(scores)
ranking = []
count = 0

while count < len(candidates):
    for score in lowest_to_highest:
        highest = lowest_to_highest.pop()
        for candidate, score in candidates.items():
            if score[0] == highest:
                ranking.append(candidate)
                count += 1
# print(ranking)

# once found the score, need to assign the option
options = []

# iterate through the ranking list from higest to lowest,
# checking each candidates options
#number of locations available = 6 = max length of options

for rank in ranking:
    # iterate through options checking if already taken
    choices = candidates[rank][1]
#    print(choices)
    for choice in choices:
        if len(options) <= 6:
            if choice in options:
                continue
            else:
                options.append(choice)
                break
    else:
        break

# print(options)

#assign that option to the candidate in a dictionary
successful = {}

for i in range(0,6):
    name = ranking[i]
    location = options[i]
    successful[name] = location

print("\nSuccessful candidates:\n")
for person, location in successful.items():
    print(f"{person}: {location}")

#if all options already taken, put on reserve list
reserve = []

for i in range(6,len(ranking)):
    name1 = ranking[i]
    reserve.append(name1)

print("\nReserve:\n")
for person in reserve:
    print(f"{person}")

print("\n")

#check length of reserve list and bump candidates down to unseuccessful
#from the bottom when too long
