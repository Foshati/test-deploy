from django.http import HttpResponse


def welcome(request):
    html_content = """
    <html>
    <head>
        <style>
            body {
                font-family: 'Tahoma', 'Arial', sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                text-align: center;
            }
            .container {
                background-color: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
                max-width: 600px;
                width: 90%;
            }
            h1 {
                color: #2c3e50;
                margin-bottom: 1rem;
            }
            p {
                color: #34495e;
                line-height: 1.6;
                margin-bottom: 1rem;
            }
            .highlight {
                color: #3498db;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>به پروژه جنگو خوش آمدید! 🌟</h1>
            <p>این صفحه اصلی پروژه <span class="highlight">Django</span> شماست.</p>
            <p>ما خوشحالیم که شما را در این پروژه می‌بینیم.</p>
            <p>این یک نقطه شروع عالی برای ساخت برنامه وب شماست.</p>
            <p>موفق باشید! 💪</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)