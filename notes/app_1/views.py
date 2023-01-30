from django.shortcuts import render,HttpResponse
from . models import Notes
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import NoteSerializer

class NoteList(ListView):
    model = Notes
    template_name="home.html"
    context_object_name="body"





@api_view(["GET"])
def getNotes(request):
    notes = Notes.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getNote(request,pk):
    notes = Notes.objects.get(id = pk)
    serializer = NoteSerializer(notes)
    return Response(serializer.data)




@api_view(['PUT'])
def updateNote(request, pk):
    data=request.data
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['Delete'])
def deleteNote(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return Response("Note is deleted!")

@api_view(['POST'])
def createNote(request):
    data =request.data
    note=Notes.objects.create(
        Body=data['Body']
    )

    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
