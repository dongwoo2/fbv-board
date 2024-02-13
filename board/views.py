from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'board/index.html')

from.models import Board

def list(request): #list 라는 뷰함수를 만들어서
    board_list = Board.objects.all()  # 보드모델로부터 전체목록을 가져와서
    context = { #그걸 응답에 사용할 수 있게 딕셔너리를 만들고
        'board_list':board_list,
    }
    return render( # 렌더함수로 리스트 템플릿을 응답으로 만들어주는데 context의 내용을 사용해주도록 한다
                  # context에서 전달한 내용이 board_list니까 템플릿에서 board_list로 접근할 수 있게 된다.
        request,
        'board/list.html',
        context
    )