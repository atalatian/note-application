from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Note_Form_Serializer
from .serializers import NotesSerializer
from .models import Notes_Form
from .models import Notes_Record
from rest_framework import viewsets
from rest_framework import mixins
from django.views.generic.edit import DeleteView


# Create your views here.

class Add_Notes(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    new_form = Notes_Form()

    def get(self, request, *args, **kwargs):
        return Response(data={"form": self.new_form}, template_name="Note_App/form.html")

    def post(self, request, *args, **kwargs):
        new_new_form = Notes_Form(request.POST)
        if new_new_form.is_valid():
            serializer = NotesSerializer(data=new_new_form.cleaned_data)
            if serializer.is_valid():
                serializer.save()
        return HttpResponseRedirect(reverse("index"))


class Update_Notes(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        queryset = Notes_Record.objects.filter(pk=pk)
        dic = {
            "title": queryset[0].title,
            "note": queryset[0].note,
        }
        new_form = Notes_Form(dic)
        return Response(data={"form": new_form, "pk": pk},
                        template_name="Note_App/Update_Form.html")

    def post(self, request, *args, **kwargs):
        new_form = Notes_Form(request.POST)
        if new_form.is_valid():
            pk = self.kwargs["pk"]
            queryset = Notes_Record.objects.filter(pk=pk)
            instance = get_object_or_404(queryset)
            dic = {
                "title": new_form.cleaned_data["title"],
                "note": new_form.cleaned_data["note"],
            }
            serializer = NotesSerializer(instance, data=dic)
            if serializer.is_valid():
                serializer.save()
            return HttpResponseRedirect(reverse("index"))


class Delete_Record(APIView, DeleteView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.queryset = Notes_Record.objects.filter(pk=self.kwargs["pk"])
        self.success_url = reverse_lazy("index")
        return super().delete(request, *args, **kwargs)


class Notes(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(data={"notes": Notes_Record.objects.all()}, template_name="Note_App/index.html")


def ok(request):
    return HttpResponse("OK")
