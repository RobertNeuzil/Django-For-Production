from django.shortcuts import render

posts = [

{
	"author": "Robert N.",
	"title": "Hello",
	"date": "09/24/2018"

},

{
	
	"author": "Jay Shoe",
	"title": "I invented shoes",
	"date": "04/11/2008"


},

{
	
	"author": "Dr. X",
	"title": "Jet Fuel Doesn't Melt Steel Beams",
	"date": "09/12/2002"


},


]


def index(request):
	context = {
	'posts' : posts

	}
	return render(request, 'home/index.html', context)

def about(request):
	return render(request, 'home/about.html')

