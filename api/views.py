# from django.http import  JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint':'/notes/',
            'methods':'GET',
            'body': None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint':'/notes/id',
            'methods':'GET',
            'body': None,
            'description':'Returns an single note'
        },
        {
            'Endpoint':'/notes/create/',
            'methods':'POST',
            'body': {'body':""},
            'description':'creates a new notes'
        },
        {
            'Endpoint':'/notes/id/update/',
            'methods':'PUT',
            'body': {'body':""},
            'description':'update a the earlier notes'
        },
        {
            'Endpoint':'/notes/id/delete/',
            'methods':' DELETE',
            'body': None,
            'description':'deletes the earlier notes'
        }
    ]
    return Response(routes)




@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request,id):
    notes = Note.objects.get(id=id)
    serializer=NoteSerializer(notes,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    note=Note.objects.create(
        body=data['body']
    )
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request,id):
    data = request.data
    note=Note.objects.get(id=id)
    serializer=NoteSerializer(note,data=request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request,id):
    data=request.data
    note=Note.objects.get(id=id)
    note.delete()
    return Response('note deleted')


