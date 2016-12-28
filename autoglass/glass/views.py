from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect
from models import *
from forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    try:
        visi = Visitas.objects.get(id='1')

        visi.home = visi.home + 1
        visi.save()

        titulo = "Master AutoGlass"
        template = "home.html"
        slider = Slide.objects.all()
        ban = Mensajeb.objects.all()
        servi = Servicios.objects.all()

        primero1 = ""
        segundo1 = ""
        tercero1 = ""
        contador1 = 0
        f1 = False
        f2 = False
        f3 = False
    except Exception as e:
        raise



    class Sprimero():
        titulo = ""
        tituloinfo = ""
        imagen = ""
        info = ""

    class Ssegundo():
        titulo = ""
        tituloinfo = ""
        imagen = ""
        info = ""

    class Stercero():
        titulo = ""
        tituloinfo = ""
        imagen = ""
        info = ""

    sprimero = Sprimero()
    ssegundo = Ssegundo()
    stercero = Stercero()

    for s1 in servi:
        if s1.valida:
            if s1.orden.orden == "Primero":
                primero1 = s1

                sprimero.titulo = s1.titulo
                print s1.titulo
                info = Info.objects.filter(servicio = s1)
                print info
                for ifo in info:
                    if ifo.orden.orden == 'Primero':
                        print "ENTRE AL PRIMERO _______"
                        sprimero.tituloinfo = ifo.titulo
                        sprimero.info = ifo.informacion
                        sprimero.imagen = ifo.foto.url

                contador1 += 1
                f1 = True
            if s1.orden.orden == "Segundo":
                segundo1 = s1

                ssegundo.titulo = s1.titulo
                print s1.titulo
                infos = Info.objects.filter(servicio = s1)
                print infos
                for ifo in infos:
                    if ifo.orden.orden == 'Primero':
                        print "ENTRE AL SEGUNDO _______"
                        ssegundo.tituloinfo = ifo.titulo
                        ssegundo.info = ifo.informacion
                        ssegundo.imagen = ifo.foto.url
                contador1 += 1
                f2 = True
            if s1.orden.orden == "Tercero":
                tercero1 = s1

                stercero.titulo = s1.titulo
                print s1.titulo
                infot = Info.objects.filter(servicio = s1)
                print infot
                for ifo in infot:
                    if ifo.orden.orden == 'Primero':
                        print "ENTRE AL TERCERO_______"
                        stercero.tituloinfo = ifo.titulo
                        stercero.info = ifo.informacion
                        stercero.imagen = ifo.foto.url
                contador1 += 1
                f3 = True

    if primero1 =="":
        if not segundo1 =="":
            primero1 = segundo1
        elif not tercero1 =="":
            primero1 =tercero1

    if segundo1 =="":
        if not primero1 =="":
            segundo1 = primero1
        elif not tercero1 =="":
            segundo1 =tercero1

    if tercero1 =="":
        if not segundo1 =="":
            tercero1 = segundo1
        elif not primero1 =="":
            tercero1 =primero1









    for b in ban:
        if b.valida:
           ba = b

    primera =""
    segunda = ""
    tercera = ""
    contador = 0

    for s in slider:
        if s.valida:

            if s.orden.orden == "Tercero":
                tercera = s
                contador+=1
            if s.orden.orden == "Segundo":
                segunda = s
                contador+=1
            if s.orden.orden == "Primero":
                primera = s
                contador+=1

    return render_to_response(template,context_instance=RequestContext(request,locals()))


def servicios(request):
    visi = Visitas.objects.get(id='1')

    visi.servi = visi.servi + 1
    visi.save()
    servi =[]

    ser = Servicios.objects.filter(valida = True)

    lisservi = []
    class Servicio():
        sid = ""
        titulo = ""
        tituloinfo = ""
        imagen = ""
        info = ""

    for servi in ser:
        s = Servicio()
        s.titulo = servi.titulo
        s.sid = servi.id
        inf = Info.objects.filter(servicio = servi)
        for f in inf:
            if f.orden.orden == "Primero":
                s.tituloinfo = f.titulo
                s.imagen = f.foto.url
                s.info = f.informacion
        lisservi.append(s)




    titulo = "SERVICIOS"
    template = 'servicios.html'
    return render_to_response(template,context_instance=RequestContext(request,locals()))


