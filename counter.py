def main() :
counters = countInputs(6)
printCounters(counters)

def countInputs(sides) :
counters = [0] * (sides + 1) # counters[0] is not used.
print("Please enter values, Q to quit:")
userInput = input("")
while userInput.upper() != "Q" :
value = int(userInput)
# Increment the counter for the input value.
if value >= 1 and value <= sides :
counters[value] = counters[value] + 1
else :
print(value, "is not a valid input.")
# Read the next value.
userInput = input("")
return counters
#
def printCounters(counters) :
for i in range(1, len(counters)) :
print("%2d: %4d" % (i, counters[i]))
#start now
main()
