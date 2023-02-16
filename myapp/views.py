import mysql.connector
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from myapp.forms import UploadForm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .models import Picture
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.template.loader import get_template

def testpdf(request):
    pdf = canvas.Canvas("test.pdf", pagesize=letter)
    y = 800
    while True: 
        pdf.setTitle("Title")
        pdf.drawImage("static/images/NCST-MAIN_LOGO.png", 10, 700, width=100, height=80)
        pdf.setFont("Times-Roman", size=20)
        pdf.drawCentredString(300, 760, "National College of Science and Technology")
        pdf.setFont("Times-Roman", size=14)
        pdf.drawCentredString(300, 730, "HoMe ExLoDer:")
        pdf.drawCentredString(300, 710, "Hospital and Medical Expert Location Finder")
        pdf.drawImage("static/images/Homeexloderlogo.png", 490, 700, width=100, height=80)
        pdf.line(0, 690, 620, 690)
        current_user = request.user
        username=[current_user.username]
        if current_user.is_authenticated:
            conn = mysql.connector.connect(host='localhost', username='root', password='1234567890', database='disease')
            mycursor = conn.cursor()
            mycursor.execute("select fullname from userprofile where user=%s", username)
            result = mycursor.fetchone()
            text = pdf.beginText(40, 670)
            text.setFont("Times-Roman", 16)
            for line in result:
                text.textLine("Fullname: " + line)
            pdf.drawText(text)

            mycursor.execute("select age from userprofile where user=%s", username)
            result1 = mycursor.fetchone()
            text1 = pdf.beginText(40, 650)
            text1.setFont("Times-Roman", 16)
            text1.textLine("Age: " + str(result1[0]))
            pdf.drawText(text1)
            

            mycursor.execute("select allergies from userprofile where user=%s", username)
            result2 = mycursor.fetchone()
            text2 = pdf.beginText(40, 630)
            text2.setFont("Times-Roman", 16)
            for line2 in result2:
                text2.textLine("Allergies: " + line2)
            pdf.drawText(text2)

            mycursor.execute("select bloodtype from userprofile where user=%s", username)
            result3 = mycursor.fetchone()
            text3 = pdf.beginText(40, 610)
            text3.setFont("Times-Roman", 16)
            for line3 in result3:
                text2.textLine("Allergies: " + line3)
            pdf.drawText(text3)

            mycursor.execute("select height from userprofile where user=%s", username)
            result4 = mycursor.fetchone()
            text4 = pdf.beginText(40, 610)
            text4.setFont("Times-Roman", 16)
            text4.textLine("Height in cm: " + str(result4[0]))
            pdf.drawText(text4)

            mycursor.execute("select weight from userprofile where user=%s", username)
            result5 = mycursor.fetchone()
            text5 = pdf.beginText(40, 590)
            text5.setFont("Times-Roman", 16)
            text5.textLine("Weight in Kg: " + str(result5[0]))
            pdf.drawText(text5)
            mycursor.close()
            conn.close()
        current_user1= request.user
        pictures = Picture.objects.filter(user=current_user1)
        for i, picture in enumerate(pictures):
            current_y = 370 - (i * 200)
            if current_y < 0:
                pdf.showPage()
                current_y = 380
            pdf.drawImage(picture.image.path, 150, current_y, 300, 200)
            # Add the picture to the PDF
        #     pdf.drawImage(picture.image.path, 40, 380 - (i * 80), 300, 200)
        # y -= 200
        # if y < 100:
        #     pdf.showPage()
        #     y = 800    

        pdf.save()
        response = FileResponse(open("test.pdf", "rb"), content_type="application/pdf")
        response["Content-Disposition"] = "attachment; filename=test.pdf"
        return response

def my_login(request):
    page='login'
    if request.method == 'POST':
        username = request.POST.get('username1')
        password = request.POST.get('password1')

        try:
            user = User.objects.get(username=username)
            print(user)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password does not exist')

    context={'page': page}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def registerPage(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)
            return redirect('configuration')
        else:
            # if request.POST.get('password1') != '' and request.POST.get('password2') !='':
            #     if request.POST.get('password1').length and request.POST.get('password2').length < 8:
            messages.error(request, 'Password is too short')
    form = UserCreationForm()
    return render(request, 'login.html', {'form': form})

def home(request):   
    return render(request, 'home.html')

def index(request):
    current_user= request.user
    username= current_user.username   
    context={'username':username}
    return render(request, 'index.html', context)

def about(request):
    current_user= request.user
    username= current_user.username   
    context={'username':username}
    return render(request, 'about.html', context)

def contact(request):
    current_user= request.user
    username= current_user.username   
    context={'username':username}
    return render(request, 'contact.html',context)

