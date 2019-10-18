évszak = input('Milyen évszak van? (ny/ő) ')
esik = input('Esik az eső? (i/n) ')
szél = input('Fúj a szél? (i/n)? ')

if szél == 'n' and évszak == 'ny' or évszak == 'ő' and esik == 'n':
    print('Megyünk!')
else:
    print('Maradunk!')
