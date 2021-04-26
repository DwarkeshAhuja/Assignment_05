from django.shortcuts import render

# Create your views here.
def home(request):
    """
    This method/will return a view of the home page i.e. base.html
    :param request: HTTP Request to render the home page
    :return: HTTP Response to render the home page
    """
    return render(request, 'base.html')

def heatmap(request):
    """
    This method/will return a view of the heatmap page
    :param request: HTTP Request to render the heatmap
    :return: HTTP Response to render the heatmap
    """
    return render(request,'heatmap.html')

def linegraph(request):
    """
       This method/will return a view of the linegraph page
       :param request: HTTP Request to render the linegraphs
       :return: HTTP Response to render the linegraphs
       """
    return  render(request,'linegraph.html')

def code(request):
    """
       This method/will return a view of the Python Code executed in Jupyter Notebook
       :param request: HTTP Request to render the code page
       :return: HTTP Response to render the code page
       """
    return render(request,'code.html')