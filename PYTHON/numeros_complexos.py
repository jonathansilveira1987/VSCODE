# Converter números reais em números complexos.
import cmath 
x = float(input('\nVetor A: '))
y = float(input('Vetor B: '))
z = complex(x,y); 
print ("\nA parte real do número complexo é: ",end="") 
print (z.real) 
print ("A parte imaginária do número complexo é: ",end="") 
print (z.imag)
print ("A fase do número complexo é: ",end="") 
print (cmath.phase(z))
print ("O módulo e o argumento do número complexo polar é: ",end="")
w = cmath.polar(z) 
print (w) 
w = cmath.rect(1.4142135623730951, 0.7853981633974483) 
print ("A forma retangular do número complexo é: ",end="") 
print (w)
print()