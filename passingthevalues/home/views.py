from django.shortcuts import render

# Create your views here.
def rendaringdata(request):
    emp1=["nani","mt581",'python']
   

    
 
    emp2=['nbvjb','hj2342','jn bn ']
    
    

    
    context={'data':emp1}
    context1={'data1':emp2}
    
    return render(request,'home.html',context)
    return render(request,'home.html',context1)
