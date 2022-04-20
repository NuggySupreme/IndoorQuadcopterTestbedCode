// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from bed_messages:msg/FanControl.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "bed_messages/msg/detail/fan_control__rosidl_typesupport_introspection_c.h"
#include "bed_messages/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "bed_messages/msg/detail/fan_control__functions.h"
#include "bed_messages/msg/detail/fan_control__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void FanControl__rosidl_typesupport_introspection_c__FanControl_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  bed_messages__msg__FanControl__init(message_memory);
}

void FanControl__rosidl_typesupport_introspection_c__FanControl_fini_function(void * message_memory)
{
  bed_messages__msg__FanControl__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember FanControl__rosidl_typesupport_introspection_c__FanControl_message_member_array[3] = {
  {
    "channel",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(bed_messages__msg__FanControl, channel),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "address",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(bed_messages__msg__FanControl, address),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(bed_messages__msg__FanControl, speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers FanControl__rosidl_typesupport_introspection_c__FanControl_message_members = {
  "bed_messages__msg",  // message namespace
  "FanControl",  // message name
  3,  // number of fields
  sizeof(bed_messages__msg__FanControl),
  FanControl__rosidl_typesupport_introspection_c__FanControl_message_member_array,  // message members
  FanControl__rosidl_typesupport_introspection_c__FanControl_init_function,  // function to initialize message memory (memory has to be allocated)
  FanControl__rosidl_typesupport_introspection_c__FanControl_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t FanControl__rosidl_typesupport_introspection_c__FanControl_message_type_support_handle = {
  0,
  &FanControl__rosidl_typesupport_introspection_c__FanControl_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_bed_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, bed_messages, msg, FanControl)() {
  if (!FanControl__rosidl_typesupport_introspection_c__FanControl_message_type_support_handle.typesupport_identifier) {
    FanControl__rosidl_typesupport_introspection_c__FanControl_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &FanControl__rosidl_typesupport_introspection_c__FanControl_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
