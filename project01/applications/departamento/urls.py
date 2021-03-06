from django.urls import path


def DesdeApps(self):
    print(' ======================= Desde la app departamento ==========================')


urlpatterns = [
    path('departamento/', DesdeApps),
]
