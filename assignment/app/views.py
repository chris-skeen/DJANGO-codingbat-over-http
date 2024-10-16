from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def near_hundred_view(request: HttpResponse, n: int) -> HttpResponse:
  num = abs(n)
  if num >= 90 and num <= 110:
    value = True
  elif (num >= 190) and (num <= 210):
    value = True
  else:
    value = False
  return HttpResponse(value)

def string_splosion_view(request: HttpRequest, word: str) -> HttpRequest:
  if word == "":
    return HttpResponse("Not a valid word")
  else:
    sploded_word = ""
    for i in range(len(word)):
      part_needed = word[:i + 1]
      sploded_word += part_needed
      print(part_needed)
    return HttpResponse(sploded_word)
  
def cat_dog(request: HttpRequest) -> HttpRequest:
  
  return HttpResponse()