from django.core.serializers import serialize
from task.models import Task
import json


class TaskSerializeMixin(object):
    def serialize(self, query_set):
        json_data = serialize('json', query_set)
        dict = json.loads(json_data)
        final_list = []
        for obj in dict:
            record = obj['fields']
            final_list.append(record)
        json_data = json.dumps(final_list)
        return json_data

    class Meta:
        model = Task
        fields = '__all__'

