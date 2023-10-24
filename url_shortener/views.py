from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from .models import URLShortener
from .utils import generate_unique_short_code


def test_view(request):
  return render(request,'Url/demo.html')
def shorten_url(request):
  shortened_url=None
  url_entry=None
  context = {
    'shortened_url':shortened_url,
    'url_entry':url_entry
  }
  if request.method=='POST':
    long_url=request.POST.get("long_url")
    short_code=generate_unique_short_code()
    url_entry=URLShortener(long_url=long_url,short_code=short_code)
    url_entry.save()
    shortened_url=request.scheme+'://my_shorturl/'+short_code
    context['shortened_url']=shortened_url 
    context['url_entry']=url_entry
    messages.success(request,"Successfully shortened")
  return render(request, 'Url/shorten_url.html',context)

def redirect_to_original(request, short_code):
  try:
    url_entry = URLShortener.objects.get(short_code=short_code)
    url_entry.click_count += 1 
    url_entry.save() 
    return redirect(url_entry.long_url)
  except URLShortener.DoesNotExist:
      return HttpResponse("Short URL not found")
def display_shortened_urls(request):
  shortened_urls = URLShortener.objects.all()
  return render(request, 'Url/shortened_urls.html', {'shortened_urls': shortened_urls})

def update_click_count(request, short_code):
    url_entry = URLShortener.objects.get(short_code=short_code)
    url_entry.click_count += 1  # Increment the click count
    url_entry.save()  # Save the updated click count
