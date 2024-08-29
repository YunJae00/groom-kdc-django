from django.utils import timezone
import random

from django.db import models

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=200) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1,2,3,4,5,6]')
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    updated_date = models.DateTimeField()

    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1,46)) # 1~45 의 숫자 리스트
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)