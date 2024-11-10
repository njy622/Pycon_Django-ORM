from django.shortcuts import render

# Create your views here.
from django.views.generic import View

# 아래의 다양한 경우의 수로 빨간 줄을 없앨 수 있음
# from ..myapp.models import CustomUser
# from orm.myapp.models import CustomUser
# orm 폴더 우클릭 > 디렉토리 다음으로 표시 > 소스루트 클릭하고 파이참 껐다 키면 빨간줄 없어짐
from myapp.models import CustomUser

from django.forms.models import model_to_dict
from django.http.response import JsonResponse


class UserAPI(View):
    def get(self, *args, **kwargs):
        # 오브젝트를 장고가 직접적으로 만들어 주어서 노란색을 띄워주나 파이참이 버전을
        # 파이참 커뮤니티 버전의 경우는 오브젝트를 인식할 수 없음으로 노란색줄이 뜸
        # 커뮤니티 버전에서도 노란줄 없애고 싶으면 설정 > 장고 > 장고지원 활성화 체킹하면 없어짐
        # 파이참 프로패셔널 버전의 경우에는 오브젝트의 노란색이 안뜸
        # users = [model_to_dict(user) for user in CustomUser.objects.all()]
        # 쿼리를 날려보내는 시점 : CustomUser.objects.all()
        # CustomUser.objects.all() 마치 다 가져올것처럼 했지만
        # 장고에서 가져오는 쿼리의 내용은 더 다양한 타입임. 쿼리를 짤때 한번에
        # 특정 파라미터가 들어왔을때 조건이나 필터가 더 실행될 수 있음
        # 장고의 ORM은 늘 준비해야하기 때문에 CustomUser.objects.all()에서는 대기를 타고
        #

        users = [CustomUser.objects.all()]
        # list(CustomUser.objects.all())
        users = CustomUser.objects.all() 
        # queryset 객체임으로 객체로 선언되고, users라고 변수가 호출되었을때, 쿼리문이 실행됨
        users = [model_to_dict(user) for user in CustomUser.objects.all()]
        # 위의 내용에서는 user 부분에서 호출되는 부분이기 때문에 쿼리문이 실행됨
        # objects => 기존 셋팅된 settings > default 를 가져오는 것이 장고의 기본값
        '''
        DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        '''

        all_users = [model_to_dict(user) for user in CustomUser.objects.all()]


        users = [model_to_dict(user) for user in CustomUser.objects.using('default2')]
        # objects.using('default2') => 기존 셋팅된 settings > default2 를 가져오는 것이 장고의 기본값
        users = [model_to_dict(user) for user in CustomUser.active_objects.using('default2')]



        return JsonResponse(
            {
                "all_users": all_users,
                "users":users
            }
        )
