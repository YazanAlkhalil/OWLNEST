from rest_framework import permissions

#models 
from system.models.Company import Company
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        return True
    def has_object_permission(self, request, view, obj):
        # Check if the user is the admin
        return request.user.is_admin
    


class IsCompanyOwner(permissions.BasePermission):
      def has_permission(self, request, view): 
      
          if Company.objects.get(id = view.kwargs['company_id']).owner.user == request.user :
          
              return True 
          return False   
      


class IsAdminInCompany(permissions.BasePermission):
      def has_permission(self, request, view): 
          if  Company.objects.get(id = view.kwargs["company_id"]).admins.filter(admin_contract__admin__user = request.user,admin_contract__employed =True).exists():
              return True
          
          return False
      

class IsAdminInCompanyOrOwner(permissions.BasePermission):
      def has_permission(self, request, view): 
          if( Company.objects.get(id = view.kwargs["company_id"]).admins.filter(admin_contract__admin__user = request.user,admin_contract__employed =True).exists()) or (Company.objects.get(id = view.kwargs['company_id']).owner.user == request.user):
               
              return True 
          
          return False