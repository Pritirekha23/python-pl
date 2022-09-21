# Generating a strong password using python.
 # Create 8 charachter password that must contain alphabet,digits and special symbols
import random as ra
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits='0123456789'
sp_symbol="~!@#$%^&*()_+[]<>/|"
print(ra.choice(alpha),ra.choice(digits),ra.choice(sp_symbol),ra.choice(alpha),ra.choice(digits),ra.choice(sp_symbol),sep='')


print('----')
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits='0123456789'
sp_symbol="~!@#$%^&*()_+[]<>/|"
print(ra.choice(alpha+digits),ra.choice(digits+sp_symbol),ra.choice(sp_symbol+alpha),ra.choice(alpha),ra.choice(digits),ra.choice(sp_symbol+alpha),sep='')


print('********')

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits='0123456789'
sp_symbol="~!@#$%^&*()_+[]<>/|"
for i in range(10):
    print(ra.choice(alpha),ra.choice(digits),ra.choice(sp_symbol),ra.choice(alpha),ra.choice(digits),ra.choice(sp_symbol),sep='')

