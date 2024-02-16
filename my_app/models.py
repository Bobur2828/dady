from django.db import models

class Slider(models.Model):
    text=models.CharField(max_length=100, verbose_name='Sarlavha kiriting')
    text_rus=models.CharField(max_length=100, verbose_name='Sarlavha kiriting Rus tilida')
    text1=models.CharField(max_length=100, verbose_name='2-Sarlavha kiriting')
    text1_rus=models.CharField(max_length=100, verbose_name='2-Sarlavha kiriting Rus tilida')
    text2=models.CharField(max_length=100,blank=True, default=None,null=True, verbose_name='Sarlavha ostidagi 1-qator')
    text2_rus=models.CharField(max_length=100,blank=True, default=None,null=True,verbose_name='Sarlavha  ostidagi 1-qatorRus tilida')
    text3=models.CharField(max_length=100,blank=None, null=True, verbose_name='Sarlavha  ostidagi 2-qator')
    text3_rus=models.CharField(max_length=100, blank=None, null=True,verbose_name='Sarlavha  ostidagi 2-qator Rus tilida')  
    image=models.ImageField(upload_to='slider', verbose_name='Banner uchun rasm kiriting')
    button=models.CharField(max_length=100, verbose_name='Knopkadagi sozni kiriting masalan:Batafsil')
    button_rus=models.CharField(max_length=100, verbose_name='Knopkadagi sozni rus tilida kiriting')
    data_created = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=10, unique=True, db_index=True, verbose_name='Kalit sozni kiriting')

class About(models.Model):
    text=models.CharField(max_length=100, verbose_name='Sarlavha kiriting')
    text_rus=models.CharField(max_length=100, verbose_name='Sarlavha kiriting Rus tilida')
    text1=models.CharField(max_length=100, verbose_name=' Asosiy Sarlavha kiriting')
    text1_rus=models.CharField(max_length=100, verbose_name='Asosiy Sarlavha kiriting Rus tilida')
    text2=models.TextField(max_length=500, verbose_name=' Matnni  kiriting')
    text2_rus=models.TextField(max_length=500, verbose_name=' Matnni kiriting Rus tilida')
    text3=models.CharField(max_length=100, verbose_name=' Galochkalar uchun sozlar  kiriting')
    text3_rus=models.CharField(max_length=100, verbose_name=' Galochkalar uchun sozlar  kiriting rus tilida')
    soz=models.CharField(max_length=100, verbose_name='Galochkalar uchun sozlar')
    soz_rus=models.CharField(max_length=100, verbose_name='Galochkalar uchun sozlar Rus tilida')
    soz1=models.CharField(max_length=100, verbose_name='Galochkalar uchun sozlar')
    soz1_rus=models.CharField(max_length=100, verbose_name='Galochkalar uchun sozlar Rus tilida')
    image=models.ImageField(upload_to='slider', verbose_name='Asosiy  rasm kiriting 362x440')
    image1=models.ImageField(upload_to='slider', verbose_name='Orqa taraf uchun rasm kiriting 362x440')
    
class Services(models.Model):
    name=models.CharField(max_length=100, verbose_name='Xizmat nomi')
    name_rus=models.CharField(max_length=100, verbose_name='Xizmat nomi rus tilida')
    content=models.TextField(max_length=100, verbose_name='Xizmat haqida  qisqacha malumot')
    content_rus=models.TextField(max_length=100, verbose_name='Xizmat haqida qisqacha malumot rus tilida')
    content1=models.TextField(max_length=1000, verbose_name='Xizmat haqida  batafsil malumot')
    content1_rus=models.TextField(max_length=1000, verbose_name='Xizmat haqida  batafsil malumot rus tilida')
    image=models.ImageField(upload_to='servis', verbose_name='Xizmatga doir rasm kiriting 1200x800 razmerda')
    slug=models.SlugField(max_length=20, unique=True, db_index=True, verbose_name='kalit sozni kiriting')
    
class Doctors(models.Model):
    name=models.CharField(max_length=100, verbose_name='Doctor Ismi Familiyasi ')
    name_rus=models.CharField(max_length=100, verbose_name='Doctor Ismi Familiyasi rus tilida') 
    soha=models.CharField(max_length=100, verbose_name='Doctor sohasi  masalan:Urolog')
    soha_rus=models.CharField(max_length=100, verbose_name='Doctor sohasi  masalan:Urolog rus tilida')
    about_doctor=models.TextField(max_length=1000, verbose_name='Doktor haqida malumot')
    about_doctor_rus=models.TextField(max_length=1000, verbose_name='Doktor haqida malumot rus tilida')
    image=models.ImageField(upload_to='doctor', verbose_name='Doctor rasmini kiriting 264x250 razmerda')
    


