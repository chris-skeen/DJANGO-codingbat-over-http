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

def string_splosion_view(request: HttpRequest, word: str) -> HttpResponse:
  if word == "":
    return HttpResponse("Not a valid word")
  else:
    sploded_word = ""
    for i in range(len(word)):
      part_needed = word[:i + 1]
      sploded_word += part_needed
    return HttpResponse(sploded_word)
  
def cat_dog_view(request: HttpRequest, string: str) -> HttpResponse:
  no_cat_string = string.replace("cat", "")
  no_dog_string = string.replace("dog", "")
  if len(no_cat_string) == len(no_dog_string):
    return HttpResponse(True)
  else:
    return HttpResponse(False)
  
def lone_sum_view(request: HttpRequest, a: int, b: int, c:int) -> HttpResponse:
  sum = 0
  if a != b and a != c:
    sum += a
  if b != a and b != c:
    sum += b
  if c != a and c!= b:
    sum += c
  return HttpResponse(sum)