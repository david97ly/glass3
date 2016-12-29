from django.conf.urls import include, url
from django .conf import settings
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    # Examples:
    url(r'^$', 'glass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^servicios', 'glass.views.servicios', name='servicios'),
    url(r'^detalleservice/(\d+)$', 'glass.views.detalleservice', name='detalleservice'),
    url(r'^contacto', 'glass.views.contacto', name='contacto'),
    url(r'^fotos', 'glass.views.fotos', name='fotos'),
    url(r'^quienes', 'glass.views.quienes', name='quienes'),
    url(r'^ubicacion', 'glass.views.ubicacion', name='ubicacion'),
    url(r'^login', 'glass.views.login', name='login'),
    url(r'^conf', 'glass.views.conf', name='conf'),
    url(r'^cfotos', 'glass.views.cfotos', name='cfotos'),
    url(r'^cservicios', 'glass.views.cservicios', name='cservicios'),
    url(r'^banner', 'glass.views.banner', name='banner'),
    url(r'^info', 'glass.views.info', name='info'),
    url(r'^gallery', 'glass.views.gallery', name='gallery'),
    url(r'^ccontacto', 'glass.views.ccontacto', name='ccontacto'),
    url(r'^slideupdate/(\d+)$', 'glass.views.slideupdate', name='slideupdate'),
    url(r'^agregarinfoservi/(\d+)$', 'glass.views.agregarinfoservi', name='agregarinfoservi'),
    url(r'^editarinfoservi/(\d+)$', 'glass.views.editarinfoservi', name='editarinfoservi'),
    url(r'^eliminarslide/(\d+)$', 'glass.views.eliminarslide', name='eliminarslide'),
    url(r'^eliminarfoto/(\d+)$', 'glass.views.eliminarfoto', name='eliminarfoto'),
    url(r'^editarfoto/(\d+)$', 'glass.views.editarfoto', name='editarfoto'),
    url(r'^eliminarinfo/(\d+)$', 'glass.views.eliminarinfo', name='eliminarinfo'),
    url(r'^eliminarserivicio/(\d+)$', 'glass.views.eliminarserivicio', name='eliminarserivicio'),
    url(r'^editarservicio/(\d+)$', 'glass.views.editarservicio', name='editarservicio'),
    url(r'^eliminarbanner/(\d+)$', 'glass.views.eliminarbanner', name='eliminarbanner'),
    url(r'^editarbanner/(\d+)$', 'glass.views.editarbanner', name='editarbanner'),

       url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
]
