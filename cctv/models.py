from django.db import models

# Create your models here.
class Manager(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    pw = models.CharField(max_length=20, null=False)
    pos = models.CharField(max_length=20)
    phonenum = models.CharField(max_length=13)
    def __str__(self):
        return self.id

class Shoot_space(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    dong = models.CharField(max_length=20)
    building_name = models.CharField(max_length=20)
    flr = models.CharField(max_length=5)
    location = models.CharField(max_length=20)
    def __str__(self):
        return self.id

class CCTV(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    model_name = models.CharField(max_length=20, null=False)
    install_date = models.DateTimeField('date installed')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=False)
    shoots = models.ManyToManyField(Shoot_space, through='Shoot', through_fields=('CCTV_id', 'Shoot_space_id'))
    def __str__(self):
        return self.id

class Shoot (models.Model):
    CCTV_id = models.ForeignKey(CCTV, on_delete=models.CASCADE, null=False)
    Shoot_space_id = models.ForeignKey(Shoot_space, on_delete=models.CASCADE, null=False)

class Files(models.Model):
    file_name =  models.CharField(max_length=20, primary_key=True, null=False)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    CCTV_id = models.ForeignKey(CCTV, on_delete=models.CASCADE, null=False)
    Shoot_space_id = models.ForeignKey(Shoot_space, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.file_name

class Neighborhood(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    route = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    space_a = models.ForeignKey(Shoot_space, related_name='A', on_delete=models.CASCADE, null=False)
    space_b = models.ForeignKey(Shoot_space, related_name='B', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.id

class Sequence(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    connects = models.ManyToManyField(Neighborhood)
    def __str__(self):
        return self.id

class Statistics(models.Model):
    file_name =  models.OneToOneField(Files)
    records = models.IntegerField()
    time_length = models.IntegerField()
    obj_num = models.IntegerField()
    avg_speed = models.DecimalField(max_digits=20, decimal_places=2)
    avg_size = models.DecimalField(max_digits=20, decimal_places=2)
    def __str__(self):
        return self.file_name

class Record(models.Model):
    time_stamp = models.DateTimeField(null=False)
    obj_id = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=20)
    obj_size = models.IntegerField
    obj_speed = models.IntegerField
    obj_color = models.CharField(max_length=20)
    file_name = models.ForeignKey(Files, null=False, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.file_name + ":" + self.time_stamp
