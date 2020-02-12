from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    ''' serializes  a name field for testing apiview'''

    name = serializers.CharField(max_length=10)

#field and model configurations
class UserProfileSerializer(serializers.ModelSerializer):
    '''serializes a user profile object'''

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        '''create and returns a new user'''

        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user


#serializer for user profiles
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''serializes profile  feed items'''

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
