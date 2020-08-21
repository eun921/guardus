from requests import Response
from rest_auth.registration.views import RegisterView
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView

from accounts import models, serializers
from accounts.models import Profile
from accounts.serializers import GuardusRegistrationSerializer, ProfileSerializer

class GuardusRegistrationView(RegisterView):
    serializer_class = GuardusRegistrationSerializer


class ProfileView(APIView):

    def get(self, request, pk, format=None):
        try:
            user_to_find = models.User.objects.get(pk=pk)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializered = serializers.ProfileSerializer(user_to_find)

        return Response(data=serializered.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):

        me = request.user

        if me.pk != pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        print(request.data)

        serializered = serializers.EditProfileSerializer(me, data=request.data, partial=True)

        if serializered.is_valid():

            serializered.save()
        else:

            print(serializered.errors)

            return Response(data=serializered.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=serializered.data, status=status.HTTP_200_OK)