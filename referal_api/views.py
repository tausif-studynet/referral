from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        Return a demo JSON response
        '''
        demo_response = {
            "todos": [
                {"id": 1, "task": "Demo Task 1", "completed": False, "user": request.user.id},
                {"id": 2, "task": "Demo Task 2", "completed": True, "user": request.user.id}
            ]
        }
        return Response(demo_response, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Return a demo JSON response for created todo
        '''
        demo_response = {
            "id": 3,
            "task": "Demo Task Created",
            "completed": False,
            "user": request.user.id
        }
        return Response(demo_response, status=status.HTTP_201_CREATED)
