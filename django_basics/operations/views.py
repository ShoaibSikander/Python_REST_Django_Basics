from django.shortcuts import render

# Create your views here.

def person_info(request):
    print(request)
    print(request.method)
    #if request.method == 'POST':
    #	print('Post Method')
    #else:
	#	print(request.method)
    #	print('Get Method')
    return render(request, 'person_info.html')