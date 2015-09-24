from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from matsonamis.models import OperatingSystemVersion, OperatingSystem, OpSysPurpose, Ami

# Create your views here.
# A basic view that just displays some text
def splash(request):
    return HttpResponse("Matson AMI View")

# some simple display views
#def detail(request, passed_id):
#    return HttpResponse("You're viewing ami %s " % passed_id)

#def amiresults(request, ami_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % ami_id)

# Example of querying the database for infomration
#def amidata(request):
#    latest_ami_list = Ami.objects.order_by('-ami_creation_date')[:3]
#    output = ', '.join([p.ami_name for p in latest_ami_list])
#    return HttpResponse(output)

# Example of querying the database for information and using
# a template to render that data.
def amidata(request):
    latest_ami_list = Ami.objects.order_by('-ami_creation_date')[:3]
    template = loader.get_template('matsonamis/index.html')

    # using the shortcut
    context = {'latest_ami_list': latest_ami_list}

    # Long way
    #context = RequestContext(request, {
    #    'latest_ami_list': latest_ami_list,
    #    })
    #return HttpResponse(template.render(context))
    return render(request, 'matsonamis/index.html', context)

def buildami(request):
    latest_ami_list = Ami.objects.order_by('-ami_creation_date')[:5]
    template = loader.get_template('matsonamis/buildami.html')
    context = {'latest_ami_list': latest_ami_list}
    return render(request, 'matsonamis/buildami.html', context)

def testview(request):
    template = loader.get_template('matsonamis/testview.html')
    context = {}
    return render(request, 'matsonamis/testview.html', context)
