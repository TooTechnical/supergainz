# SuperGainz

**[Live Site → https://supergainz-9cba26bd3cfd.herokuapp.com/](https://supergainz-9cba26bd3cfd.herokuapp.com/)**

**[Admin Site https://supergainz-9cba26bd3cfd.herokuapp.com/admin/](https://supergainz-9cba26bd3cfd.herokuapp.com/admin/)**




SuperGainz is a dynamic web platform for **traders** to **download free indicators** or **purchase premium trading tools.** Users can register, log in, add items to a cart, check out with Stripe, and download PDFs directly from the site.

Built with **Django 5.2** and deployed to **Heroku**, it features a design inspired by professional trading websites like **AlgoGainz.**

---

## ✨ Features

✅ User authentication via Django AllAuth  
✅ Free downloadable trading indicators (PDFs)  
✅ Paid indicators with **Stripe Checkout**  
✅ Shopping cart with add/remove functionality  
✅ Admin panel for managing products  
✅ Static PDF download link  
✅ Responsive styling similar to AlgoGainz  
✅ Hosted live on Heroku

---

## 🛠️ Technologies

- Django 5.2
- Python 3.13
- Stripe API
- Bootstrap & custom CSS
- PostgreSQL (prod) / SQLite (dev)
- Heroku
- Gunicorn
- WhiteNoise
- Git / GitHub

---

## 🚀 Live Demo

👉 [https://supergainz-9cba26bd3cfd.herokuapp.com/](https://supergainz-9cba26bd3cfd.herokuapp.com/)

---



## 🐞 Issues & Solutions

1️⃣ Static files (CSS/JS) not loading on Heroku
Fix:

Added WhiteNoiseMiddleware

Confirmed STATIC_ROOT and STATIC_URL set correctly

Ran collectstatic

Confirmed /staticfiles/ populated

---

##  2️⃣ Free Indicator PDF 404 on Heroku
Cause: Heroku doesn't serve /media/ like local dev.

Fix:

✅ Moved PDF into /static/products/pdfs

✅ Used {% static %} in template

---

## 5️⃣ Stripe cancel URL returned 404
Fix:

Added cancel route:
path('cancel/', views.payment_cancel, name='payment_cancel'),


## 

6️⃣ Admin clicking product → NoReverseMatch
Fix:

✅ Removed/adjusted get_absolute_url in Product model
✅ Or defined product_detail view/URL.

## 

📝 Admin Panel
Accessible at /admin/ → manage:

Products

Users

Indicator files

Note: Upload PDFs manually into /static/products/pdfs/ → run collectstatic.


## 

🚩 Known Limitations
Free PDFs are static links (not uploaded via admin)

Updating a free indicator PDF requires manual file replacement

Staticfiles need collectstatic on every update

## 

❤️ Credits
Created by Dillon Malone

## 



📢 Summary
SuperGainz is a professional-grade Django web app for traders, offering:

✅ Free and paid indicators
✅ Stripe checkout integration
✅ Cart functionality
✅ Robust deployment on Heroku



## 


## 



## 
