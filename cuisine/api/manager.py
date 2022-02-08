from tenants.utils import get_tenant_from_request
from django.db import models


class TenantFilterManager(models.Manager):
    def filter_by_tenant(self, request):
        tenant = get_tenant_from_request(request)
        return super().get_queryset().filter(tenant=tenant)
