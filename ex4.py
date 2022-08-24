a = 5 + 5j
b = complex(5, 5)
c = complex(5, 5)

s = (a + b) + b
sub = (a - b) - c
m = (a * b) * c
d = (a / b) / compile

print('Soma:'), print('real:', s.real, '\nimaginário:', s.imag, '\n')
print('Subtração:'), print('real:', sub.real, '\nimaginário', sub.imag, '\n')
print('Multiplicação:'), print('real:', m.real, '\nimaginário', m.imag, '\n')
print('Divisão:'), print('real:', d.real, '\nimaginário:', d.imag)