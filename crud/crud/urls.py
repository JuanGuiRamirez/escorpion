from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crud.views.home', name='home'),
    # url(r'^crud/', include('crud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$','principal.views.index'),#nombre de la acplicacion, archivo de vistas y la vista
    url(r'^add/$', 'principal.views.agregar_producto'),
    url(r'^borrar/(?P<id_producto>\d+)/$', 'principal.views.borrar_producto'),
    url(r'^editar/(?P<id_producto>\d+)/$', 'principal.views.editar_producto'),
)
