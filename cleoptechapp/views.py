from django.shortcuts import render,redirect
from .models import Product,comment
from math import ceil
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages


def home (request):
    return render(request,'home.html')

def products (request):
    current_uesr=request.user 
    print(current_uesr)
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats :
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        sslides=n // 4 + ceil((n/4) -(n//4))
        allprods.append([prod,range(1,sslides),sslides])
    params={'allprods':allprods}
    return render(request,'products.html',params)
def details(request,pk):
    product=Product.objects.get(id=pk)
    
    comm=comment.objects.filter(product_id=pk)
    num=len(comm)
    
    return render(request,'details.html',{'product':product,'comment':comm,"num":num})
def addcomment(request,id):
    url=request.META.get('HTTP_REFERER') # LAST PAGE
    
    if request.method=='POST':
        
        newbody=request.POST["body"]
        
        currentuser=request.user 
        nproduct=id
        nuser=currentuser.id
        comment.objects.all()
        
        newcomment=comment()
        newcomment.body=newbody
        newcomment.product_id=nproduct
        newcomment.user_id=nuser
        
        newcomment.save()

        messages.success(request,"you has been added new comment")
    
        return redirect(url)
    return redirect(url)        
            
            
    


       
    
    