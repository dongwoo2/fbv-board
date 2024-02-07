from django.db import models

# Create your models here.
from django.utils import timezone

class Board(models.Model):
    title = models.CharField(max_length = 50)
    writer = models.CharField(max_length = 30)
    content = models.TextField()
    regdate = models.DateTimeField(auto_now=timezone.now)
    readcount = models.IntegerField(defalut=0)
    
    def __str__(self):
        return '%s. %s(%d)' % (self.title, self.writer, self.readcount)
    
    def incrementReadCount(self): # 도메인 안에 있는건 도메인에서 처리하도록 하자, 도메인 안에 조회 수 증가시키는 함수를 넣음
        self.readcount += 1
        self.save()