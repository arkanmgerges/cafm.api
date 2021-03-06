"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from enum import Enum


# region Command constants
class CommandConstant(Enum):
    CREATE_USER = "create_user"
    DELETE_USER = "delete_user"
    UPDATE_USER = "update_user"
    CREATE_ROLE = "create_role"
    DELETE_ROLE = "delete_role"
    UPDATE_ROLE = "update_role"
    CREATE_OU = "create_ou"
    DELETE_OU = "delete_ou"
    UPDATE_OU = "update_ou"
    CREATE_PERMISSION = "create_permission"
    DELETE_PERMISSION = "delete_permission"
    UPDATE_PERMISSION = "update_permission"
    CREATE_PROJECT = "create_project"
    DELETE_PROJECT = "delete_project"
    UPDATE_PROJECT = "update_project"
    CREATE_REALM = "create_realm"
    DELETE_REALM = "delete_realm"
    UPDATE_REALM = "update_realm"
    CREATE_RESOURCE_TYPE = "create_resource_context"
    DELETE_RESOURCE_TYPE = "delete_resource_context"
    UPDATE_RESOURCE_TYPE = "update_resource_context"
    CREATE_PERMISSION_CONTEXT = "create_permission_context"
    DELETE_PERMISSION_CONTEXT = "delete_permission_context"
    UPDATE_PERMISSION_CONTEXT = "update_permission_context"
    CREATE_USER_GROUP = "create_user_group"
    DELETE_USER_GROUP = "delete_user_group"
    UPDATE_USER_GROUP = "update_user_group"
    ASSIGN_ROLE_TO_USER = "assign_role_to_user"
    REVOKE_ASSIGNMENT_ROLE_TO_USER = "revoke_assignment_role_to_user"
    ASSIGN_ROLE_TO_USER_GROUP = "assign_role_to_user_group"
    REVOKE_ASSIGNMENT_ROLE_TO_USER_GROUP = "revoke_assignment_role_to_user_group"
    ASSIGN_USER_TO_USER_GROUP = "assign_user_to_user_group"
    REVOKE_ASSIGNMENT_USER_TO_USER_GROUP = "revoke_assignment_user_to_user_group"
    ASSIGN_PERMISSION_TO_PERMISSION_CONTEXT = "assign_permission_to_permission_context"
    REVOKE_ASSIGNMENT_PERMISSION_TO_PERMISSION_CONTEXT = (
        "revoke_assignment_permission_to_permission_context"
    )
    ASSIGN_ROLE_TO_PERMISSION = "assign_role_to_permission"
    REVOKE_ASSIGNMENT_ROLE_TO_PERMISSION = "revoke_assignment_role_to_permission"
    GRANT_ACCESS_ROLE_TO_RESOURCE = "grant_access_role_to_resource"
    REVOKE_ACCESS_ROLE_TO_RESOURCE = "revoke_access_role_to_resource"
    ASSIGN_RESOURCE_TO_RESOURCE = "assign_resource_to_resource"
    REVOKE_ASSIGNMENT_RESOURCE_TO_RESOURCE = "revoke_assignment_resource_to_resource"
    SET_USER_PASSWORD = "set_user_password"
    RESET_USER_PASSWORD = "reset_user_password"
    CREATE_BUILDING = "create_building"
    DELETE_BUILDING = "delete_building"
    UPDATE_BUILDING = "update_building"
    CREATE_BUILDING_LEVEL = "create_building_level"
    DELETE_BUILDING_LEVEL = "delete_building_level"
    UPDATE_BUILDING_LEVEL = "update_building_level"
    LINK_BUILDING_LEVEL_TO_BUILDING = "link_building_level_to_building"
    UNLINK_BUILDING_LEVEL_FROM_BUILDING = "unlink_building_level_from_building"
    CREATE_BUILDING_LEVEL_ROOM = "create_building_level_room"
    DELETE_BUILDING_LEVEL_ROOM = "delete_building_level_room"
    UPDATE_BUILDING_LEVEL_ROOM = "update_building_level_room"
    UPDATE_BUILDING_LEVEL_ROOM_INDEX = "update_building_level_room_index"
    CREATE_SUBCONTRACTOR = "create_subcontractor"
    DELETE_SUBCONTRACTOR = "delete_subcontractor"
    UPDATE_SUBCONTRACTOR = "update_subcontractor"
    ASSIGN_SUBCONTRACTOR_TO_ORGANIZATION = "assign_subcontractor_to_organization"
    REVOKE_ASSIGNMENT_SUBCONTRACTOR_TO_ORGANIZATION = (
        "revoke_assignment_subcontractor_to_organization"
    )
    UPDATE_ORGANIZATION = "update_organization"
    CREATE_EQUIPMENT_MODEL = "create_equipment_model"
    UPDATE_EQUIPMENT_MODEL = "update_equipment_model"
    DELETE_EQUIPMENT_MODEL = "delete_equipment_model"
    CREATE_MANUFACTURER = "create_manufacturer"
    UPDATE_MANUFACTURER = "update_manufacturer"
    DELETE_MANUFACTURER = "delete_manufacturer"
    CREATE_EQUIPMENT_PROJECT_CATEGORY = "create_equipment_project_category"
    UPDATE_EQUIPMENT_PROJECT_CATEGORY = "update_equipment_project_category"
    DELETE_EQUIPMENT_PROJECT_CATEGORY = "delete_equipment_project_category"
    CREATE_EQUIPMENT_CATEGORY = "create_equipment_category"
    UPDATE_EQUIPMENT_CATEGORY = "update_equipment_category"
    DELETE_EQUIPMENT_CATEGORY = "delete_equipment_category"
    CREATE_EQUIPMENT_CATEGORY_GROUP = "create_equipment_category_group"
    UPDATE_EQUIPMENT_CATEGORY_GROUP = "update_equipment_category_group"
    DELETE_EQUIPMENT_CATEGORY_GROUP = "delete_equipment_category_group"
    CREATE_EQUIPMENT = "create_equipment"
    UPDATE_EQUIPMENT = "update_equipment"
    DELETE_EQUIPMENT = "delete_equipment"
    CREATE_UNIT = "create_unit"
    UPDATE_UNIT = "update_unit"
    DELETE_UNIT = "delete_unit"
    CREATE_EQUIPMENT_INPUT = "create_equipment_input"
    UPDATE_EQUIPMENT_INPUT = "update_equipment_input"
    DELETE_EQUIPMENT_INPUT = "delete_equipment_input"
    CREATE_MAINTENANCE_PROCEDURE = "create_maintenance_procedure"
    UPDATE_MAINTENANCE_PROCEDURE = "update_maintenance_procedure"
    DELETE_MAINTENANCE_PROCEDURE = "delete_maintenance_procedure"
    CREATE_MAINTENANCE_PROCEDURE_OPERATION = "create_maintenance_procedure_operation"
    UPDATE_MAINTENANCE_PROCEDURE_OPERATION = "update_maintenance_procedure_operation"
    DELETE_MAINTENANCE_PROCEDURE_OPERATION = "delete_maintenance_procedure_operation"
    CREATE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER = (
        "create_maintenance_procedure_operation_parameter"
    )
    UPDATE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER = (
        "update_maintenance_procedure_operation_parameter"
    )
    DELETE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER = (
        "delete_maintenance_procedure_operation_parameter"
    )
    CREATE_DAILY_CHECK_PROCEDURE = "create_daily_check_procedure"
    UPDATE_DAILY_CHECK_PROCEDURE = "update_daily_check_procedure"
    DELETE_DAILY_CHECK_PROCEDURE = "delete_daily_check_procedure"
    CREATE_DAILY_CHECK_PROCEDURE_OPERATION = "create_daily_check_procedure_operation"
    UPDATE_DAILY_CHECK_PROCEDURE_OPERATION = "update_daily_check_procedure_operation"
    DELETE_DAILY_CHECK_PROCEDURE_OPERATION = "delete_daily_check_procedure_operation"
    CREATE_DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER = (
        "create_daily_check_procedure_operation_parameter"
    )
    UPDATE_DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER = (
        "update_daily_check_procedure_operation_parameter"
    )
    DELETE_DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER = (
        "delete_daily_check_procedure_operation_parameter"
    )
    CHANGE_PROJECT_STATE = "change_project_state"
    LINK_EQUIPMENT_PROJECT_CATEGORY_GROUP = "link_equipment_project_category_group"
    LINK_EQUIPMENT_TO_EQUIPMENT = "link_equipment_to_equipment"
    UNLINK_EQUIPMENT_TO_EQUIPMENT = "unlink_equipment_to_equipment"
    UNLINK_EQUIPMENT_PROJECT_CATEGORY_GROUP = "unlink_equipment_project_category_group"
    CREATE_STANDARD_MAINTENANCE_PROCEDURE = "create_standard_maintenance_procedure"
    UPDATE_STANDARD_MAINTENANCE_PROCEDURE = "update_standard_maintenance_procedure"
    DELETE_STANDARD_MAINTENANCE_PROCEDURE = "delete_standard_maintenance_procedure"
    CREATE_SUBCONTRACTOR_CATEGORY = "create_subcontractor_category"
    UPDATE_SUBCONTRACTOR_CATEGORY = "update_subcontractor_category"
    DELETE_SUBCONTRACTOR_CATEGORY = "delete_subcontractor_category"
    CREATE_STANDARD_EQUIPMENT_CATEGORY_GROUP = (
        "create_standard_equipment_category_group"
    )
    UPDATE_STANDARD_EQUIPMENT_CATEGORY_GROUP = (
        "update_standard_equipment_category_group"
    )
    DELETE_STANDARD_EQUIPMENT_CATEGORY_GROUP = (
        "delete_standard_equipment_category_group"
    )
    CREATE_STANDARD_EQUIPMENT_CATEGORY = "create_standard_equipment_category"
    UPDATE_STANDARD_EQUIPMENT_CATEGORY = "update_standard_equipment_category"
    DELETE_STANDARD_EQUIPMENT_CATEGORY = "delete_standard_equipment_category"
    CREATE_STANDARD_EQUIPMENT = "create_standard_equipment"
    UPDATE_STANDARD_EQUIPMENT = "update_standard_equipment"
    DELETE_STANDARD_EQUIPMENT = "delete_standard_equipment"
    LINK_ORGANIZATION_BUILDING = "link_organization_building"
    UNLINK_ORGANIZATION_BUILDING = "unlink_organization_building"
    PROCESS_BULK = "process_bulk"

    CREATE_TAG = 'create_tag'
    UPDATE_TAG = 'update_tag'
    DELETE_TAG = 'delete_tag'
    ASSIGN_TAG_TO_ROLE = 'assign_tag_to_role'

    CREATE_STANDARD_EQUIPMENT_PROJECT_CATEGORY = 'create_standard_equipment_project_category'
    UPDATE_STANDARD_EQUIPMENT_PROJECT_CATEGORY = 'update_standard_equipment_project_category'
    DELETE_STANDARD_EQUIPMENT_PROJECT_CATEGORY = 'delete_standard_equipment_project_category'
    CREATE_DAILY_CHECK_PROCEDURE_OPERATION_LABEL = 'create_daily_check_procedure_operation_label'
    UPDATE_DAILY_CHECK_PROCEDURE_OPERATION_LABEL = 'update_daily_check_procedure_operation_label'
    DELETE_DAILY_CHECK_PROCEDURE_OPERATION_LABEL = 'delete_daily_check_procedure_operation_label'
    CREATE_STANDARD_MAINTENANCE_PROCEDURE_OPERATION_LABEL = 'create_standard_maintenance_procedure_operation_label'
    UPDATE_STANDARD_MAINTENANCE_PROCEDURE_OPERATION_LABEL = 'update_standard_maintenance_procedure_operation_label'
    DELETE_STANDARD_MAINTENANCE_PROCEDURE_OPERATION_LABEL = 'delete_standard_maintenance_procedure_operation_label'
    CREATE_MAINTENANCE_PROCEDURE_OPERATION_LABEL = 'create_maintenance_procedure_operation_label'
    UPDATE_MAINTENANCE_PROCEDURE_OPERATION_LABEL = 'update_maintenance_procedure_operation_label'
    DELETE_MAINTENANCE_PROCEDURE_OPERATION_LABEL = 'delete_maintenance_procedure_operation_label'

# endregion
