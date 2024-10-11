from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer , Alladmins , UploadAssignmentSerializer , UploadAssignmentAnotherSerializer

from rest_framework.decorators import APIView
from .models import User , UploadAssigment


@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'message': "Registration successful", 'data': serializer.data}, status=status.HTTP_201_CREATED)

    return Response({'message': 'Registration failed', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class LoginViewSet(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        login_type = request.data.get('login_type')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'msg': 'Invalid User'}, status=400)

            if user.check_password(password):
                if user.user_type == login_type:
                    return Response({'msg': 'Login successfully'}, status=200)
                else:
                    return Response({'msg': 'Invalid user type'}, status=400)
            else:
                return Response({'msg': 'Invalid password'}, status=400)
        else:
            return Response({'msg': 'Email and password are required'}, status=400)
        
        
@api_view(['GET'])
def GetAllAdmin(reqeust):
    try:
        user = User.objects.filter(user_type='admin')
        serializer = Alladmins(user , many=True)
        return Response({'data':serializer.data},status=200)
    except Exception as e:
        return Response({'msg':'No admins Found'})
        
        

    
@api_view(['POST'])
def UploadAssignment(request):
    if request.method == 'POST':
        serializer = UploadAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            
            uservalid = serializer.validated_data.get('userobj') 
            try:
                user = User.objects.get(first_name=uservalid, user_type='users')
                print(user)
            except User.DoesNotExist:
                return Response({'msg': 'Invalid User'}, status=status.HTTP_400_BAD_REQUEST)
            admin_name = serializer.validated_data.get('Tagadmin') 
            try:
                admin_user = User.objects.get(first_name=admin_name, user_type='admin')
            except User.DoesNotExist:
                return Response({'msg': 'Admin with this name is not valid'}, status=status.HTTP_400_BAD_REQUEST)
            print('here',user.user_id)
            assignment = UploadAssigment.objects.create(
                userobj=user,
                task=serializer.validated_data.get('task'),
                Tagadmin=admin_user
            )

            return Response({'msg': 'Assignment uploaded successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def GetAllAssignment(request):
    admin_first_name = request.data.get('admin_first_name')

    if not admin_first_name:
        return Response({'msg': 'Admin first name is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        admin_user = User.objects.get(first_name=admin_first_name, user_type='admin')
        assignments = UploadAssigment.objects.filter(Tagadmin=admin_user)
        serializer = UploadAssignmentAnotherSerializer(assignments, many=True)

        if not assignments.exists():
            return Response({'msg': 'No assignments found for this admin'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'assignments': serializer.data}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'msg': 'Admin not found'}, status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def assignmentaccepted(request,user_obj):
    try:
        assignment = UploadAssigment.objects.get(id=user_obj)
        return Response({'msg':'Assignment Accepted'},status=200)

    except Exception as e:
        return Response({'msg':'No assignment with this id '})


@api_view(['POST'])
def assignmentrejected(request,user_obj):
    try:
        assignment = UploadAssigment.objects.get(id=user_obj)
        return Response({'msg':'Assignment Rejected'},status=200)

    except Exception as e:
        return Response({'msg':'No assignment with this id '})