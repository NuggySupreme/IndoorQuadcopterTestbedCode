// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from bed_messages:msg/PSControl.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "bed_messages/msg/detail/ps_control__rosidl_typesupport_introspection_c.h"
#include "bed_messages/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "bed_messages/msg/detail/ps_control__functions.h"
#include "bed_messages/msg/detail/ps_control__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void PSControl__rosidl_typesupport_introspection_c__PSControl_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  bed_messages__msg__PSControl__init(message_memory);
}

void PSControl__rosidl_typesupport_introspection_c__PSControl_fini_function(void * message_memory)
{
  bed_messages__msg__PSControl__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember PSControl__rosidl_typesupport_introspection_c__PSControl_message_member_array[4] = {
  {
    "ps_num",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(bed_messages__msg__PSControl, ps_num),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "voltage",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(bed_messages__msg__PSControl, voltage),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "current",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(bed_messages__msg__PSControl, current),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "turn_off",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(bed_messages__msg__PSControl, turn_off),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers PSControl__rosidl_typesupport_introspection_c__PSControl_message_members = {
  "bed_messages__msg",  // message namespace
  "PSControl",  // message name
  4,  // number of fields
  sizeof(bed_messages__msg__PSControl),
  PSControl__rosidl_typesupport_introspection_c__PSControl_message_member_array,  // message members
  PSControl__rosidl_typesupport_introspection_c__PSControl_init_function,  // function to initialize message memory (memory has to be allocated)
  PSControl__rosidl_typesupport_introspection_c__PSControl_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t PSControl__rosidl_typesupport_introspection_c__PSControl_message_type_support_handle = {
  0,
  &PSControl__rosidl_typesupport_introspection_c__PSControl_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_bed_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, bed_messages, msg, PSControl)() {
  if (!PSControl__rosidl_typesupport_introspection_c__PSControl_message_type_support_handle.typesupport_identifier) {
    PSControl__rosidl_typesupport_introspection_c__PSControl_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &PSControl__rosidl_typesupport_introspection_c__PSControl_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
