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


@api_view(['GET'])
def getData(request):

    notes = [
        {
            'id': 1,
            "body": "Todays Agenda\n\n- Walk Dog\n- Feed fish\n- Play basketball\n- Eat a salad",
            "updated": "2021-07-14T13:49:02.078653Z",
            "created": "2021-07-13T21:54:16.235392Z"
        },
        {
            "id": 2,
            "body": "Bob from bar down the \n\n- Take out trash\n- Eat food",
            "updated": "2021-07-13T20:43:18.550058Z",
            "created": "2021-07-13T00:17:13.289897Z"
        },
        {
            "id": 3,
            "body": "Wash car",
            "updated": "2021-07-13T19:46:12.187306Z",
            "created": "2021-07-13T00:16:22.399841Z"
        }
    ]
    return Response(notes)


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
