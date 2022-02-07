from django.shortcuts import render

from .models import Tenant


def get_hostname_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(':')[0].lower()


def get_tenant_from_request(request):
    hostname = get_hostname_from_request(request)
    subdomain_prefix = hostname.split('.')[0]
    return Tenant.objects.filter(subdomain_prefix=subdomain_prefix).first()
