from django.shortcuts import render, get_object_or_404, redirect
from .forms import BoardForm
from .models import Board
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def post(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.update_date=timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm()
        return render(request, 'post.html', {'form':form})

def show(request):
    # 모든 글들을 대상으로
    boards = Board.objects
    board_list = Board.objects.all().order_by('-id')
    paginator = Paginator(board_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'show.html', {'boards':boards, 'posts': posts})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board':board_detail})

def edit(request, pk): #Pk 받는다 원하는 폼만 뜰 수 있도록 한다. 글의 인스턴스
        board = get_object_or_404(Board, pk=pk)
        if request.method == "POST":
                form = BoardForm(request.POST, instance=board)
                if form.is_valid():
                        board = form.save(commit = False)
                        board.update_date=timezone.now()
                        board.save()
                        return redirect('show')
        else:
                form = BoardForm(instance=board)
                return render(request, 'edit.html', {'form':form})

def delete(request, pk):
        board=Board.objects.get(id=pk)
        board.delete()
        return redirect('show')