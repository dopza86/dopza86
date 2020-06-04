from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from fcusers.models import Fcusers
from tag.models import Tag
from .models import Board
from .forms import BoardForm

# Create your views here.
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404("게시글을 찾을수 없습니다")
        # return redirect("/board/list/")
    # 장고는 기본적으로 pk (Primary Key)를 생성해주는데,
    # id 값이라고 생각하면 됨! 데이터가 추가될 때마다 자동으로 증가하는 숫자 (ex. 1, 2, 3 ... )
    return render(request, "board_detail.html", {"board": board})


def board_write(request):
    if not request.session.get("user"):
        return redirect("/fcusers/login/")
    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            user_id = request.session.get("user")
            fcusers = Fcusers.objects.get(pk=user_id)

            tags = form.cleaned_data["tags"].split(",")

            board = Board()
            board.title = form.cleaned_data["title"]  # 모델에서의 타이틀에 폼에서 가져온 타이틀을 대입
            board.contents = form.cleaned_data["contents"]
            # https://stackoverflow.com/questions/5083493/is-valid-vs-clean-django-forms 참조
            # is_valid 실행시 자동으로 clean()이 실행되고 self.cleand_data가 생성됨
            board.writer = fcusers
            board.save()

            for tag in tags:
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(
                    name=tag
                )  # created값을 사용하지 않기때문에 _로 표시한다
                # get_or_create-> 객체가 존재할 경우 객체를 얻고 , 아닐경우 생성한다
                # get_or_create(조건1,기본값) 조건1이 일치하면 가져오고 없으면 생성
                # 이 메서드는 (object, created) 라는 튜플 형식으로 반환을 한다.
                # 첫번째 인자(object)는 우리가 꺼내려고 하는 모델의 인스턴스이고,
                # 두번째 인자(created)는 boolean flag이다
                board.tags.add(_tag)

                # board 가 생성되고  id 가 생성이되야 tag 가 추가 가능, 상당히 당연한 소리임
                # 즉 글생성이 완료되야 태그작성이 가능하다

            return redirect(
                "/board/list/"
            )  # redirect("board/list/") 로 하면 쓰여있는 주소뒤에 또 주소를 적음
    else:
        form = BoardForm()

    return render(request, "board_write.html", {"form": form})


def board_list(request):
    all_boards = Board.objects.all().order_by("-id")  # 모든 게시글을 가져올건데 시간역순 정렬
    page = int(request.GET.get("p", 1))  # p라는 값으로 받고 없다면 1을 받음,기본값이 1
    # request.GET은 GET으로 받는 인자들을 다 포함하는 딕셔너리 객체이다.
    # get() 메서드는 키값이 딕셔너리 안에 있으면 밸류값을 리턴해준다. 키값이 존재하지 않으면 디폴트값 None을 리턴한다.
    # request.GET.get()은 위 두 개념을 합친 것으로 GET요청이 접근할 수 있는 키와 밸류값을 이용한다. 이것은 장고 뷰스에서 대부분 쓰여진다.
    paginator = Paginator(all_boards, 2)
    boards = paginator.get_page(page)
    return render(
        request, "board_list.html", {"boards": boards}
    )  # {'boards':boards} 템플릿에 전달
