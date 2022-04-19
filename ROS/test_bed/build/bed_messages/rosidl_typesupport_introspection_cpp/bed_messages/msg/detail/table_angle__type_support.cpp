// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from bed_messages:msg/TableAngle.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "bed_messages/msg/detail/table_angle__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace bed_messages
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TableAngle_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) bed_messages::msg::TableAngle(_init);
}

void TableAngle_fini_function(void * message_memory)
{
  auto typed_message = static_cast<bed_messages::msg::TableAngle *>(message_memory);
  typed_message->~TableAngle();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TableAngle_message_member_array[2] = {
  {
    "roll",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(bed_messages::msg::TableAngle, roll),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "pitch",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(bed_messages::msg::TableAngle, pitch),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TableAngle_message_members = {
  "bed_messages::msg",  // message namespace
  "TableAngle",  // message name
  2,  // number of fields
  sizeof(bed_messages::msg::TableAngle),
  TableAngle_message_member_array,  // message members
  TableAngle_init_function,  // function to initialize message memory (memory has to be allocated)
  TableAngle_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TableAngle_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TableAngle_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace bed_messages


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<bed_messages::msg::TableAngle>()
{
  return &::bed_messages::msg::rosidl_typesupport_introspection_cpp::TableAngle_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, bed_messages, msg, TableAngle)() {
  return &::bed_messages::msg::rosidl_typesupport_introspection_cpp::TableAngle_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
