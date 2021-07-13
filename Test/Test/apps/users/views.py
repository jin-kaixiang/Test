from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from users.models import Author,Book
import json
# Create your views here.

class CreateAuthor(View):
    def post(self,request):
        # 获取json数据
        json_dict = json.loads(request.body.decode())
        name = json_dict.get('name')
        gender = json_dict.get('gender')
        born_date = json_dict.get('born_date')

        #保存数据
        try:
            user =  Author.objects.create_user(name=name,
                                             gender=gender,
                                             born_date=born_date)
        except Exception as e:
            return JsonResponse({
                'code':400,
                'errmsg':e
            })
        return JsonResponse({
            'code':200,
            'errmsg':'ok'
        })

    def get(self,request):
        # 获取json数据
        json_dict = json.loads(request.body.decode())
        name = json_dict.get('name')

        # 查询数据
        try:
            author = Author.objects.get(name=name)
        except Exception as e:
            return JsonResponse({
                'code':400,
                'errmsg':e
            })

        author_message = {
            'name':author.name,
            'gender':author.gender,
            'born_date':author.born_date
        }
        return JsonResponse({
            'code':200,
            'data':author_message
        })





class CreateBook(View):
    def post(self, request):
        # 获取json数据,
        json_dict = json.loads(request.body.decode())
        hauthor_id = json_dict.get('hauthor_id')
        publish_date = json_dict.get('publish_date')
        Country = json_dict.get('Country')
        # 保存数据
        try:
            user = Book.objects.create_user(hauthor_id=hauthor_id,
                                              publish_date=publish_date,
                                              Country=Country)
        except Exception as e:
            return JsonResponse({
                'code': 400,
                'errmsg': e
            })
        return JsonResponse({
            'code': 200,
            'errmsg': 'ok'
        })

    def get(self, request):
        # 获取json数据
        json_dict = json.loads(request.body.decode())
        name = json_dict.get('name')

        # 查询数据
        try:
            book = Book.objects.get(name=name)
        except Exception as e:
            return JsonResponse({
                'code': 400,
                'errmsg': e
            })
        message = {
            'author_name': book.hauthor.name,
            'author_gender': book.hauthor.gender,
            'author_born_date': book.hauthor.born_date,
            'book_name':book.name,
            'book_country':book.country,
            'book_publish_date':book.publish_date
        }
        return JsonResponse({
            'code': 200,
            'data': message
        })