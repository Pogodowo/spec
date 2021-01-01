import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
#==================================
from django.shortcuts import render
from . import slownie



def home (request):
    ls=''
    ls1=''
    ls3=''
    liczba= request.GET.get("li200")
    liczba1=request.GET.get("li100")
    liczba3=request.GET.get("li50")
    if liczba and liczba.isdigit():
        liczba=int(liczba)*200
        ls=slownie.slownie(int(liczba))
    if liczba1 and liczba1.isdigit():
        liczba1=int(liczba1)*100
        ls1=slownie.slownie(int(liczba1))
    if liczba3 and liczba3.isdigit():
        liczba3=int(liczba3)*50
        ls3=slownie.slownie(int(liczba3))
    suma=0
    if liczba1 and liczba and liczba3:
        suma=int(liczba)+int(liczba1)+int(liczba3)
    return render(request, 'home.html',{'liczba':liczba,'liczba1':liczba1,'liczba3':liczba3,
                                        'suma':suma,
                                        'ls':ls,
                                        'ls1':ls1,
                                        'ls3':ls3})


def some_view(request):

    
    ls = ''
    ls1 = ''
    ls3 = ''
    liczba = request.GET.get("li200")
    liczba1 = request.GET.get("li100")
    liczba3 = request.GET.get("li50")
    if liczba and liczba.isdigit():
        liczba = int(liczba) * 200
        ls = slownie.slownie(int(liczba))
    if liczba1 and liczba1.isdigit():
        liczba1 = int(liczba1) * 100
        ls1 = slownie.slownie(int(liczba1))
    if liczba3 and liczba3.isdigit():
        liczba3 = int(liczba3) * 50
        ls3 = slownie.slownie(int(liczba3))
    suma = 0


       # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, ls3)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer , as_attachment=True, filename='hello.pdf')
