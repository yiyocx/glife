# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado para solo permitir que los propietarios
    de un Documento puedan editarlo
    """

    def has_object_permission(self, request, view, obj):
        # Permisos de lectura son permitidos para cualquier peticion,
        # asi que siempre vamos a permitir peticiones GET, HEAD o OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permisos de escritura solo son permitidos al propietario del Documento
        return obj.owner == request.user


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Permite que cualquier persona pueda registrarse creando una cuenta
        pero restringe la visualización de usuarios existentes a usuarios autenticados
        """
        return request.method == 'POST' or request.user and request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


