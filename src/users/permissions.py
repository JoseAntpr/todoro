from rest_framework.permissions import BasePermission




class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Define si un usuario puede usar o no el endpoint que quiere utilizar
        :param request:
        :param view:
        :return:
        """
        #Cualquiera autenticado puede acceder al detalle para ver, actualizar o borrar
        if request.user.is_authenticated() and view.action in ("retrieve", "update", "destroy"):
            return True

        #Si es superusuario y quiere acceder al listado
        if request.user.is_superuser and view.action == "list":
            return True
        #Cualquiera puede crear un usuario (POST)
        if view.action == "create":
            return True


        #Un uusario no authenticado no puede ejecutar get, put o delete

        return False

        #Si el usuario quiere acceder al listado de usuaarios debe ser administrador

    def has_object_permission(self, request, view, obj):
       """
       Define si el usuario puede realizar la acción sobre el objeto que quiere realizarla
       :param request: HttpRequest
       :param view: UsersApi/UserDetailApi
       :param obj: user
       :return: True si puede, False si no puede
       """
       return request.user.is_superuser or request.user == obj
