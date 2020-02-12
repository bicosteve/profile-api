from rest_framework import permissions


#restricts users from making changes to other user profiles
class UpdateOwnProfile(permissions.BasePermission):
    '''Allow user to edit their own profile'''

    def has_object_permission(self, request, view, object):
        '''check if use is trying to edit their own profile'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    '''allow users to update their own profile'''

    def has_object_permission(self,request,view, object):
        '''check the user is trying to update own status'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.user_profile.id == request.user.id
