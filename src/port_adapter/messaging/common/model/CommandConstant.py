"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from enum import Enum


class CommandConstant(Enum):
    CREATE_USER = 'create_user'
    DELETE_USER = 'delete_user'
    UPDATE_USER = 'update_user'
    CREATE_ROLE = 'create_role'
    DELETE_ROLE = 'delete_role'
    UPDATE_ROLE = 'update_role'
    CREATE_OU = 'create_ou'
    DELETE_OU = 'delete_ou'
    UPDATE_OU = 'update_ou'
    CREATE_PERMISSION = 'create_permission'
    DELETE_PERMISSION = 'delete_permission'
    UPDATE_PERMISSION = 'update_permission'
    CREATE_PROJECT = 'create_project'
    DELETE_PROJECT = 'delete_project'
    UPDATE_PROJECT = 'update_project'
    CREATE_REALM = 'create_realm'
    DELETE_REALM = 'delete_realm'
    UPDATE_REALM = 'update_realm'
    CREATE_RESOURCE_TYPE = 'create_resource_type'
    DELETE_RESOURCE_TYPE = 'delete_resource_type'
    UPDATE_RESOURCE_TYPE = 'update_resource_type'
    CREATE_USER_GROUP = 'create_user_group'
    DELETE_USER_GROUP = 'delete_user_group'
    UPDATE_USER_GROUP = 'update_user_group'