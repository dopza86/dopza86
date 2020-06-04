from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcusers
from .forms import LoginForm

# Create your views here.
def home(request):
    # user_id = request.session.get("user")  # 이값이 있으면 로그인한 클라이언트
    # if user_id:
    #     fcusers = Fcusers.objects.get(pk=user_id)  # Fcusers 모듈 안에서 user_id를 지정해서 가져온다
    # return HttpResponse(f"{fcusers.username}님 반갑습니다")
    return render(request, "home.html")


def logout(request):
    if request.session.get("user"):  # 세션안에 유저값이 있는지 없는지에 따라 로그인을 판단,즉 로그인된 상태
        del request.session["user"]  # 세션에서 user값 삭제를 하면 로그아웃이 된다

    return redirect("/")


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():  # is_valid -> 정상적인지 검증하는 함수 bool값을 리턴한다
            request.session["user"] = form.user_id  # forms 에서 fcusers.id 로 이미 저장됨
            return redirect("/")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


# def login(request):
#     if request.method == "GET":
#         return render(request, "login.html").
#     elif request.method == "POST":
#         username = request.POST.get("username", None)
#         password = request.POST.get("password", None)

#         res_data = {}
#         if not (username and password): .
#             res_data["error"] = "모든값을 입력하세요"
#         else:
#             fcusers = Fcusers.objects.get(
#                 username=username
#             )  # 모델에서 Fcusers 안의 객체를 가져올때 .objects.get()을 사용
#             if check_password(
#                 password, fcusers.password
#             ):  # check_password(입력받은비밀번호,모델로부터 가져온값)
#                 request.session["user"] = fcusers.id  # 세션에 아이디 저장
#                 return redirect("/")

#                 # 비밀번호 일치시 로그인 처리
#                 pass
#             else:
#                 res_data["error"] = "비밀번호를 다시 입력 해주세요"

#         return render(request, "login.html", res_data)


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get(
            "username", None
        )  # None 은 디폴트 값으로 키가 존재하지 않을떄 리턴할값이다
        password = request.POST.get("password", None)
        re_password = request.POST.get("re-password", None)
        email = request.POST.get("email", None)

        # username = request.POST["username"]
        # password = request.POST["password"]
        # re_password = request.POST["re-password"]

        # if passwod != repassword :
        #     return HttpResponse('비밀번호가 다릅니다') #다른창으로 넘어가서 비밀번호가 다릅니다 출력

        res_data = {}  # 빈 dict

        if not (username and password and re_password and email):
            res_data["error"] = "모든 항목을 작성해 주세요"  # 딕셔너리변수

        elif password != re_password:

            res_data["error"] = "비밀번호가 다릅니다!"
        else:
            fcusers = Fcusers(
                username=username, password=make_password(password), useremail=email
            )  # 클래스 변수 생성
            fcusers.save()

        return render(
            request, "register.html", res_data
        )  # register.html 데이터를 전달할때 res_data가 맵핑이된다
