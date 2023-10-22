from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll.form import userform
from enroll.models import user

# Create your views here.
#def success(request):
#   return render(request, 'enroll/success.html')

def add_show(request):
    print("view work correctly")
    if request.method == 'POST':
       fm = userform(request.POST)
       if fm.is_valid():
          ld = fm.cleaned_data['id']
          nd = fm.cleaned_data['name']
          em = fm.cleaned_data['email']
          pd = fm.cleaned_data['password']
          '''another way of saving data in DB is fm.save()'''
          reg = user(id=ld, name=nd, email=em, password=pd)
          reg.save()
          return HttpResponseRedirect('/')
          #stu = user.objects.all()
          #return render(request, 'enroll/addandshow.html', {'form':fm ,'stub':stu})
          #return render(request, 'enroll/success.html')
    else:
      fm = userform()
      stu = user.objects.all()
      return render(request, 'enroll/addandshow.html', {'form':fm ,'stub':stu})

# for delete data

def delete_data(request, id):
   if request.method == "POST":
      pi = user.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')
   
# for update data

def update_data(request, id):
   if request.method == 'POST':
      pi = user.objects.get(pk=id)
      fm = userform(request.POST, instance=pi)
      if fm.is_valid():
          ld = fm.cleaned_data['id']
          nd = fm.cleaned_data['name']
          em = fm.cleaned_data['email']
          pd = fm.cleaned_data['password']
          '''another way of saving data in DB is fm.save()'''
          reg = user(id=ld, name=nd, email=em, password=pd)
          reg.save()
          return HttpResponseRedirect('/')
   else:
      pi = user.objects.get(pk=id)
      fm = userform(instance=pi)
      return render(request, 'enroll/updatestudent.html', {'form':fm})
