from rest_framework.serializers import ModelSerializer

from .models import Profile, SchoolGroup, AcademyGroup


class ProfileListSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'grade', 'school_code', 'academy_code',)
        depth = 2


class ProfileDetailSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'grade', 'school_code', 'academy_code',)
        depth = 2


class SchoolGroupSerializer(ModelSerializer):
    class Meta:
        model = SchoolGroup
        fields = ('code', 'name',)



class AcademyGroupSerializer(ModelSerializer):
    class Meta:
        model = AcademyGroup
        fields = ('code', 'name',)
