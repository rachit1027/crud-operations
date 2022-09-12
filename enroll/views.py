from django.shortcuts import render,HttpResponseRedirect


from enroll.forms import studentregistration
from enroll.models import User


#this function will add new data and show it
def addshow(request):
    if request.method=='POST':
        fm=studentregistration(request.POST)
        if fm.is_valid():
            #fm.save() yaha pr save karwa skate hai baaki apan ab ek ek data ko save karwa rahe hai isme poora data ek saath jaar hai ye bhi kar skte hai ki dikkat nahi hai
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']#or jaise apan chahte hai ki koi field save na ho database me to yaha se vo field hata do simple.
            pw=fm.cleaned_data['password'] # ek ek data save hpha agr poora karna ek baar me to direct save lokh do
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=studentregistration()# form ko data add karne ke baad vapas blank hone ke lie lagaya hai ye
            
    else:
        fm=studentregistration()
    stud=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#this function will delete
def delete(request,id):#dynamic url se pk me id chale jaaega
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')# home page pe redirect ho jaaega

#this function will update and edit
def update(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=studentregistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save
    else:
        pi=User.objects.get(pk=id)
        fm=studentregistration( instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})
    return render(request,'enroll/updatestudent.html',{'id':id})