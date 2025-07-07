#Choose Your Own Adventure Game

phone = 'no'
game_start = 'yes'

while game_start == 'yes':
  print('You\'re watching TV in your home alone and the power goes out in your bedroom. Do you go downstairs to check it out?')
  answer_1 = input('Yes or no? ')
  if answer_1 == 'yes':
    print('You go downstairs and hear a noise. Do you want to grab something to protect yourself?') 
  else:
    print('You close the door and lock it. You search for your phone, but realize it\'s still in the bathroom. Do you go look for it?')
    phone = input('Yes or no? ')
    while phone == 'no':
      print('You don\'t have any options. Do you want to look for your phone?')
      phone = input('Yes or no? ')
    print('You open the door and tiptoe into the bathroom. You grab your phone and hear a noise downstairs. Do you want to check it out?')
  answer_2 = input('Yes or no? ')
  if answer_2 == 'yes':
    print('You picked up your sister\'s baseball bat. Do you want to head towards the noise?')
    answer_3 = input('Yes or no? ')
    if answer_3 == 'yes':
      print('You slowly inch towards the noise in your garage. You notice that the power is switched off. Is it time to call the police?')
      answer_4 = input('Yes or no? ')
      if answer_4 == 'yes':
        if phone == 'yes':
          print('Good choice. You call 911 and wait for authorities to arrive.')
          break
        print('You feel your pocket and realize you left it inside. Do you head back inside?')
        input('Yes or no? ')
        print('You realize it\'s not a good idea to go back inside. You go to your neighbor\'s house and call the police.')
        break
      else:
        print('Surprise! You search the garage and find your best friend hiding there. They were playing a prank on you! ')
      break
    else:
      if phone == 'yes':
        print('Good call. You dial 911 and wait for authorities to arrive.')
        break
      print('You try to dial 911, but realize you don\'t have your phone.')
  else:
    if phone == 'yes':
      print('Good call. You dial 911 and wait for authorities to arrive.')
      break
    print('This story line does not end well.')
  game_start = input('Do you want to start over? ')