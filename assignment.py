business_name = 'Yusuf & Sons'
p = float(input('Enter amount: '))
t = float(input('Enter time: '))
r = float(input('Enter rate: '))

simple_interest = p * r * t/100
compound_interest = p * ( (1+r/100)**t)

print(business_name)
print('Simple interest is: %f' % (simple_interest))
print('Compound interest is: %f' %(compound_interest))