def detalleservice(request, idser):
    try:
        servicio = get_object_or_404(Servicios, pk=idser)

        if not servicio.valida:
            ser = Servicios.objects.all()
            fl = True
            for se in ser:
                if se.valida:
                    servicio = se
                    break
        else:
            info = Info.objects.filter(valida = True,servicio = servicio)
            primero = ""
            segundo = ""
            tercero = ""

            for inf in info:
                if inf.orden.orden == 'Primero':
                    primero = inf
                elif inf.orden.orden == 'Segundo':
                    segundo = inf
                elif inf.orden.orden =='Tercero':
                    tercero = inf
                else:
                    pass


    except Exception as e:
        raise
    else:
        pass

    titulo = servicio.titulo
    template = 'servi2.html'
    return render_to_response(template,context_instance=RequestContext(request,locals()))










def contacto(request):
    visi = Visitas.objects.get(id='1')

    visi.contacto = visi.contacto + 1
    visi.save()

    titulo = "Contactenos"
    template = 'contacto.html'
    return render_to_response(template,context_instance=RequestContext(request,locals()))


def fotos(request):
    visi = Visitas.objects.get(id='1')

    visi.fotos = visi.fotos + 1
    visi.save()

    titulo = "Galeria de fots"
    template = "fotos.html"
    fota = Fotos.objects.all()
    fot = []

    for f in fota:
        if f.valida:
            fot.append(f)


    return render_to_response(template,context_instance=RequestContext(request,locals()))


def quienes(request):
    titulo = "Quienes somos"
    c = {'titulo': titulo}
    return render_to_response('quienes.html',c)



def ubicacion(request):
    visi = Visitas.objects.get(id='1')

    visi.mapa = visi.mapa + 1
    visi.save()

    titulo = "Nuestra Ubicacion"
    template = 'ubicacion.html'
    return render_to_response(template,context_instance=RequestContext(request,locals()))


def login(request):
    titulo = "Login"
    c = {'titulo': titulo}
    return render_to_response('login.html',c)



@login_required(login_url = 'home')
def conf(request):
    if request.POST:
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/conf")
    else:
        form = SlideForm()
        sl = Slide.objects.all()

    template = "cofiguraciones.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required(login_url = 'home')
def cfotos(request):
    if request.POST:
        formf = FotosForm(request.POST, request.FILES)
        if formf.is_valid():
            formf.save()
            return HttpResponseRedirect("/cfotos")
    else:
        formf = FotosForm()
        fot = Fotos.objects.all()

    template = "confotos.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required(login_url = 'home')
def cservicios(request):
     if request.POST:
        formser = ServiciosForm(request.POST, request.FILES)
        if formser.is_valid():
            formser.save()
            return HttpResponseRedirect("/cservicios")
     else:
         formser = ServiciosForm()
         servi = Servicios.objects.all()

         class Servis():
             idservi = 0
             tituloservi = ""
             valida = False
             tituloinfo = ""
             info = ""
             imagen = ""
             orden = ""

         listinfo = []

         for s in servi:
             print "ENTRE AL PRIMER FOR_____________"
             ser = Servis()
             ser.idservi =  s.id
             ser.orden = s.orden
             ser.tituloservi = s.titulo
             ifo = Info.objects.filter(servicio = s)
             for inf in ifo:
                 print "ENTRE AL SEGUNDO FOR ______________"
                 if inf.orden.orden == 'Primero':
                     print "ENCONTRE UN PRIMERO_____________________"
                     ser.tituloinfo = inf.titulo
                     ser.imagen = inf.foto.url
                     ser.info = inf.informacion

             ser.valida = s.valida


             listinfo.append(ser)

     template = "confservicios.html"
     return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required(login_url = 'home')
def banner(request):
    if request.POST:
        formb = MensajebForm(request.POST, request.FILES)
        if formb.is_valid():
            formb.save()
            return HttpResponseRedirect("/banner")
    else:
        formb = MensajebForm()
        baner = Mensajeb.objects.all()

    template = "confbanner.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required(login_url = 'home')
def info(request):
    titulo = "Login"
    c = {'titulo': titulo}
    return render_to_response('login.html',c)

@login_required(login_url = 'home')
def ccontacto(request):
    titulo = "Login"
    c = {'titulo': titulo}
    return render_to_response('login.html',c)



