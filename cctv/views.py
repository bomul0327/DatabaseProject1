from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import FilesForm

from .models import Manager, Shoot_space, CCTV, Shoot, Files, Neighborhood, Sequence, Statistics, Record #DB Table과 HTML을 연결해주는 역할
#테이블 이름은 cctv_'객체명' , eg: cctv_manager, cctv_shoot_space ...
from django.db import connection #SQL로 insert into, delete, update를 하기위하여 필요.
#from .forms import manager_manage_form #사용안함
from django.http import HttpResponse

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def login(request):
    request.session['login_sess'] = 'cctv'
    return render(request, 'cctv/login.html', {})
    #return HttpResponse('[%s] logged in successfully' % request.session['login_sess'])

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def logout(request):
    del request.session['login_sess']
    return HttpResponse('logged out successfully')
    #return render(request, 'cctv/login.html', {})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
@login_required
def shoot_space_manage(request): #여기 작성중 12-05 오후 12:20
    space_list = Shoot_space.objects.raw('SELECT id, dong, building_name, flr, location FROM cctv_shoot_space')
    if request.method == "POST" and request.POST['mode'] =="select":
        shoot_space_list = Shoot_space.objects.raw('SELECT cc.id, ss.id AS space_id , ss.dong, ss.building_name, ss.flr, ss.location FROM cctv_shoot_space AS ss, cctv_shoot AS sh, cctv_cctv AS cc WHERE ss.id = sh.Shoot_space_id_id AND cc.id = sh.CCTV_id_id AND cc.manager_id = %s', [request.user.username])
        cctv_list = CCTV.objects.raw('SELECT id, model_name, install_date, manager_id FROM cctv_cctv WHERE manager_id = %s', [request.user.username])
        return render(request, 'cctv/shoot_space_manage.html', {'space_list' : space_list, 'shoot_space_list' : shoot_space_list, 'cctv_list' : cctv_list})
    with connection.cursor() as form:
        form = connection.cursor()
        if request.method == "POST" and request.POST['mode'] =="insert" :
            #문제점 : install_date 타입이 DateTimeField 인데 이게 입력이 잘 안됩니다.
            #shoot = Shoot.objects.raw('SELECT cctv_id_id FROM cctv_shoot WHERE cctv_id_id = %s', [request.POST['cctv_id']])
            #if(shoot.___str___ == "") #shoot.___str___이 cctv_id_id 를 리턴하는가 확인. 윗줄과 이거 주석 해제하고 아래 form 한칸 들여쓰기
            form.execute("INSERT INTO cctv_shoot ('cctv_id_id', 'shoot_space_id_id') VALUES(%s, %s)", [request.POST['cctv_id'], request.POST['shoot_space_id']] )
        elif request.method == "POST" and request.POST['mode'] =="delete" :
            form.execute('DELETE FROM cctv_shoot WHERE cctv_id_id = %s AND shoot_space_id_id = %s', [request.POST['cctv_id'], request.POST['shoot_space_id']])
            #form.execute('DELETE FROM cctv_shoot WHERE cctv_id_id = %s AND shoot_space_id_id = %s', [[request.POST['cctv_id'], request.POST['shoot_space_id']])
        elif request.method == "POST" and request.POST['mode'] == "update" :
            cctv_id = request.POST['cctv_id']
            shoot_space_id = request.POST['shoot_space_id']
            form.execute("UPDATE cctv_shoot SET shoot_space_id_id = %s WHERE cctv_id_id = %s", [shoot_space_id, cctv_id] )
    return render(request, 'cctv/shoot_space_manage.html', {'space_list' : space_list })

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
@login_required
def file_manage(request):
    if request.method == "GET":
        form = FilesForm()
    elif request.method == "POST":
        form = FilesForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return render(request, 'cctv/file_manage.html')
    files_list = Files.objects.raw(
        'SELECT file_name, file, CCTV_id_id, Shoot_space_id_id, start_time, end_time FROM cctv_files')
    ctx = {'files_list': files_list, 'form': form,}
    return render(request, 'cctv/file_manage.html', ctx)

    files_list = Files.objects.raw('SELECT file_name, CCTV_id_id, Shoot_space_id_id, start_time, end_time FROM cctv_files')
    if request.method == "POST" and request.POST['mode'] =="select":
        cctv_id = request.POST['cctv_id']         # 여기부터
        if cctv_id == "":                            # 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            cctv_id = "%"                            # 여기까지
        shoot_space_id = request.POST['shoot_space_id']                       # 여기부터
        if shoot_space_id == "":                                   # 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            shoot_space_id = "%"                                   # 여기까지
        start_time = request.POST['start_time']             # 여기부터
        if start_time == "":                              # 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            start_time = "%"                              # 여기까지
        end_time = request.POST['end_time']             # 여기부터
        if end_time == "":                              # 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            end_time = "%"                              # 여기까지
        files_list = Files.objects.raw('SELECT file_name, CCTV_id_id, Shoot_space_id_id, start_time, end_time FROM cctv_files WHERE CCTV_id_id like %s AND Shoot_space_id_id like %s AND start_time like %s AND end_time like %s', [cctv_id, shoot_space_id, start_time, end_time])
    with connection.cursor() as form:
        form = connection.cursor()
        if request.method == "POST" and request.POST['mode'] =="insert" :
            form.execute("INSERT INTO cctv_files ('file_name', 'start_time', 'end_time', 'CCTV_id_id', 'Shoot_space_id_id') VALUES(%s, %s, %s, %s, %s)", [request.POST['file_name'], request.POST['start_time'], request.POST['end_time'], request.POST['cctv_id'], request.POST['shoot_space_id']] )
            # CCTV_id_id 나 Shoot_space_id_id 에 값이 안들어가는 경우(존재 하지 않는 CCTV ID나 Space ID 입력한 경우) 삭제
            #form.execute("DELETE FROM cctv_files WHERE CCTV_id_id IS NULL OR Shoot_space_id_id IS NULL")
    return render(request, 'cctv/file_manage.html', {'files_list': files_list})

