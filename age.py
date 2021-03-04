driving = input('Can you drive a car?')
if driving != 'yes' and driving != 'no':
	print('You can only answer yes or no')
	raise SystemExit

age = input('How old are you?')
age = int(age) 
if driving == 'yes':
	if age >= 18:
		print('Nice, you can go anywhere at anytime. Be safe')
	else:
		print('What?! How come! Watch out the police.')
elif driving == 'no':
	if age >= 18:
		print('It is time to have a ride on your own')
	else:
		print('Wait~ the time will come')


#else:
	#print(' You can only answer yes/no')＃如果不用上面的systemexit方式，可用else在最後排除掉不必要的答案
