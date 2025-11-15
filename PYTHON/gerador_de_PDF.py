from reportlab.pdfgen import canvas # pip install reportlab
from reportlab.lib.pagesizes import A4

try:
    nome_pdf = input('\nInforme o nome do PDF: ')
    elemento = int(input('\nInforme o número de elementos para a lista: '))
    print()
    listaFinal = [input("Dado: ") for i in range(elemento)]
    pdf = canvas.Canvas(f'{nome_pdf}.pdf')
    for cont, l in enumerate(listaFinal):
        pdf.drawString(100, 750-20 * cont,l) # 100 é alinhamento vertical, 750-20 é alinhamento horizontal.
    pdf.save()
    print(f'\n{nome_pdf}.pdf gerado com sucesso!\n')
except:
    print(f'\nNão foi possível gerar {nome_pdf}.pdf!\n')

# Caso o arquivo precise ter mais de uma página você pode usar a função pdf.showPage(). Veja esse exemplo abaixo:
from reportlab.pdfgen import canvas

pdf = canvas.Canvas('Páginas.pdf')

pdf.drawString(235.5, 85, "Primeira página") # 100 é alinhamento vertical, 750 é alinhamento horizontal.
pdf.showPage()
pdf.drawString(235.5, 85, "Segunda página") # 100 é alinhamento vertical, 750 é alinhamento horizontal.
pdf.showPage()
pdf.drawString(235.5, 85, "Terceira página") # 100 é alinhamento vertical, 750 é alinhamento horizontal.
pdf.showPage()
pdf.save()