from django.urls import path, include
from . import django_fbv, drf_fbv, drf_cbv, drf_mixin
# 1. snippets.urls.__init__의 내용을 수정해서
#   /django-fbv/snippets/
#   /django-fbv/snippets/<pk>/
#   가 동작하도록 작성


# 2. 위의 'django-fbv'가 들어간 URL로 기존 Postman API들의 URL수정
# 3. 2장의 내용을 Postman에서
#    /drf-fbv/snippets/
#    /drf-fbv/snippets/<pk>/
#    에서 처리할 수 있도록 코드 작성 후
#    Postman의 Collections내부 새 폴더(drf-fbv)에 총 6개 API등록
#     (List, Create, Retrieve, Update, Update(partial), Delete)

urlpatterns = [
    path('django-fbv/', include(django_fbv)),
    path('drf-fbv/', include(drf_fbv)),
    path('drf-cbv/', include(drf_cbv)),
    path('drf-mixin/', include(drf_mixin)),
]


# 문자열인 경우에는 절대경로만 (상대경로는 안된다.)