import random
def birthday_Generator(n):
    
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Agu','Sep','Oct','Nov','Dec']
    Generated_Dates = []
    for i in range(n):
        month = random.choice(months)
        
        if month in ('Jan','Mar','May','Jul','Agu','Oct','Dec'):
            day = random.randint(1,32)
        elif month == 'Feb':
            day = random.randint(1,30)
        else:
            day = random.randint(1,31)
        
        Generated_Dates.append('{} {}'.format(day, month))
    return Generated_Dates


def matched_BDays(list):
    if len(list) == len(set(list)):
        return None
    for i , Birthdayi in enumerate(list):
        for j , Birthdayj in enumerate(list[i+1:]):
            if Birthdayi == Birthdayj:
                return Birthdayi


while True :
    print("How many birthdays should I generate? (Max =1000)")
    response = input('-->')
    if  response.isdecimal()  and ( 0 < int(response) <=1000):
        numBDays  = int(response)
        break


months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Agu','Sep','Oct','Nov','Dec')
    


print("Here are your {} Birthdates".format(numBDays))
Birthdays = birthday_Generator(numBDays)
print(Birthdays)


print()
print()



match = matched_BDays(Birthdays)


if match != None :
    print("There are people who have birthdays on same date")
    print(match)

else:
    print("There are no matches")



print("Generating "+ str(numBDays)+ " random birthdays 10000 times")
input("Press enter to begin......")


print(" Let's run another 100000 simulations..")
Matched_Sims = 0
for i in range(100000):
    if i % 10000 == 0:
        print(i ,'  simulations run.....')
    birthdayys = birthday_Generator(numBDays)
    if birthdayys != None:
        # print(birthdayys)
        Matched_Sims += 1
        
print('100000 simulations run.')
 
# Display simulation results:
probability = round((Matched_Sims / 100000) * 100, 2)
print('Out of 100000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', Matched_Sims, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')