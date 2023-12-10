from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import todo_item
from django.contrib.auth.models import User
from django.core.serializers import serialize
@api_view(['GET','POST','PUT','DELETE'])
def functionality(request):
    if not request.user.is_authenticated:
        return Response({"user not login"})
    if request.method=="POST":
        if "tag" not in request.POST:
            request.POST["tag"]=""
        if "due_date" not in request.POST:
            request.POST["due_date"]=date(9999,12,31)
        try:
            obj=todo_item.objects.create(username=request.user.username,title = request.POST['title'] ,  description=request.POST['description'] , tag=request.POST['tag']  , due_date=request.POST['due_date'] )
            obj.save()
            return Response({"entry saved successfully"})
        except Exception as e:
            return Response({"Invalid Input"})
    elif request.method =="GET":
        data=request.GET
        if 'timestamp' in data:
            queryset = todo_item.objects.filter(username=request.user.username,timestamp=data["timestamp"])
            serialized_data = serialize('json', queryset)
            return Response(serialized_data)
        else:
            queryset = todo_item.objects.filter(username=request.user.username)
            serialized_data = serialize('json', queryset)
            return Response(serialized_data)
    elif request.method=="PUT":
        data=request.PUT
        if 'timestamp' in data:
            queryset = todo_item.objects.filter(username=request.user.username,timestamp=data["timestamp"])
            if queryset:
                query=queryset[0]
                for x in data:
                    try:
                        query.x=data[x]
                    except:
                        continue
                query.save()
                
                return Response({"changes successful"})
            else:
                return Response({"invalid input"})
        else:
            
            return Response({"invalid input"})
    elif request.method=="DELETE":
        if 'timestamp' in data:
            queryset = todo_item.objects.filter(username=request.user.username,timestamp=data["timestamp"])
            if queryset:
                query=queryset[0]
                query.delete()
                
                return Response({"deleted successfully"})
            else:
                return Response({"invalid input"})
        else:
            return Response({"invalid input"})
        
    else:
        return Response({"invalid request"})
@api_view(['POST'])
def user_create(request):
    print(1)
    print(request.POST)
    if request.method=="POST":
        data=request.POST
        if not ("username" in data and "password" in data):
            return Response(request)
        if User.objects.filter(username=data["username"]).exists():
            return Response({"username already taken"})
        else:
            t=User.objects.create(username=data['username'])
            t.set_password(data["password"])
            t.save()
            return Response({"user created successfully"})
            
    else:
        return  Response({"invalid request"})
@api_view(['POST'])
def user_login(request):
    if request.method=="POST":
        data=request.POST
        if not ("username" in data and "password" in data):
            return Response({"invalid request,argument(s) missing"})
        user=authenticate(request,username=data["username"],password=data["password"])
        if user :
            login(request,user)
            return Response({"login successfully"})
            
        else:
            return  Response({"invalid credentials"})
    else:
        return  Response({"invalid request"})
        