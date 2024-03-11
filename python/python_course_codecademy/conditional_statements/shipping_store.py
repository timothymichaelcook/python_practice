#variables
name = input('Please enter your name: ')
weight = input('How much does your package weigh? ')
weight = int(weight)
cost_premium = 125

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 4:
  cost_drone = weight * 9
elif weight <= 6:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

#program
print('')
print('Hello ' + name + ', welcome to Sal\'s shipping store.')
print('Let\'s check how much your package weighs.')
print('Your package weighs ' + str(weight) + 'lbs.')

if cost_ground < cost_premium and cost_drone:
  print('Your least expensive option is: ground shipping.')
elif cost_premium < cost_ground and cost_drone:
  print(print('Your least expensive option is: premium shipping.'))
else:
  print('Your least expensive option is: drone shipping.')
choice = input('What shipping method would you like to use: ground, premium, or drone shipping? ')

if choice == 'ground':
  print('Your total today for ground shipping is: $' + str(cost_ground) + '.00')
elif choice == 'premium':
  print('Your total today for premium shipping is: $' + str(cost_premium) + '.00')
elif choice == 'drone':
  print('Your total today for drone shipping is: $' + str(cost_drone) + '.00')