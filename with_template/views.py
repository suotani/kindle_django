from django.shortcuts import render

def index(request):
  return render(request, "with_template/index.html", {})

def show(request, name):
  return render(request, "with_template/show.html", {'user_name': name})

def list(request):
  numbers = [1,2,3,4,5]
  return render(request, "with_template/list.html", {'numbers': numbers})

def fizzbuzz(request, limit):
  content = {'list': range(1, limit+1) }
  return render(request, "with_template/fizzbuzz.html", content)

def form(request):
  return render(request, 'with_template/form.html', {})

def form_read(request):
  input_name = request.POST["input_name"]
  content = {'input_name': input_name }
  return render(request, 'with_template/form_read.html', content)