from django.shortcuts import render,render_to_response, RequestContext
from django_tables2   import RequestConfig
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models  import Job
from .tables  import JobTable
from .forms import JobForm
from .forms2 import IbiomesForm
from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf
#from django.conrib.auth.decorators import login_required
from .tables2 import IbiomesTable
import action as action
import urllib
from django.db.models.loading import get_models
from django.contrib.auth.decorators import login_required
from .forms3  import FileTransferForm
import os
#from .models import JobManager,my_costum_sql
# Create your views here.
@login_required
def Jobs(request):
	f=open('shayan.txt','w')
	#for p in JobManager('Select * FROM job_management_job'):
        #for p in Job.objects:
               #f.write(p)
        lol=str(Job.objects)
        f.write(lol)
        f.close()
	table = JobTable(Job.objects.all())
        #table = JobTable(Job.objects.filter(userid=request.user.user_id))
	RequestConfig(request).configure(table)
        #if(request.GET.get('delAction')):
            #os.system('echo "y" | starcluster terminate restmd_cluster')
	return render(request, 'Jobs.html', {'table': table})
def forms(request):
	#if request.method == 'POST':
		#form = UserProfileForm(request.POST, instance=request.user.profile)
		#if form.is_valid():
			#form.save()
	#else:
	#user = request.user
	#profile = user.profile
	#form = UserProfileForm (instance = profile)

	form= JobForm(request.POST or None)
	if form.is_valid():
		#save_it= form.save(commit=False)
		#save_it.save()
	#args = {}
	#args.update(csrf(request))

	#args["forms"] = forms
		values={}
		us = request.user
		values['user'] = us
		data = urllib.urlencode(values) 

		url =  "http://dare.cct.lsu.edu:8080/gateways/ngs/ngs/rem_form"
		full_url = url + '?' + data 
		return HttpResponseRedirect(full_url)
	else:
		return render_to_response("forms.html",
                              	   	   locals(),
                              		   context_instance=RequestContext(request))

	#return render_to_response("forms.html",
                              #locals(),
                              #context_instance=RequestContext(request))
def forms2(request):
	form= IbiomesForm(request.POST or None)
	if form.is_valid():
		save_it= form.save(commit=False)
		save_it.save()
		return render_to_response("forms2.html",
                              	   	   locals(),
                              		   context_instance=RequestContext(request))
#@login_required
def Ibiomes(request):
	#table = JobTable(Job.objects.all())
	table = IbiomesTable(Job.objects.filter())
	RequestConfig(request).configure(table)
	return render(request, 'dataAnalysis.html', {'table': table})
def Files(request):
   form = FileTransferForm(request.POST or None)
   if form.is_valid():
       selected=form.cleaned_data.get('Files')
       #save_it= form.save(commit=False)
       #save_it.save()
   else:
      form = FileTransferForm(request.POST or None)
   return render_to_response("forms3.html",
                                  locals(),
                                  context_instance=RequestContext(request))
def update(request):
    result=action.main()
    return HttpRequest(result)
    
#def action(Deleteview):
    #model=Job
    #template_name='Jobs.html'
    #success_url=reverse_lazy('Jobs')
