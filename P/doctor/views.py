from typing import Counter, Sized
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from .models import doctor,client

def login_page(request):
    if request.method == 'POST':
        id1=request.POST['id']
        username1=request.POST['username']
        password1=request.POST['password']
        a=True
        count=0
        count1=0
        if doctor.objects.filter(id=id1).exists():
            for i in id1:
                if i<'0' or i>'9':
                    messages.error(request,"Wrong ID")
                    a=False
                    return render(request,'login.html')
            if a:
                if doctor.objects.filter(username=username1).exists():
                    for i in username1:
                        if i <='z' or i>='a' or i>='0'or i<=9:
                            a=True
                    if a:
                        if doctor.objects.filter(password=password1).exists():
                            return redirect('home')
                        else:
                            messages.error(request,"Wrong password")
                    else:
                        messages.error(request,"Wrong usrname")
                else:
                    messages.error(request,"Wrong usrname")
        else:
            messages.error(request,"wrong Id")


    return render(request,'login.html')




def home_page(request): 
    m='no details'
    if request.method == 'POST':
        id=request.POST['id']
        name=request.POST['name']
        q1=request.POST['q1']
        q2=request.POST['q2']
        q3=request.POST['q3']
        q4=request.POST['q4']
        q5=request.POST['q5']
        q6=request.POST['q6']
        q7=request.POST['q7']
        q8=request.POST['q8']
        q9=request.POST['q9']
        mc=request.POST['mc']
        age=request.POST['age']
        g = request.POST['g']
        

        if q1 != '':
            m='כמות תאי הדם הלבנים. במבוגרים(+18 ) : 4500-11000, בילדים(4-17): 5500-15500,בפעוטות(0-3): 6000-17500 ערכים גבוהים : מצביעים לרוב על קיומו של זיהום, אם קיימת מחלת חום. במקרים אחרים, נדירים ביותר , עלולים ערכים גבוהים מאוד להעיד על מחלת דם או סרטן.ערכים נמוכים: מצביעים על מחלה ויראלית, כשל של מערכת החיסון ובמקרים נדירים ביותר על סרטן'
        
        
        if q2 != '':
            m='כמות תאי הדם הלבנים האחראים בעיקר על חיסול החיידקים. ערכים תקינים : 28%- 54% מכלל תאי הדם הלבנים ערכים גבוהים : מעידים לרוב על זיהום חיידקה   ערכים נמוכים: מעידים על הפרעה ביצירת בדם על נטייה לזיהומים מחיידקים ובמקרים נדירים- על תהליך סרטני'
       
        if q3 != '':
            m='תאי דם לבנים האחראים על הריגת נגיפים או חיידקים הנמצאים בגוף זמן ממושך . ערכים תקנים: 36%-52% מכלל תאי הדם הלבנים.   ערכים נמוכים : מעידים על בעיה ביצירת תאי הדם.    ערכים גבוהים:עשויים להצביע על זיהום חיידקי ממושך או על סרטן הלימפומה'
       
        if q4 != '':
            m='כדוריות הדם האדומות אחראיות על קשירת חמצן מהריאות, על הובלתו לרקמות ההגוף, על על קליטת פחמן דו-חמצני מתאי הגוף השונים ועל פליטתו בחזרה לריאת. ערכים תקנים : 4.5-6.  ערכים גבוהים :  עלולים להצביע על הפרעה במערכת ייצור הדם. רמות גבוהות נצפו גם אצל מעשנים ואצל חולים במחלות ריאות.  ערכים נוכים :  עלולים להצביע על אנמיה או על דימומים קשים'
       
        if q5 != '':
            m='נפח כדוריות הדם האדומות בתוך כלל נוזל הדם.  ערכים תקינים : גברים: 37%-54%. נשים: 33%-47%  ערכים גבוהים : שכיח בדרך כלל אצל מעשנים  ערכים נמוכים :  מצביעים לרוב על דימום או על אנמיה'
       
        if q6 != '':
            m='רמת השתנן בדם . שתנן הוא התוצר הסופי של תהליך חילוף החומרים של חלבונים בגוף. ערכים תקינים : 17 עד 43 מיליגרם  ערכים גבוהים : עלולים להצביע על מחלות כליה , התייבשות או דיאטה עתירת חלבונים  ערכים נמוכים : תת תזונה , דיאטה דלת חלבון או מחלת כבד . יש לציין שבהריון רמת השתנן יורדת'
       
        if q7 != '':
            m='המוגלובין הוא מרכיב בתוך  הכדורית האדומה , אשר אחראי על קשירתם ועל שחרורם של חמצן ושל פחמן דו-חמצני. ערכים תקינים : נשים: 12-16 מילגרם , גברים 12-18 ,ילדים 0-17 : 11.5-15.5 מילגרם ערכים נמוכים : מעידים על אנמיה . זו יכולה לנבוע מהפרעה המטולוגית ממחסור בברזל ומדימומים'
       
        if q8 != '':
            m='הברזל חיוני ליצירת ההומוגלובין - החלבון שנושא את החמצן בדם  נוסף על כך הוא משמ ליצירת אנזימים רבים אחרים . ערכים תקינים 60 עד 160 אצל נשים נמוך ב20% רמות גבוהות : עלולים להצביע על הרעלת ברזל  רמות נמוכות : מעידה בדרך כלל על תזונה לא מספקת או על עלייה בצורך בברזל או על איבוד דם בעקבות דימום'
       
        if q9 != '':
            m='הקרוי גם "הכולוסטרול הטוב" ,הינו מולקולה דמוית חלבון , אשר נושאת את הכולובטרול מתאי הגוף אל הכבד , שם מפורק הכולוסטרול'


        if q1 == '':
            q1=0
   

        if q2 == '':
            q2=0
        
        if q3 == '':
            q3=0
        
        if q4 == '':
            q4=0
       
        if q5 == '':
            q5=0
       
        if q6 == '':
            q6=0
        
        if q7 == '':
            q7=0
       
        if q8 == '':
            q8=0
       
        if q9 == '':
            q9=0
        
       


        client.objects.create(id=id,name=name,age=age,g=g,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,q7=q7,q8=q8,q9=q9,mc=mc)
        return redirect('detail',m)
    return render(request,'doctorpage.html')


def patient_det(request,m):
    content={'m':m}
    return render(request,'Details.html',content)


def list_c(request):
    clients = client.objects.all()
    return render(request,'clients.html',{'clients':clients})