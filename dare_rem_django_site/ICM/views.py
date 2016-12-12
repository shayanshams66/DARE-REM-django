from django.shortcuts import render,render_to_response, RequestContext
# Create your views here.
def ICM(request):
    return render_to_response("ICM.html",
                               locals(),
                               context_instance=RequestContext(request))
