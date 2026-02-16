int_  =  1 
float_  =  1.5 
complex_  =  5  +  4j  # parte real e parte complexa
print ( '\ninteiro:' ,  int_ ,  'type:' ,  type ( int_ )) 
print ( 'número real: {:.2f} type: {} ' . format ( float_ ,  type ( float_ ))) 
print ( 'número complexo: '  +  str ( complex_ )  +  ' type: '  +  str ( type ( complex_ )))

str_ = 'Você vai usar'
str_ += ' álgebra linear'
str_ = str_.__add__(' durante toda sua carreira!') # acabei de usar um dos 'métodos mágicos', busque mais a respeito sobre eles!
str__ = ' Estude!'
str_ = str_ + str__
print(f'\n{str_}\n')