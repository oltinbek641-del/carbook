# Carbook — nimalarni to'g'irlash kerak

hozir u umuman ishga tushmayapti. Pastda hammasini yozib qo'ydim.
Tartib bilan, birinchi punktdan boshlab qil. Har bir qismdan keyin `python manage.py runserver` qilib tekshirib tur.

Eslatma: `carbook_master` papkasini `config` deb o'zgartirdim. Endi `config` bu **loyiha** (settings, urls),
`carbook` esa **app** (models, views). Adashtirma.

---

## 1-qism. Loyiha ishga tushishi uchun 

**1. `carbook/urls.py` yo'q**
`config/urls.py` ichida `include('carbook.urls')` bor, lekin `carbook` papkasida `urls.py` fayli yo'q.
Uni yarat va hamma sahifalar uchun `path(...)` yoz (home, about, services, pricing, cars, blog, contact).
Har biriga `name=` berishni unutma, keyin kerak bo'ladi.

**2. `config/urls.py` 31-qator**
`path('contact/', views.contact, ...)` — `views` import qilinmagan, xato beradi.
Bu qatorni o'chir, contact ni `carbook/urls.py` ga o'tkaz.

**3. `INSTALLED_APPS` ga app qo'shilmagan**
`config/settings.py` da `INSTALLED_APPS` ichiga `'carbook'` ni qo'sh. Busiz modeling ham, admin ham ishlamaydi.

**4. `views.py` da shablon nomlari noto'g'ri**
Sen `'About.html'`, `'Services.html'`, `'Cars.html'` deb yozgansan, fayllar esa kichik harf bilan:
`about.html`, `services.html`, `car.html`... Linuxda katta-kichik harf muhim!
Hamma nomlarni `templates` papkasidagi fayllarga moslab chiq.

**5. 3 ta shablonda `{% load static %}` yo'q**
`blog-single.html`, `contact.html`, `main.html` — bularda `{% static %}` ishlatilgan, lekin tepada
`{% load static %}` yozilmagan. Qo'shib qo'y, aks holda sahifa ochilmaydi.

---

## 2-qism. Sayt chiroyli ko'rinishi uchun

**6. CSS/JS yuklanmaydi**
`settings.py` da `STATIC_URL` bor, lekin Django `static` papkangni bilmaydi. Shuni qo'sh:
```python
STATICFILES_DIRS = [BASE_DIR / 'static']
```

**7. Menyu linklari noto'g'ri**
Menyuda `href="{% static 'about.html' %}"` deb yozilgan — bu `/static/about.html` ga olib boradi, 404 chiqadi.
Sahifalarga link `{% url 'about' %}` orqali qilinadi (1-punktdagi `name=` shu yerda kerak).
Hamma shablonlarda menyuni to'g'irla.

**8. Rasmlar va skriptlar yo'li**
- `<script src="../static/js/...">` — bunday yozma, `{% static 'js/...' %}` qil.
- `style="background-image: url(images/car-1.jpg);"` — bu ham ishlamaydi, `url('{% static 'images/car-1.jpg' %}')` qil.
- Ba'zi joylarda `href="car-single.html"` qolib ketgan — ularni ham `{% url %}` ga o'tkaz.

**9. Google Fonts**
`about.html` va `car.html` 9-qatorda Google Fonts linkini `{% static %}` ichiga o'ragansan.
Tashqi linklar `static` ga kerak emas, oddiy yoz. `car.html` da qo'shtirnoq ham buzilgan, qarab chiq.

---

## 3-qism. Model va admin

**10.** `Car` modelida `ImageField` bor — buning uchun `pip install pillow` kerak.
Keyin `python manage.py makemigrations` va `python manage.py migrate` qil (migratsiyalar umuman yo'q).

**11.** `admin.py` da `Car` modelini ro'yxatdan o'tkaz, admin panelda ko'rinsin.

**12.** Rasm yuklash uchun `settings.py` ga `MEDIA_URL` va `MEDIA_ROOT` qo'sh, `urls.py` da media fayllarni ulab qo'y.

---

## 4-qism. Kodni tozalash (vaqting bo'lsa)

**13.** Har bir shablonda menyu va footer bir xil, takrorlanib ketgan. `base.html` yarat,
qolganlarida `{% extends 'base.html' %}` va `{% block content %}` ishlat.

**14.** View funksiyalar nomi kichik harf bilan yoziladi: `Home` emas `home`, `About` emas `about`.

**15.** Formalarda (`contact.html`, `index.html`) `method="post"` va `{% csrf_token %}` yo'q.

**16.** `config/urls.py` dagi `i18n` qismi chala qolgan (`LocaleMiddleware` yo'q). Hozircha kerak bo'lmasa — o'chirib tashla.



---

Hammasini qilib bo'lgach, menga yoz — tekshirib beraman. 
