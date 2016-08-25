from django.shortcuts import render, get_object_or_404, render_to_response

from django.views.decorators.csrf import csrf_exempt
from models import Matrix 
from forms import MatrixForm

from django.template import RequestContext
import matplotlib.pyplot as plt
import mpld3

# Create your views here.

def cover(request):
	return render_to_response('cover.html',
                          locals(),
                          context_instance=RequestContext(request))

def home(request):
	title = "Matplotlib to Webstie"

	# Form get info
	matrixform = MatrixForm()
	if request.GET.get('filesys') or request.GET.get('matrix'):
		matrixform = MatrixForm(request.GET)
		if matrixform.is_valid():
			FILESYS = matrixform.cleaned_data['filesys']
			MX = matrixform.cleaned_data['matrix']
		else:
			FILESYS = ['filesys1']
			MX = 'mx1'
	else:
		FILESYS = ['filesys1']
		MX = 'mx1'

	# queryset
	plot_list = []
	# The form of the data
	fig_sign = {
		'filesys1': 'g^',
		'filesys2': 'ro',
		'filesys3': 'bs'
	}

	max_y = 0

	for system in FILESYS:
		data_list = []
		queryset = Matrix.objects.filter(filesys = system)
		for obj in queryset:
			data_list.append(getattr(obj, MX))
		max_y = max(max_y, max(data_list))
		plot_list.extend([range(1, 5), data_list, fig_sign[system]])

	# matpotlib & mpld3
	#xlabels = ['bench1','bench2', 'bench3', 'bench4']
	fg = plt.figure(1) # create a object, its number is 1  
	plt.clf() # clear the figure
	plt.setp(plt.plot(*plot_list), ms=12, alpha=0.6) # set up 
	plt.axis([0,5,0,max_y * 1.2])# range for x-y
	plt.gca().yaxis.grid(True, alpha=0.2) # draw gridding for current y-axes 
	fig = mpld3.fig_to_html(fg, d3_url=None, mpld3_url=None, no_extras=False, template_type='general', figid=None, use_http=False)


	context = {
		"title": title,
		"fig": fig,
		"matrixform": matrixform,
	}


	return render_to_response('home.html',
                          locals(),
                          context_instance=RequestContext(request))


def about(request):
	return render_to_response('about.html',
                          locals(),
                          context_instance=RequestContext(request))

@csrf_exempt  
def contact(request):
	return render_to_response('contact.html',
                          locals(),
                          context_instance=RequestContext(request))

def column(request):
	return render_to_response('column.html',
                          locals(),
                          context_instance=RequestContext(request))

def polar(request):
	return render_to_response('polar.html',
                          locals(),
                          context_instance=RequestContext(request))

def log(request):
	return render_to_response('log.html',
                          locals(),
                          context_instance=RequestContext(request))
def scatter(request):
	return render_to_response('scatter.html',
                          locals(),
                          context_instance=RequestContext(request))
