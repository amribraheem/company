# from .models import Member
# from .utils import get_tenant_from_request
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import MemberSerializer
# from rest_framework import viewsets

# @api_view(['GET'])
# def our_teams(request):
#     tenant = get_tenant_from_request(request)
#     members = Member.objects.filter(tenant=tenant)
#     print(members)
#     serializer = MemberSerializer(members, many=True)
#     # print(serializer.data)

#     return Response(serializer.data)


# class MemberViewSet(viewsets.ModelViewSet):
#     serializer_class = MemberSerializer

#     def get_queryset(self):
#         tenant = get_tenant_from_request(self.request)
#         return super().get_queryset().filter(tenant=tenant)
