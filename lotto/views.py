from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
# Create your views here.
def index(request): # request는 사용자가 요청한 정보를 담고 있는 객체


    #<input name="name" type="text"></input>

    # user_input_name = request.POST['name']
    # user_input_text = request.GET['text']

    # new_row = GuessNumbers(name=user_input_name, text=user_input_text)

    #print(new_row) -> "pk 1 : win the prize!' - updated on 2025.09.12"

#     print(new_row.num_lotto)
#     print(new_row.name)

#     new_row.name = new_row.name.upper()
#    # new_row.lottos = [np.randint(1,50)for i in range(6)]
#     #new_row.save()

#     new_row.generate()


    # request.POST -> dict
    # dict 의 키값은 input 태그의 name 속성값
    # dict 의 value는 input 태그의 value 속성값 (user의 입력값)


    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos':lottos}) # lotto > templates > lotto > default.html 파일을 렌더링하여 사용자에게 보여줌


def post(request):


    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():

            lotto = form.save(commit=False)
            lotto.generate()

            return redirect('index')

            # lotto.text = lotto.text.upper()
            # lotto.lottos = '[1,2,3,4,5,6]'
            # lotto.save()
            # print("\n\n\n")
            # print(type(form))

            # print(form)
            # print("\n\n\n")
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

    # form = PostForm(request.POST)
    # form.save()  

    print("\n\n\n")
    print(type(form))

    print(form)
    print("\n\n\n")


    form = PostForm()
    return render(request, 'lotto/form.html', {'form':form})


def hello(request):
    # data = GuessNumbers.objects.all()
    # data = GuessNumbers.objects.get(id=1)
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>") # 사용자에게 보여줄 응답을 반환


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(id=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto}) # lotto > templates > lotto > detail.html 파일을 렌더링하여 사용자에게 보여줌