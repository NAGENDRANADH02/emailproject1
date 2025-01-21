from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import EmailTemplate
import json
import os
from django.conf import settings
# 1. Fetch Email Layout
def get_email_layout(request):
    try:
        # Example static layout; you can later load it from a file or the database
        layout = """
        <html>
        <head><title>{{ title }}</title></head>
        <body>
            <h1>{{ title }}</h1>
            <p>{{ content }}</p>
            <footer>{{ footer }}</footer>
        </body>
        </html>
        """
        context = {'layout': layout}
        return render(request, 'email_layout_get.html', context)  # Render HTML template
    except Exception as e:
        return HttpResponse(f"<h1>Error: {str(e)}</h1>")

# 2. Upload Image
@csrf_exempt
def upload_image(request):
    if request.method == 'GET':
        # Render a form for image upload
        return render(request, 'builder/upload_image.html')
    elif request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        image_path = os.path.join(settings.MEDIA_ROOT, image.name)
        
        # Save the file in the media directory
        with open(image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)
        
        return HttpResponse(f"<h1>Image uploaded successfully! URL: /media/{image.name}</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# 3. Save Email Configuration
@csrf_exempt
def upload_email_config(request):
    if request.method == 'GET':
        # Render a form for inputting email configuration
        return render(request, 'upload_email_config.html')
    elif request.method == 'POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            footer = request.POST.get('footer')
            EmailTemplate.objects.create(
                title=title,
                content=content,
                footer=footer
            )
            return HttpResponse("<h1>Email template saved successfully!</h1>")
        except Exception as e:
            return HttpResponse(f"<h1>Error: {str(e)}</h1>")
    return HttpResponse("<h1>Invalid request</h1>")

# 4. Render and Download Template
@csrf_exempt
def render_and_download_template(request):
    if request.method == 'GET':
        # Render a form for inputting rendering details
        return render(request, 'render_template.html')
    elif request.method == 'POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            footer = request.POST.get('footer')
            layout = """
            <html>
            <head><title>{{ title }}</title></head>
            <body>
                <h1>{{ title }}</h1>
                <p>{{ content }}</p>
                <footer>{{ footer }}</footer>
            </body>
            </html>
            """
            rendered_html = layout.replace('{{ title }}', title)
            rendered_html = rendered_html.replace('{{ content }}', content)
            rendered_html = rendered_html.replace('{{ footer }}', footer)
            response = HttpResponse(rendered_html, content_type='text/html')
            response['Content-Disposition'] = 'attachment; filename="email_template.html"'
            return response
        except Exception as e:
            return HttpResponse(f"<h1>Error: {str(e)}</h1>")
    return HttpResponse("<h1>Invalid request</h1>")
