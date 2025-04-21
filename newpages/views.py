from django.http import HttpResponse
from django.urls import reverse

def page1(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Page1</title>
        <style>
            video {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
        </style>
    </head>
    <body>
        <a href="/page2/" style="
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            padding: 15px 30px;
            background-color: #2980b9;
            color: white;
            font-size: 24px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            z-index:1;
        ">
            Keyingi sahifaga o'tish
        </a>
        <video autoplay muted loop>
            <source src="https://nn.tuit.uz/video/video.mp4" type="video/mp4">
            <source src="https://nn.tuit.uz/video/video.ogg" type="video/ogg">
            <source src="https://nn.tuit.uz/video/video.webm" type="video/webm">
        </video>
        
    </body>
    </html>
    """
    return HttpResponse(html)

def page2(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Page 2</title>
    </head>
    <body style = "background-image: url(https://nn.tuit.uz/assest/images/gallery/images/img14.jpg); background-size:1550px;">
        <h1 style = "text-align:center; font-size:50px; padding:50px;">My University</h1>
        <p style = 'font-size:20px; text-align: center; padding:300px; padding-top:0;'>TATU — O‘zbekistonning axborot-kommunikatsiya texnologiyalari (AKT) sohasidagi yetakchi oliy ta’lim muassasasi hisoblanadi. Ushbu universitet 1955-yilda tashkil etilgan bo‘lib, ilgari Toshkent elektrotexnika aloqa instituti (TEAI) nomi bilan tanilgan.</p>
        <a href="/page1/" style="
            margin-right: 20px;
            padding: 12px 24px;
            background-color: #27ae60;
            color: white;
            font-size: 20px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            bottom: 5%;
            position:fixed;
        ">
            Oldingi sahifa
        </a>
        <a href="/page3/" style="
            padding: 12px 24px;
            background-color: #2980b9;
            color: white;
            font-size: 20px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            bottom: 5%;
            position: fixed;
            right: 20px;
        ">
            Keyingi sahifa
        </a>

    </body>
    </html>
    """
    return HttpResponse(html)
def page3(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Page 3</title>
    </head>
    <body style = "background-image: url(https://scontent.ftas2-2.fna.fbcdn.net/v/t39.30808-6/466133576_1103264541806720_324967089494655763_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=833d8c&_nc_ohc=zKv3B14Bb1IQ7kNvwFeQU5i&_nc_oc=AdkYKmXDFFiTGhk-E-laoN0O7NWs4eNNvdt_Aq3AHFlzqEM8savDXDycOj3TtT-fkVo&_nc_zt=23&_nc_ht=scontent.ftas2-2.fna&_nc_gid=99XQC6bH_21YsQEqS0w62A&oh=00_AfEPm8LfEgGwHf9I86-ed4G311kZxS5v7zln-7a-ut_tlg&oe=680971EC); background-size:cover;">
       <h1 style = "text-align:center; font-size: 60px;">Mening fakultetim</h1>
       <a href="/page2/" style="
            margin-right: 20px;
            padding: 12px 24px;
            background-color: #27ae60;
            color: white;
            font-size: 20px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            bottom: 5%;
            position:fixed;
        ">
            Oldingi sahifa
        </a>
        <a href="/page4/" style="
            padding: 12px 24px;
            background-color: #2980b9;
            color: white;
            font-size: 20px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            bottom: 5%;
            position: fixed;
            right: 20px;
        ">
            Keyingi sahifa
        </a>

    </body>
    </html>
    """
    return HttpResponse(html)

def page4(request):
    html = """
    <html>
    <body style="background-image: url(https://i.ytimg.com/vi/a_YoDIElW1s/hqdefault.jpg); background-size: cover; background-position: center;">            <h1>Bu Page 4</h1>
            <h1 style = "color:white;text-align:center;font-size:50px;">Fakultet haqida ma'lumot</h1>
            <h1 style = "color:white;padding:20px;">Dasturiy injiniring fakulteti haqida ma’lumot
            🧠 Ta'rifi:
            Dasturiy injiniring (inglizcha: Software Engineering) — bu kompyuter dasturlarini tizimli, ishonchli, samarali va tejamkor tarzda loyihalash, yaratish, sinash va qo‘llab-quvvatlash bilan shug‘ullanuvchi muhandislik sohasidir.
            
            🎓 Fakultetda o‘qitiladigan asosiy fanlar:
            Algoritmlar va ma’lumotlar tuzilmasi
            
            Dasturlash tillari (C++, Java, Python, JavaScript va boshqalar)
            
            Ma’lumotlar bazasi (SQL, PostgreSQL)
            
            Web dasturlash va mobil ilovalar ishlab chiqish
            
            Dasturiy ta’minotni testlash va sinovdan o‘tkazish
            
            Tizimli tahlil va talablarni yig‘ish
            
            Versiyalarni boshqarish (Git, GitHub)
            
            Sun’iy intellekt va mashinali o‘rganish (AI/ML) asoslari
            
            Kompyuter tarmoqlari va xavfsizlik
            
            Operatsion tizimlar
            
            🎯 Fakultet maqsadi:
            Dasturiy mahsulotlar ishlab chiqishning barcha bosqichlarida ishtirok eta oladigan yuqori malakali dasturchilar va muhandislarni tayyorlash.
            
            Talabalarga real loyihalar asosida amaliy tajriba berish.
            
            IT industriyasiga raqobatbardosh mutaxassislar yetkazib berish.
            
            </h1>
            <a href="/page3/" style="
            margin-right: 20px;
            padding: 12px 24px;
            background-color: #27ae60;
            color: white;
            font-size: 20px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            bottom: 5%;
            position:fixed;
        ">
            Oldingi sahifa
        </a>
        <a href="/page5/" style="
            padding: 12px 24px;
            background-color: #2980b9;
            color: white;
            font-size: 20px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            bottom: 5%;
            position: fixed;
            right: 20px;
        ">
            Keyingi sahifa
        </a>
        </body>
    </html>
    """
    return HttpResponse(html)

def page5(request):
    html = """
    <html>
        <head>
            <title>Page 5 </title>
        </head>
        <body style = "background-image: url(https://www.mgpu.ru/wp-content/uploads/2021/11/kod-tvorchesva.jpg);background-size:cover;">
            <h1 style = "color:white; padding:20px;">Bu oxirgi sahifa. Rahmat!</h1>
            <a href="/page4/" style="
            margin-right: 20px;
            padding: 12px 24px;
            background-color: #27ae60;
            color: white;
            font-size: 20px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            bottom: 5%;
            position:fixed;
        ">
            Oldingi sahifa
        </a>
        </body>
    </html>
    """
    return HttpResponse(html)