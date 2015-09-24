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
    """
    Solo permite que un usuario pueda actualizar y eliminar su propia información
    a excepción de un admin que si puede alterar la información de cualquier usuario
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_staff:
            return True

        return obj == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_staff) or request.method in permissions.SAFE_METHODS
