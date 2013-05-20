from django.shortcuts import render_to_response
from django.template import RequestContext
from pages.models import HomePage, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from sorl.thumbnail import get_thumbnail



def MainHomePage(request):
	homepage	= HomePage.objects.all()
	category   = Category.objects.all()
	paginator = Paginator(homepage, 2)
    	page = request.GET.get('page','1')
    	try:
        	homepage = paginator.page(page)
    	except PageNotAnInteger:
        	homepage = paginator.page(1)
    	except EmptyPage:
        	homepage = paginator.page(paginator.num_pages)
    	context		= {'homepage':homepage,'category': category}
	return render_to_response('index.html',context, context_instance=RequestContext(request))
