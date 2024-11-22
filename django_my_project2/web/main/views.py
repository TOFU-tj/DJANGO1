from django.shortcuts import render

def main_page(request): 
    return render(request, 'main/main_page.html')

def about_page(request): 
    return render(request, 'main/about_page.html')

def merch_page(request): 
    return render(request, 'main/merch_page.html')

def contact_page(request): 
    conn = {
        'send demo tracks to our lable' : 'radiantmusic69@gmail.com',
        'telegram' : '@radiant_lable'
    }
    return render(request, 'main/contact_page.html',{'conn':conn})