@login_required(login_url='login')
def profile(request):

    current_user = request.user
    username=[current_user.username]
    if current_user.is_authenticated:
        conn = mysql.connector.connect(host='localhost', username='root', password='1234567890', database='disease')
        mycursor = conn.cursor()
        mycursor.execute("select fullname from userprofile where user=%s", username)
        result = mycursor.fetchone()
        fullname=[]
        for name in result:
            fullname.append(name)

        mycursor.execute("select age from userprofile where user=%s", username)
        result1 = mycursor.fetchone()
        age=[]
        for edad in result1:
            age.append(edad)

        mycursor.execute("select allergies from userprofile where user=%s", username)
        result2 = mycursor.fetchone()
        allergies=[]
        for kati in result2:
            allergies.append(kati)

        mycursor.execute("select bloodtype from userprofile where user=%s", username)
        result3 = mycursor.fetchone()
        blood=[]
        for dugo in result3:
            blood.append(dugo)

        mycursor.execute("select height from userprofile where user=%s", username)
        result4 = mycursor.fetchone()
        height=[]
        for tangkad in result4:
            height.append(tangkad)

        mycursor.execute("select weight from userprofile where user=%s", username)
        result5 = mycursor.fetchone()
        weight=[]
        for bigat in result5:
            weight.append(bigat)
        mycursor.close()
        conn.close()
    current_user1= request.user
    username1= current_user1.username

    if request.method == 'POST':
        form1 = UploadForm(request.POST, request.FILES)
        if form1.is_valid():
            picture = form1.save(commit=False)
            picture.user = request.user
            # picture.image.name = f"{request.user.username}_{picture.image.name}"
            picture.save()
    else:
        form1 = UploadForm()
    
    if Picture.image is not None:
        pictures = Picture.objects.filter(user=current_user1)
    else:
        pictures = None  
    context = {'fullname': fullname, 'age': age, 'allergies': allergies, 'blood': blood, 'height': height, 'weight': weight, 'username':username1, 'form1': form1,'pictures': pictures}
    return render(request,'profile.html', context)

def hospital(request):
    current_user= request.user
    username= current_user.username   
    context={'username':username}
    return render(request, 'hospital.html',context)

def symptoms(request):
    current_user= request.user
    username= current_user.username   
    context={'username':username}
    return render(request, 'symptoms.html',context)

def search(request):
    if request.method == 'POST':
      sort_by = request.POST.get('sort_by')
      conn = mysql.connector.connect(host='localhost', username='root', password='1234567890', database='disease')
      mycursor = conn.cursor()
      disease = [x+"%" for x in [(request.POST.get('search_query'))]]
      query=("select disease.Name, disease.Specialization, disease.Hospital, disease.location, disease.schedule FROM disease JOIN search ON disease.Service_ID = search.Service_ID WHERE search.services LIKE %s")  
      if sort_by == 'nearest':
        query += " ORDER BY nearest"
      elif sort_by == 'rating':
        query += " ORDER BY rating"
      mycursor.execute(query, disease)
      result=mycursor.fetchall()
      datas=[]    
      for i in result:
        datas.append(i)
      hospital_dict=[{"doctor": person[0], "specialization": person[1], "hospital": person[2], "location": person[3], "schedule": person[4]} for person in datas]
      mycursor.close()
      conn.close()
        # if datas != '':
        #     nearest=request.POST.get('nearest')
        #     datasnr=disease.sort(nearest=nearest)
        #     return render(request, 'search.html', {"datasnr": datasnr})
        # else:
        #     return render(request, 'search.html', context)
    
    current_user= request.user
    username= current_user.username   
    context={'datas': datas, 'username':username,'hospital_dict': hospital_dict}
    return render(request, 'search.html', context)

@login_required(login_url='login')
def editprofile(request):
    
    if request.method == 'POST':
        current_user = request.user
        username= current_user.username
        fullname1 = request.POST['fullname1']
        age1 = request.POST['age1']
        allergies1 = request.POST['allergies1']
        bloodtype1 = request.POST['bloodtype1']
        height1 = request.POST['height1']
        weight1 = request.POST['weight1']
        if age1.strip().isdigit():           
            connection= mysql.connector.connect(host='localhost', username='root', password='1234567890', database='disease')
            cursor = connection.cursor()
            cursor.execute("UPDATE userprofile SET fullname=%s, age=%s, allergies=%s, bloodtype=%s, height=%s, weight=%s WHERE user=%s", (fullname1, age1, allergies1, bloodtype1, height1, weight1, username))
            connection.commit()
            messages.success(request, 'Profile Updated')
        else:
            messages.error(request, 'Use numbers in age')
            return redirect('editprofile')

    current_user= request.user
    username= current_user.username   
    context={'username':username}
    return render(request, 'editprofile.html',context)

@login_required(login_url='login')
def afterlogin(request):
    if request.method == 'POST':
        current_user= request.user
        username= current_user.username
        fullname = request.POST['fullname']
        age = request.POST['age']
        allergies = request.POST['allergies']
        bloodtype = request.POST['bloodtype']
        height = request.POST['height']
        weight = request.POST['weight']

        connection= mysql.connector.connect(host='localhost', username='root', password='1234567890', database='disease')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO userprofile (user, fullname, age, allergies, bloodtype, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s)", (username, fullname, age, allergies, bloodtype, height, weight))   
        connection.commit()
        cursor.close()
        connection.close()
        return redirect('/index/')
    return render(request, 'afterlogin.html')