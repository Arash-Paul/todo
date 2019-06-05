from .models import UserModel
from django.core.serializers import serialize
import json


class UserSerializeMixin(object):
    def serialize(self, query_set):
        json_data = serialize('json', query_set)
        dict = json.loads(json_data)
        final_list = []
        for obj in dict:
            record = obj['fields']
            # record = {
            #     'pk': object['pk'],
            #     'username':
            # }
            final_list.append(record)
        json_data = json.dumps(final_list)
        return json_data

