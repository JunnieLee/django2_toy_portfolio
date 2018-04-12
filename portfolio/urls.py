
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')), #만약 주소가 blog/ 뒤에 쌸라쌸라 이렇게 있는거면, blog/urls.py 파일에 있는 url 정보를 참고해라!!
                                         #이런식으로 하면 각 app들에 대해 세부 url들을 따로따로 깔끔하게 관리할 수 있겠지!
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
