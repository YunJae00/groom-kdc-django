from django.contrib import admin

from .models import Question, Choice


# question 만들 때 choice 도 같이 보이게
# stacked 는 위아래로 tabular 는 table 형식으로 (가로로)
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 2 # default 로 보여줄 Choice 입력 slot 의 수

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2 # default 로 보여줄 Choice 입력 slot 의 수


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['question_text', 'pub_date']
    fieldsets = [
        # group (Question title) 에 들어갈 fields 들 (list)
        ("Question title", {'fields': ['question_text']}),
        # collapse 는 굳이 안보여줘도 되는거는 안보이게 (classes는 스타일 느낌임 디자인)
        ("Date information", {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # choice 추가
    inlines = [ChoiceInline]

    # question 리스트 보여줄 때 어떤거 보여주는지 표시
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # filter 를 만들어주고 어떤 기준으로 만들어주냐 (어떤걸 기준으로 잡냐를 list 안에 넣어줌)
    list_filter = ['pub_date']

    # search 가능하게
    search_fields = ['question_text']





# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)