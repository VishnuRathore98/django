from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User # model class to serialize 
        # fields = ['name', 'age'] # only these two fields are required
        fields = '__all__' # all the fields in model class User is required, if you want to get the id as well which is created but not returned if __all__ is not used, only the mentioned fields are sent and returned for view.
        # exlude = ['age'] # everything except 'age' parameter is required
    
    def validate(self, data):
        schar="`~1!2@3#4$5%6^7&8*9()0_-+=|{}[];:""''\\"
        if any(ch in schar for ch in data['name']):
            raise serializers.ValidationError('name should not contain special chars')

        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')

        return data 
