# Create your views here.
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import Profile, AcademyGroup, SchoolGroup
from users.serializers import ProfileListSerializer, ProfileDetailSerializer, SchoolGroupSerializer, \
    AcademyGroupSerializer
from words.models import Textbook
from words.serializers import TextbookSerializer, TextbookListSerializer


class ProfileList(ListCreateAPIView):
    """
    get: 유저 전체요청
    post: 회원가입
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer

    # def post(self):


class ProfileDetail(RetrieveUpdateDestroyAPIView):
    # class ProfileDetail(GenericAPIView):
    """
    get: 유저 상세기록 요청
    put: 유저 상세기록 수정
    delete: 회원 탈퇴
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer

    # def get(self, request, *args, **kwagrs):
    #     serializer = ProfileDetailSerializer(data=self.request.data)
    #     user_id = kwagrs['pk']
    #     print(user_id)
    #     user = Profile.objects.get(id=user_id)
    #     academy_code = user.academy_code
    #     school_code = user.school_code
    #
    #     queryset_academy = Textbook.objects.filter(academy_code=academy_code)
    #     queryset_school = Textbook.objects.filter(school_code=school_code)
    #
    #     res = {
    #         'academy': queryset_academy
    #     }
    #     return Response(res, status=200, content_type="application/json")


class UserTextbookList(generics.ListAPIView):
# class UserTextbookList(GenericAPIView, mixins.ListModelMixin):
    """
    get: 해당 유저가 볼수있는 교과서들 출력
    """

    serializer_class = TextbookListSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        user = Profile.objects.get(user_id=user_id)
        academy_code = user.academy_code_id
        school_code = user.school_code_id

        # 공통으로 볼수있는교과서 추가해서 출력 필요함.
        from django.db.models import Q
        return Textbook.objects.filter(Q(academy_code=academy_code), Q(school_code=school_code))

    # def get(self, request, *args, **kwagrs):
    #     user_id = kwagrs['pk']
    #     user = Profile.objects.get(user_id=user_id)
    #     # print(user)
    #     academy_code = user.academy_code_id
    #     # print(academy_code)
    #     school_code = user.school_code_id
    #     # print(school_code)
    #     queryset = Textbook.objects.filter(academy_code=academy_code)
    #     # queryset_academy = Textbook.objects.filter(academy_code=academy_code)
    #     # queryset_school = Textbook.objects.filter(school_code=school_code)
    #     # res = {
    #     #     'academy_code':  queryset_academy,
    #     #     # 'academy_code':  user.academy_code_id,
    #     #     # 'school_code':  user.school_code_id,
    #     # }
    #     # return Response(queryset_academy, status=200, content_type="application/json")
    #     # return queryset_academy
    #     return self.list(request, *args, **kwagrs)


class SchoolGroupList(ListCreateAPIView):
    """
    get: 전체 학교리스트
    post: 학교 추가
    """
    queryset = SchoolGroup.objects.all()
    serializer_class = SchoolGroupSerializer


class SchoolGroupDetail(RetrieveUpdateDestroyAPIView):
    """
    get: 특정 학교 정보 조회
    put: 특정 학교 정보 수정
    delete: 특정 학교 삭제
    """
    queryset = SchoolGroup.objects.all()
    serializer_class = SchoolGroupSerializer


class AcademyGroupList(ListCreateAPIView):
    """
    get: 전체 학원 리스트
    post: 학원 추가
    """
    queryset = AcademyGroup.objects.all()
    serializer_class = AcademyGroupSerializer


class AcademyGroupDetail(RetrieveUpdateDestroyAPIView):
    """
    get: 특정 학원 정보 조회
    put: 특정 학원 정보 수정
    delete: 특정 학원 삭제
    """
    queryset = AcademyGroup.objects.all()
    serializer_class = AcademyGroupSerializer
