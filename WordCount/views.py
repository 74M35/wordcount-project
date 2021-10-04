from django.http import HttpResponse
from django.shortcuts import render
import operator, re

def home(request):
    return render(request, "home.html")

def count(request):
    fullText = request.GET["fullText"]
    wordList = fullText.split()
    wordDict = {}
    for word in wordList:
        word = re.sub(r'[^\w\s]', "", word).lower()
        if word in wordDict:
            #increase
            wordDict[word] += 1
        else:
            #add to dict
            wordDict[word] = 1
    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {"fullText": fullText, "count": len(wordList), "sortedWords": sortedWords})

def about(request):
    return render (request, "about.html")