@login_required
#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def log_read(request):
    return render(request, 'cctv/log_read.html', {})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
@login_required
def my_page(request):
    if request.method == "POST" and request.POST['mode'] =="select":
        manager = Manager.objects.raw('SELECT id, pos, phonenum FROM cctv_manager WHERE id = %s', [request.POST['manager_id']])
        cctv_list = CCTV.objects.raw('SELECT id, manager_id FROM cctv_cctv WHERE manager_id = %s', [request.POST['manager_id']])
        return render(request, 'cctv/my_page.html', {'manager' : manager, 'cctv_list' : cctv_list})
    with connection.cursor() as form:
        form = connection.cursor()
        if request.method == "POST" and request.POST['mode'] =="update" :
            pos = request.POST['pos']
            phonenum = request.POST['phonenum']
            if pos == "" and phonenum != "":
                form.execute("UPDATE cctv_manager SET phonenum = %s WHERE id = %s", [phonenum, request.POST['manager_id']] )
            elif pos != "" and phonenum == "":
                form.execute("UPDATE cctv_manager SET pos = %s WHERE id = %s", [pos, request.POST['manager_id']] )
            elif pos != "" and phonenum != "":
                form.execute("UPDATE cctv_manager SET pos = %s, phonenum = %s WHERE id = %s", [pos, phonenum, request.POST['manager_id']] )
    return render(request, 'cctv/my_page.html', {'form' : form})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
@login_required
#최고관리자
def manager_manage(request):
    if request.user.is_authenticated:
        if not request.user.is_staff == True:
            return shoot_space_manage(request)
    manager_list = Manager.objects.raw('SELECT distinct manager.id, manager.pos, manager.phonenum FROM cctv_manager AS manager LEFT OUTER JOIN cctv_cctv AS cctv ON manager.id = cctv.manager_id WHERE manager.id NOT IN ("admin")')
    if request.method == "POST" and request.POST['mode'] =="select":
        manager_id = request.POST['manager_id']         # 여기부터
        if manager_id == "":                            # 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            manager_id = "%"                            # 여기까지
        pos = request.POST['pos']                       # 여기부터
        if pos == "":                                   # 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            pos = "%"                                   # 여기까지
        phonenum = request.POST['phonenum']             # 여기부터
        if phonenum == "":                              # 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            phonenum = "%"                              # 여기까지
        cctv_id = request.POST['cctv_id']
        if cctv_id == "" and (manager_id == "%" and pos == "%" and phonenum =="%"):  #검색 칸이 전부 빈공간인 경우 전체 검색
            manager_list = Manager.objects.raw('SELECT distinct manager.id, manager.pos, manager.phonenum FROM cctv_manager AS manager LEFT OUTER JOIN cctv_cctv AS cctv ON manager.id = cctv.manager_id WHERE manager.id NOT IN ("admin")')
            return render(request, 'cctv/manager_manage.html', {'manager_list' : manager_list})
        if cctv_id == "" and not(manager_id == "%" and pos == "%" and phonenum =="%"):  #관리 CCTV ID 칸만 빈칸인 경우 cctv_id 는 조건절에서 제외하고 검색
            manager_list = Manager.objects.raw('SELECT distinct manager.id, manager.pos, manager.phonenum FROM cctv_manager AS manager LEFT OUTER JOIN cctv_cctv AS cctv ON manager.id = cctv.manager_id WHERE manager.id like %s AND manager.pos like %s AND manager.phonenum like %s', [manager_id, pos, phonenum])
            return render(request, 'cctv/manager_manage.html', {'manager_list' : manager_list})
        manager_list = CCTV.objects.raw('SELECT distinct manager.id, manager.pos, manager.phonenum FROM cctv_manager AS manager LEFT OUTER JOIN cctv_cctv AS cctv ON manager.id = cctv.manager_id WHERE manager.id like %s AND manager.pos like %s AND manager.phonenum like %s AND cctv.id like %s', [manager_id, pos, phonenum, cctv_id])
    with connection.cursor() as form:
        form = connection.cursor()
        if request.method == "POST" and request.POST['mode'] =="insert" :
            form.execute("INSERT INTO cctv_manager ('id', 'pw', 'pos', 'phonenum') VALUES(%s, %s, %s, %s)", [request.POST['insert_id'], request.POST['pw'], request.POST['pos'], request.POST['phonenum']] )
        elif request.method == "POST" and request.POST['mode'] =="delete" :
            form.execute('DELETE FROM cctv_manager WHERE id = %s AND id NOT IN ("admin")', [request.POST['delete_id']] )
    return render(request, 'cctv/manager_manage.html', {'manager_list' : manager_list, 'form': form})


