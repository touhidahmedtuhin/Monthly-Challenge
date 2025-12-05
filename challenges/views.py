from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound ,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges_dict = {
    "january": "Walk 20 minutes every day!",
    "february": "Read 10 pages of a book daily!",
    "march": "Practice coding for 30 minutes!",
    "april": "Meditate for 10 minutes each morning!",
    "may": "Drink 2 liters of water daily!",
    "june": "Write in a journal every night!",
    "july": "Learn a new word each day!",
    "august": "Do 15 pushups every morning!",
    "september": "Spend 30 minutes learning Django!",
    "october": "Try a new healthy recipe weekly!",
    "november": "Practice gratitude daily!",
    "december": None
}

def index(request):
  months = list(monthly_challenges_dict.keys())
  return render (request, 'challenges/index.html',{
    'months':months,
  })



def monthly_challenges_by_number(request,month):
  months = list(monthly_challenges_dict.keys())
  if month < 1 or month > len(months):
    return HttpResponseNotFound('Invalid Month')
  month_name = months[month - 1]
  reverse_url = reverse('month-challenge', args=[month_name])
  return HttpResponseRedirect (reverse_url)



def monthly_challenges(request,month):
  try:
    challenge_text = monthly_challenges_dict[month.lower()]
    return render (request, 'challenges/challenges.html',{
      'text':challenge_text,
      'month_name':month,
    })
  except KeyError:
    return HttpResponseNotFound("<h1>This is not a valid month</h1>")

