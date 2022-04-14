// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from bed_messages:msg/PSControl.idl
// generated code does not contain a copyright notice
#include "bed_messages/msg/detail/ps_control__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "bed_messages/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "bed_messages/msg/detail/ps_control__struct.h"
#include "bed_messages/msg/detail/ps_control__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _PSControl__ros_msg_type = bed_messages__msg__PSControl;

static bool _PSControl__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _PSControl__ros_msg_type * ros_message = static_cast<const _PSControl__ros_msg_type *>(untyped_ros_message);
  // Field name: ps_num
  {
    cdr << ros_message->ps_num;
  }

  // Field name: voltage
  {
    cdr << ros_message->voltage;
  }

  // Field name: current
  {
    cdr << ros_message->current;
  }

  // Field name: turn_off
  {
    cdr << ros_message->turn_off;
  }

  return true;
}

static bool _PSControl__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _PSControl__ros_msg_type * ros_message = static_cast<_PSControl__ros_msg_type *>(untyped_ros_message);
  // Field name: ps_num
  {
    cdr >> ros_message->ps_num;
  }

  // Field name: voltage
  {
    cdr >> ros_message->voltage;
  }

  // Field name: current
  {
    cdr >> ros_message->current;
  }

  // Field name: turn_off
  {
    cdr >> ros_message->turn_off;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_bed_messages
size_t get_serialized_size_bed_messages__msg__PSControl(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _PSControl__ros_msg_type * ros_message = static_cast<const _PSControl__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name ps_num
  {
    size_t item_size = sizeof(ros_message->ps_num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name voltage
  {
    size_t item_size = sizeof(ros_message->voltage);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name current
  {
    size_t item_size = sizeof(ros_message->current);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name turn_off
  {
    size_t item_size = sizeof(ros_message->turn_off);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _PSControl__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_bed_messages__msg__PSControl(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_bed_messages
size_t max_serialized_size_bed_messages__msg__PSControl(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: ps_num
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: voltage
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: current
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: turn_off
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _PSControl__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_bed_messages__msg__PSControl(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_PSControl = {
  "bed_messages::msg",
  "PSControl",
  _PSControl__cdr_serialize,
  _PSControl__cdr_deserialize,
  _PSControl__get_serialized_size,
  _PSControl__max_serialized_size
};

static rosidl_message_type_support_t _PSControl__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_PSControl,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, bed_messages, msg, PSControl)() {
  return &_PSControl__type_support;
}

#if defined(__cplusplus)
}
#endif
