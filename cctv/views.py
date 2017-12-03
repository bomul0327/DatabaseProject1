from django.shortcuts import render
from .models import Manager, Shoot_space, CCTV, Shoot, Files, Neighborhood, Sequence, Statistics, Record #DB Table과 HTML을 연결해주는 역할
#테이블 이름은 cctv_'객체명' , eg: cctv_manager, cctv_shoot_space ...
from django.db import connection #SQL로 insert into, delete, update를 하기위하여 필요.
from .forms import manager_manage_form

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def login(request):
    return render(request, 'cctv/login.html', {})

def shoot_space_manage(request):
    return render(request, 'cctv/shoot_space_manage.html', {})

def file_manage(request):
    return render(request, 'cctv/file_manage.html', {})

def log_read(request):
    return render(request, 'cctv/log_read.html', {})

def my_page(request):
    return render(request, 'cctv/my_page.html', {})

def manager_manage(request):
    manager_list = Manager.objects.raw('SELECT id, pos, phonenum from cctv_manager')
    with connection.cursor() as form:
        form = connection.cursor()
        if request.method == "POST":
            form.execute("INSERT INTO cctv_manager ('id', 'pw', 'pos', 'phonenum') VALUES(%s, %s, %s, %s)", [request.POST['id'], request.POST['pw'], request.POST['pos'], request.POST['phonenum']] )
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


def post_new(request):
    form = manager_manage_form()
    return render(request, 'cctv/post_edit.html', {'form': form})

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

def cctv_manage(request):
    return render(request, 'cctv/cctv_manage.html', {})

def space_manage(request):
    return render(request, 'cctv/space_manage.html', {})
