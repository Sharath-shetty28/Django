from django.http import JsonResponse, FileResponse
from django.shortcuts import render
from PIL import Image
from io import BytesIO
import os



def index(request):
    return render(request, 'index.html')


def img_to_pdf(request):
    if request.method == 'POST':
        files = request.FILES.getlist('images')

        # Ensure at least one file is uploaded
        if len(files) < 1:
            return JsonResponse({'error': 'Please upload at least one image.'}, status=400)

        images = []
        for file in files:
            try:
                # Open image and ensure it's in RGB mode for PDF compatibility
                img = Image.open(file)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                images.append(img)
            except Exception as e:
                return JsonResponse({'error': f'Error processing file {file.name}: {e}'}, status=400)

        # Create a PDF from the images
        pdf_file = BytesIO()
        first_image = images.pop(0)
        first_image.save(pdf_file, format='PDF', save_all=True, append_images=images)
        pdf_file.seek(0)

        # Generate a file name for the PDF
        first_file_name = os.path.splitext(files[0].name)[0]
        pdf_file_name = f"{first_file_name}_converted.pdf"

        # Return the PDF as a file response
        response = FileResponse(pdf_file, as_attachment=True, filename=pdf_file_name)
        return response

    return render(request, 'converter/img_to_pdf.html')
  


# views.py
import os
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from docx import Document
from io import BytesIO
from reportlab.pdfgen import canvas

@csrf_exempt
def word_to_pdf(request):
    if request.method == "POST" and request.FILES.get("word_files"):
        files = request.FILES.getlist("word_files")
        pdf_buffer = BytesIO()
        canvas_obj = canvas.Canvas(pdf_buffer)

        try:
            for file in files:
                if file.name.endswith(".docx"):
                    doc = Document(file)
                    
                    # Start writing from the top of the page
                    x, y = 50, 800  
                    
                    for paragraph in doc.paragraphs:
                        # Split paragraph into lines if it exceeds the page width
                        lines = canvas_obj.beginText(x, y)
                        lines.setFont("Helvetica", 12)
                        
                        # Handle word wrapping manually for long text
                        max_width = 500  # Adjust based on page width
                        words = paragraph.text.split()
                        line = ""
                        
                        for word in words:
                            if canvas_obj.stringWidth(line + word + " ", "Helvetica", 12) <= max_width:
                                line += word + " "
                            else:
                                lines.textLine(line.strip())
                                line = word + " "
                                y -= 20
                                if y < 50:  # Move to a new page if needed
                                    canvas_obj.drawText(lines)
                                    canvas_obj.showPage()
                                    y = 800
                                    lines = canvas_obj.beginText(x, y)
                        
                        if line:
                            lines.textLine(line.strip())
                            y -= 20

                        # Ensure proper spacing between paragraphs
                        y -= 10
                        if y < 50:  # Move to a new page if needed
                            canvas_obj.drawText(lines)
                            canvas_obj.showPage()
                            y = 800
                            lines = canvas_obj.beginText(x, y)

                        canvas_obj.drawText(lines)
                else:
                    return JsonResponse({"error": "Invalid file format. Only .docx files are allowed."}, status=400)

            canvas_obj.save()
            pdf_buffer.seek(0)

            response = HttpResponse(pdf_buffer, content_type="application/pdf")
            response["Content-Disposition"] = f'attachment; filename="converted_files.pdf"'
            return response
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "converter/word_to_pdf.html")



   
