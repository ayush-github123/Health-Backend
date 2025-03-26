from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Health API</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #f4f4f4; }
            h1 { color: #4CAF50; }
            .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }
            a { display: block; margin: 10px 0; text-decoration: none; color: #2196F3; font-weight: bold; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Welcome to the Health API!</h1>
            <p>Explore the API documentation:</p>
            <a href="/docs/swagger/">📜 Swagger Docs</a>
            <a href="/docs/redoc/">📘 ReDoc</a>
            <a href="/api/schema/">📄 OpenAPI Schema</a>
        </div>
    </body>
    </html>
    """)
