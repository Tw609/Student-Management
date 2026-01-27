from django.shortcuts import render, redirect
from django.contrib import messages

def score_list(request):
    scores = request.session.get("scores", [])
    return render(request, "score/list.html", {"scores": scores})

def score_add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        score_value = request.POST.get("score")

        scores = request.session.get("scores", [])
        scores.append({"name": name, "score": score_value})
        request.session["scores"] = scores

        messages.success(request, "Score has been added successfully!")
        return redirect("score_list")
    return render(request, "score/add.html")

def score_edit(request, index):
    scores = request.session.get("scores", [])
    if request.method == "POST":
        name = request.POST.get("name")
        score_value = request.POST.get("score")
        if 0 <= index < len(scores):
            scores[index]["name"] = name
            scores[index]["score"] = score_value
            request.session["scores"] = scores
            messages.success(request, "Score has been edited!")
            return redirect("score_list")
    return render(request, "score/edit.html", {"score": scores[index]})

def score_delete(request, index):
    scores = request.session.get("scores", [])
    if 0 <= index < len(scores):
        scores.pop(index)
        request.session["scores"] = scores
        messages.success(request, "Score has been deleted!")
        return redirect("score_list")