from django.db import models

# Create your models here.



class CustomUserManager(models.Manager):

    # CustomUser.objects.all()
    # CustomUser : 모델
        # 테이블을 어떻게 가져올지 작성하는 것  Manager (어떤 서식으로 가져올지)
    # objects : manager
        # 데이터셋을 어떻게 들고 올지 정하는것, 집합자체를 정의하는것을 manager라고 하는것
    # all() : QuerySet
        # 어떻게 조합해서 가져올지는 QuerySet,

    def active_users(self):
        return self.filter(is_activate=True)

    def get_queryset(self):
        return super().get_queryset().filter(is_activate=True)


class CustomUser(models.Model):
    '''

        CREATE TABLE "myapp_customuser"
    (
        "id"         integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
        "username"   varchar(50)  NOT NULL UNIQUE,
        "password"   varchar(255) NOT NULL,
        "email"      varchar(100) NOT NULL UNIQUE,
        "created_at" datetime     NOT NULL,
        "updated_at" datetime     NOT NULL
    );
    '''


    # 장고에서는 ORM들이 ID필드가 없음에도 불구하고 id라는 컬럼이 생김,
    # 일반적인 id라는 컬럼은 프라이머리키가 들어가야 함
    # 언제나 id값을 들어갈 것을 대비해서 id라는 필드를 정의할 필요가 없음
    # 장고는 그런 필드의 메커니즘을 가지고 있음
    # id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=50, unique=True, verbose_name="사용자 이름")
    # varchar 캐릭터 타입을 하나하나 신경쓰지 않기때문에, 장고는 언제나 Varchar()를 사용함
    # 당장 만들때는 그냥 varchar()를 사용하는게 맞음
    password = models.CharField(max_length=255, verbose_name="비밀번호")
    email = models.EmailField(max_length=100, unique=True, verbose_name="이메일")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    is_activate = models.BooleanField(
        default=True,db_default=True, verbose_name="활성 여부"
    )
    # is_activate를 임시로 디폴트값을 어떻게 다룰 것인지 신경쓰면서 정의하며 만들어야함
    # default=True 값을 통해, db 마이그레이션을 진행함으로써 배포를 언제할 수 있을지 모르는 애매한 상황을 대비해서, 명확히 구분하고 마이그레이션 해야함
    # db_default값이 없으면 DB에서는 default 값이 없어서 오류가 남,
    # 4버전까지는 무조건 오류가 났었음(구버전)
    # 5버전부터는 오류가 나지 않음

    active_objects = CustomUserManager()

    class Meta:
        verbose_name = "유저 목록"

    def __str__(self):
        return self.username

    def send_mail(self):
        print(f"Sending email to {self.email}")
