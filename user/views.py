from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import UserModel
from .mixins import UserSerializeMixin
from django.http import HttpResponse
from task.utils import is_json
import json
from .forms import UserForm

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch') # class csrf_exempt
class UserView(View, UserSerializeMixin):
    def get(self, request):
        query_set = UserModel.objects.all()
        # json_data = UserModelSerializer(queryset, many=True)
        json_data = self.serialize(query_set)
        return HttpResponse(json_data, content_type='application/json', status=200)

    def post(self, request):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Invalid JSON data!'})
            return HttpResponse(json_data, content_type='application/json', status=400)
        user_data = json.loads(data)
        user_form = UserForm(user_data)
        if user_form.is_valid():
            user_form.save(commit=True)
            json_data = json.dumps({'msg': 'Saved Successfully.'})
            return HttpResponse(json_data, content_type='application/json', status=200)
        if user_form.errors:
            json_data = json.dumps(user_form.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)
