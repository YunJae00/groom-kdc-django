import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # 문자열 date published 는 admin 페이지에서 보여줄

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    # 이거 admin 페이지에서 볼 수 있음 true false 가 아니라 o x 로 나오게 변경
    was_published_recently.boolean = True
    # 이 칼럼으로 정렬할 때 pub_date 를 기준으로 정렬해라 라고 명시해줌
    was_published_recently.admin_order_field = 'pub_date'
    # 의미를 조금 짧게 설명해줌
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 알아서 question의 pk를 땡겨와서 연결해줌
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text