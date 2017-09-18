from django.shortcuts import render




def post_list(request):

    #이것의 매핑은 blog/templates/blog/post_list.html
    return render(request,'blog/post_list.html')