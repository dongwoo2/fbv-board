from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
    return render(request, 'board/index.html')

from.models import Board

def list(request): #list 라는 뷰함수를 만들어서
    board_list = Board.objects.all().order_by('-id')  # 보드모델로부터 전체목록을 가져와서
    context = { #그걸 응답에 사용할 수 있게 딕셔너리를 만들고
        'board_list':board_list,
    }
    return render( # 렌더함수로 리스트 템플릿을 응답으로 만들어주는데 context의 내용을 사용해주도록 한다
                  # context에서 전달한 내용이 board_list니까 템플릿에서 board_list로 접근할 수 있게 된다.
        request,
        'board/list.html',
        context
    )
    
def read(request, id): # 경로변수로 id를 하나 가져옴
    board = Board.objects.get(pk=id) # board 모델에서 get으로 검색
    board.incrementReadCount()
    return render(request, 'board/read.html', {'board':board}) # 검색해서 나온 결과물로 html에 전달

def regist(request):
    if request.method == 'POST':
        title = request.POST['title']
        writer = request.POST.get('writer')
        content = request.POST['content']
        Board(title=title, writer=writer, content=content).save()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/regist.html')
        
def edit(request, id):
    board = Board.objects.get(pk=id) # 검색된 보드를 수정해줌
    if request.method == 'POST':
        board.title = request.POST['title'] # 값이 없으면 에러가 나고
        board.writer = request.POST.get('writer', 'default') # 값이 없으면 default를 쓰겠다
        board.content = request.POST['content']
        board.save() #수정하고 나서 수정된 정보를 save해야 해당 id와 동일한정보가 database에서 수정됨
        return redirect(reverse('board:read', args=(id,)))
    else:
        return render(request, 'board/edit.html', {'board:board'})
    
def remove(request, id):
    board = Board.objects.get(pk=id)
    if request.method == 'POST':
        board.delete()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/remove.html', {'board:board'})