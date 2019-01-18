import time 
import random

print()
print('-' * 63)
print('A wild Jigglypuff appears!')
time.sleep(0.2)
print('You only have one Pokemon.')
time.sleep(0.2)
print('I choose you Leekbird!')
print()
time.sleep(0.2)


# Starting HPs
Leekbird_hp = 200
Jigglypuff_hp = 125 

#Print out starting HPs
print('Original HPs')
time.sleep(0.2)
print('- Leekbird HP:' + str(Leekbird_hp))
time.sleep(0.2)
print('-Jigglypuff HP:' + str(Jigglypuff_hp))
time.sleep(0.2)
print()
time.sleep(0.2)


while Leekbird_hp > 0 and Jigglypuff_hp > 0:

	print('Battle Options:')
	time.sleep(0.2)
	print('- [1] Pray ')
	time.sleep(0.2)
	print('- [2] Tackle ')
	time.sleep(0.2)
	print('- [3] TWEEN BEHIND THE BACK...FILLLAYY')
	time.sleep(0.2)
	print('- [4] YEEEEEEET ')
	time.sleep(0.2)
	print('- [5] Capture ')
	time.sleep(0.2)
	print()
	your_move=input('Choose a move using the corresponding number: ')
	print()
	if your_move is '1':
		print('Leekbird uses Pray Heal')
		Snorlax_hp = Snorlax_hp + 50
		print('Leekbird uses Pray Heal, his HP increases to ' + str(Snorlax_hp))
		time.sleep(0.2)
	elif your_move is '2':
		Jigglypuff_hp = Jigglypuff_hp - 10 
		print('Leekbird uses tackle and deals 10 damage to Jigglypuff')
		time.sleep(0.2)
	elif your_move is '3':
		Jigglypuff_hp = Jigglypuff_hp - 30
		print('Leekbird uses TWEEN BEHIND THE BACK...FILLLAYY and deals 30 damage to Jigglypuff')
		time.sleep(0.2)
	elif your_move is '4':
		Jigglypuff_hp = Jigglypuff_hp - 40 
		print('Leekbird uses YEEEEEEET and deals 40 damage to Jigglypuff')
		time.sleep(0.2)
	elif your_move is '5':
		capture_roll = random.randint(0,125)
		if capture_roll > Jigglypuff_hp:
			print('You have captured Jigglypuff!')
			break


		else:
			print('You tried to capture Jigglypuff, but he escaped')
	elif your_move is '6':
		Jigglypuff_hp = Jigglypuff_hp - 25
		print('Leekbird uses Water Blast and deals 25 damage to Jigglypuff')
		time.sleep(0.2)
		
	print()

	#Jigglypuff attacks 
	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)


	if enemy_move is '1':
		Snorlax_hp = Snorlax_hp - 30
		Jigglypuff_hp = Jigglypuff_hp + 30
		print('Jigglypuff uses Drink Blood and deals 30 HP of damage while recovering. ')
		time.sleep(0.2)
	if enemy_move is '2':
		Snorlax_hp = Snorlax_hp - 50
		print('Jigglypuff uses Free Smoke and deals 50 HP of damage.')
		time.sleep(0.2)

	print()

#Check for overkill
	if Leekbird_hp < 0:
		Leekbird_hp = 0
	if Jigglypuff_hp < 0: 
		Jigglypuff_hp = 0


	print('Updated HP:')
	time.sleep(0.2)
	print('- Leekbird HP:' + str(Leekbird_hp))
	time.sleep(0.2)
	print('- Jigglypuff HP:' + str(Jigglypuff_hp))
	time.sleep(0.2)
	print()
	time.sleep(0.2)

if Leekbird_hp == 0:
	print('You lost the battle! Jigglypuff wins!!!')
elif Jigglypuff_hp == 0:
	print('You lost the battle! Leekbird wins!!!')







print('-' * 63)	