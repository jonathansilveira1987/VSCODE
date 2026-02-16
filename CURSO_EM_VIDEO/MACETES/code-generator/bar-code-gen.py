from barcode import EAN13
from barcode.writer import ImageWriter

# Gera o código de barras e salva no caminho desejado #
with open(r'C:\Users\Jonathan Silveira\Documents\VISUALSTUDIOCODE\MACETES\code-generator.png', 'wb') as f:
    EAN13('123456789102', writer=ImageWriter()).write(f)