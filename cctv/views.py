from django.shortcuts import render
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
def shoot_space_manage(request):
    return render(request, 'cctv/shoot_space_manage.html', {})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def file_manage(request):
    return render(request, 'cctv/file_manage.html', {})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def log_read(request):
    return render(request, 'cctv/log_read.html', {})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def my_page(request):
    return render(request, 'cctv/my_page.html', {})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def manager_manage(request):
    manager_list = Manager.objects.raw('SELECT id, pos, phonenum from cctv_manager WHERE id NOT IN ("admin")')
    with connection.cursor() as form:
        form = connection.cursor()
        if request.method == "POST" and request.POST['mode'] =="insert" :
            form.execute("INSERT INTO cctv_manager ('id', 'pw', 'pos', 'phonenum') VALUES(%s, %s, %s, %s)", [request.POST['insert_id'], request.POST['pw'], request.POST['pos'], request.POST['phonenum']] )
        elif request.method == "POST" and request.POST['mode'] =="delete" :
            form.execute('DELETE FROM cctv_manager WHERE id = %s AND id NOT IN ("admin")', [request.POST['delete_id']] )
#    if request.method == "POST":
#        form = manager_manage_form(request.POST)
#        if form.is_valid():
#            post = form.save()
#    else:
#        form = manager_manage_form()
    return render(request, 'cctv/manager_manage.html', {'manager_list' : manager_list, 'form': form})


#def insert_sql(self):
#    with connection.cursor() as cursor:
#        cursor.execute("INSERT INTO cctv_manager ('id', 'pw', 'pos', 'phonenum') VALUES(%s, %s, %s, %s)", [self.id], [self.pw], [self.pos], [self.phonenum])
#        row = cursor.fetchone()
#    return row

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def post_new(request):
    form = manager_manage_form()
    return render(request, 'cctv/post_edit.html', {'form': form})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
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
def cctv_manage(request):
    cctv_list = CCTV.objects.raw('SELECT id, model_name, install_date, manager_id FROM cctv_cctv')
    if request.method == "POST":
        model_name = request.POST['model_name'] # 여기부터
        if model_name == "":                    # model_name에 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            model_name = "%"                    # 여기까지
        manager_id = request.POST['manager_id'] # 여기부터
        if manager_id == "":                    # manager_id에 공백이 입력된 경우 전체 값을 검색하기 위한 처리과정
            manager_id = "%"                    # 여기까지
        cctv_list = CCTV.objects.raw('SELECT id, model_name, install_date, manager_id FROM cctv_cctv WHERE model_name like %s AND manager_id like %s', [model_name, manager_id])
    with connection.cursor() as form:
        form = connection.cursor()
        if request.method == "POST" and request.POST['mode'] =="insert" :
            form.execute("INSERT INTO cctv_cctv ('id', 'model_name', 'manager_id', 'install_date') VALUES(%s, %s, %s, %s)", [request.POST['insert_id'], request.POST['model_name'], request.POST['manager_id'], request.POST['install_date']] )
        elif request.method == "POST" and request.POST['mode'] =="delete" :
            form.execute('DELETE FROM cctv_cctv WHERE id = %s', [request.POST['delete_id']])
    return render(request, 'cctv/cctv_manage.html', {'cctv_list' : cctv_list, 'form': form})

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def space_manage(request):
    return render(request, 'cctv/space_manage.html', {})
