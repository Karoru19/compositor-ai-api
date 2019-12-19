from rest_framework import viewsets


class ReadUpdateSerializerMixin:
    serializer_class = None
    read_serializer_class = None
    update_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'create':
            return self.serializer_class
        if self.action == 'update':
            return self.update_serializer_class
        return self.read_serializer_class
