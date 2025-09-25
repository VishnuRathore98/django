from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User # model class to serialize 
        # fields = ['name', 'age'] # only these two fields are required
        fields = '__all__' # all the fields in model class User is required, if you want to get the id as well which is created but not returned if __all__ is not used, only the mentioned fields are sent and returned for view.
        # exlude = ['age'] # everything except 'age' parameter is required