@login_required(login_url = 'home')
def slideupdate(request, idslide):
    slide = get_object_or_404(Slide, pk=idslide)
    if request.POST:
        formslide = SlideForm(request.POST, request.FILES, instance=slide)
        if formslide.is_valid():
            formslide.save()
            return HttpResponseRedirect("/conf")
    else:
        formslide = SlideForm(instance=slide)

    template = "slideupdate.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required(login_url = 'home')
def eliminarslide(request, idslide):
    slide = get_object_or_404(Slide,pk=idslide)
    if request.POST:
        slide.delete()
        return HttpResponseRedirect("/conf")

    template = "eliminarslide.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required(login_url = 'home')
def editarfoto(request, idfoto):
    foto = get_object_or_404(Fotos, pk=idfoto)
    if request.POST:
        formfoto = FotosForm(request.POST, request.FILES, instance=foto)
        if formfoto.is_valid():
            formfoto.save()
            return HttpResponseRedirect("/cfotos")
    else:
        formfoto = FotosForm(instance=foto)

    template = "editarfoto.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required(login_url = 'home')
def eliminarfoto(request, idfoto):
    foto = get_object_or_404(Fotos,pk=idfoto)
    if request.POST:
        foto.delete()
        return HttpResponseRedirect("/cfotos")

    template = "eliminarfoto.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))


@login_required(login_url = 'home')
def editarservicio(request, idservi):
    servi = get_object_or_404(Servicios, pk=idservi)
    if request.POST:
        formservi = ServiciosForm(request.POST, request.FILES, instance=servi)
        if formservi.is_valid():
            formservi.save()
            return HttpResponseRedirect("/cservicios")
    else:
        formservi = ServiciosForm(instance=servi)

    template = "editarservicio.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required(login_url = 'home')
def eliminarserivicio(request, idservi):
    servi = get_object_or_404(Servicios,pk=idservi)
    if request.POST:
        servi.delete()
        return HttpResponseRedirect("/cservicios")

    template = "eliminarservicio.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))


@login_required(login_url = 'home')
def editarbanner(request, idbaner):
    ban = get_object_or_404(Mensajeb, pk=idbaner)
    if request.POST:
        formba = MensajebForm(request.POST, request.FILES, instance=ban)
        if formba.is_valid():
            formba.save()
            return HttpResponseRedirect("/banner")
    else:
        formba = MensajebForm(instance=ban)

    template = "editarbanner.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))


@login_required(login_url = 'home')
def eliminarbanner(request, idbaner):
    ban = get_object_or_404(Mensajeb,pk=idbaner)
    if request.POST:
        ban.delete()
        return HttpResponseRedirect("/banner")

    template = "eliminarbanner.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))


@login_required(login_url = 'home')
def agregarinfoservi(request,idservi):
    try:
        print "PASE ENTRE"
        servi = get_object_or_404(Servicios, pk=idservi)

        print "NO ENCONTRE NADA"
        if request.POST:
            print "entre aqui"
            forminfo = InfoForm(request.POST, request.FILES)
            print "saque todo eso"
            if forminfo.is_valid():
                nueva_info = forminfo.save(commit=False)
                nueva_info.servicio = servi
                nueva_info.save()
                print "soy gallo"
                return redirect ("agregarinfoservi",servi.id)
        else:
            forminfo = InfoForm()
            informa = Info.objects.filter(servicio = servi)


            template = "confinfo.html"

            return render_to_response(template,context_instance=RequestContext(request,locals()))
    except Exception as e:
        print e
        return redirect('home')

@login_required(login_url = 'home')
def editarinfoservi(request,idinfo):
    try:
        print "PASE ENTRE"
        info = get_object_or_404(Info,pk = idinfo)

        print "NO ENCONTRE NADA"
        if request.POST:
            print "entre aqui"
            forminfo = InfoForm(request.POST, request.FILES,instance = info)
            print "saque todo eso"
            if forminfo.is_valid():
                forminfo.save()
                print "soy gallo"
                return redirect ("agregarinfoservi",info.servicio.id)
        else:
            forminfo = InfoForm(instance = info)

            template = "editarconfinfo.html"

            return render_to_response(template,context_instance=RequestContext(request,locals()))
    except Exception as e:
        print e
        return redirect('home')
