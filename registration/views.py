# coding: UTF-8
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from backend.decorators import check_auth
from django.contrib.auth import logout
from backend.logging import loginfo
from django.shortcuts import render_to_response
from django.template import RequestContext
from const import ADMINSTAFF_USER
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.sites.models import get_current_site
from django.template.response import TemplateResponse

def loginviews(request):
    return render(request,"login.html")

def login_redirect(request,identity):
    """
    When the user login, it will decide to jump the according page, in other
    words, school user will be imported /school/ page, if the user have many
    authorities, the system will jump randomly
    """
    #TODO: I will use reverse function to redirect, like school and expert

    # print "ENTERING LOGIN_DIRECT"
    loginfo(identity) #日志相关，与auth无关
    if check_auth(request.user,identity): # 只验证 user 和 identity 是否匹配？ 密码呢？
        loginfo(request.user)
        pass
    else:
        # print "LOGIN FAILED!"
        try:
            del request.session['auth_role']
        except:
            pass
        logout(request)
        return HttpResponseRedirect('/identityerror')
    if identity==ADMINSTAFF_USER:
        redirect_url = '/'+identity+'/'+"studentmanage"
    else:
        redirect_url = '/'+identity+'/'+"homepage"
    request.session['auth_role'] = identity
    return HttpResponseRedirect(redirect_url)

def logout_redirect(request):
    try:
        del request.session['auth_role']
    except KeyError:
        pass
    return HttpResponseRedirect('/')



    