#def insert_sql(self):
#    with connection.cursor() as cursor:
#        cursor.execute("INSERT INTO cctv_manager ('id', 'pw', 'pos', 'phonenum') VALUES(%s, %s, %s, %s)", [self.id], [self.pw], [self.pos], [self.phonenum])
#        row = cursor.fetchone()
#    return row

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
@login_required
def post_new(request):
    form = manager_manage_form()
    return render(request, 'cctv/post_edit.html', {'form': form})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
#최고관리자
@login_required
def cctv_manage(request):
    if request.user.is_authenticated:
        if not request.user.is_staff == True:
            return shoot_space_manage(request)
    cctv_list = CCTV.objects.raw('SELECT id, model_name, install_date, manager_id FROM cctv_cctv')
    if request.method == "POST" and request.POST['mode'] =="select":
        model_name = request.POST['model_name'] # 여기부터
        if model_name == "":                    # model_name에 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            model_name = "%"                    # 여기까지
        manager_id = request.POST['manager_id'] # 여기부터
        if manager_id == "":                    # manager_id에 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            manager_id = "%"                    # 여기까지
        install_date = request.POST['install_date'] # 여기부터
        if install_date == "":                    # install_date에 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            install_date = "%"                    # 여기까지
        cctv_list = CCTV.objects.raw('SELECT id, model_name, install_date, manager_id FROM cctv_cctv WHERE model_name like %s AND manager_id like %s AND install_date like %s', [model_name, manager_id, install_date])
    with connection.cursor() as form:
        form = connection.cursor()
        if request.method == "POST" and request.POST['mode'] =="insert" :
            #문제점 : install_date 타입이 DateTimeField 인데 이게 입력이 잘 안됩니다.
            form.execute("INSERT INTO cctv_cctv ('id', 'model_name', 'manager_id', 'install_date') VALUES(%s, %s, %s, %s)", [request.POST['insert_id'], request.POST['model_name'], request.POST['manager_id'], request.POST['install_date']] )
        elif request.method == "POST" and request.POST['mode'] =="delete" :
            form.execute('DELETE FROM cctv_cctv WHERE id = %s', [request.POST['delete_id']])
    return render(request, 'cctv/cctv_manage.html', {'cctv_list' : cctv_list, 'form': form})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
#최고관리자
@login_required
def space_manage(request):
    if request.user.is_authenticated:
        if not request.user.is_staff == True:
            return shoot_space_manage(request)
    space_list = Shoot_space.objects.raw('SELECT id, dong, building_name, flr, location FROM cctv_shoot_space')
    with connection.cursor() as form:
        form = connection.cursor()
        if request.method == "POST" and request.POST['mode'] =="insert" :
            #문제점 : install_date 타입이 DateTimeField 인데 이게 입력이 잘 안됩니다.
            form.execute("INSERT INTO cctv_shoot_space ('id', 'dong', 'building_name', 'flr', 'location') VALUES(%s, %s, %s, %s, %s)", [request.POST['shoot_space_id'], request.POST['dong'], request.POST['building_name'], request.POST['flr'], request.POST['location']] )
        elif request.method == "POST" and request.POST['mode'] =="delete" :
            form.execute('DELETE FROM cctv_shoot_space WHERE id = %s', [request.POST['shoot_space_id']])
    return render(request, 'cctv/space_manage.html', {'space_list' : space_list})
