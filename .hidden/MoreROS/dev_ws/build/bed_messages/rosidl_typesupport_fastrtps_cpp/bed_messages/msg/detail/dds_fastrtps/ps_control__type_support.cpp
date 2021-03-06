// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from bed_messages:msg/PSControl.idl
// generated code does not contain a copyright notice
#include "bed_messages/msg/detail/ps_control__rosidl_typesupport_fastrtps_cpp.hpp"
#include "bed_messages/msg/detail/ps_control__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace bed_messages
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_bed_messages
cdr_serialize(
  const bed_messages::msg::PSControl & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: ps_num
  cdr << ros_message.ps_num;
  // Member: voltage
  cdr << ros_message.voltage;
  // Member: current
  cdr << ros_message.current;
  // Member: turn_off
  cdr << ros_message.turn_off;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_bed_messages
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  bed_messages::msg::PSControl & ros_message)
{
  // Member: ps_num
  cdr >> ros_message.ps_num;

  // Member: voltage
  cdr >> ros_message.voltage;

  // Member: current
  cdr >> ros_message.current;

  // Member: turn_off
  cdr >> ros_message.turn_off;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_bed_messages
get_serialized_size(
  const bed_messages::msg::PSControl & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: ps_num
  {
    size_t item_size = sizeof(ros_message.ps_num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: voltage
  {
    size_t item_size = sizeof(ros_message.voltage);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: current
  {
    size_t item_size = sizeof(ros_message.current);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: turn_off
  {
    size_t item_size = sizeof(ros_message.turn_off);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_bed_messages
max_serialized_size_PSControl(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: ps_num
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: voltage
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: current
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: turn_off
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _PSControl__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const bed_messages::msg::PSControl *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _PSControl__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<bed_messages::msg::PSControl *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _PSControl__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const bed_messages::msg::PSControl *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _PSControl__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_PSControl(full_bounded, 0);
}

static message_type_support_callbacks_t _PSControl__callbacks = {
  "bed_messages::msg",
  "PSControl",
  _PSControl__cdr_serialize,
  _PSControl__cdr_deserialize,
  _PSControl__get_serialized_size,
  _PSControl__max_serialized_size
};

static rosidl_message_type_support_t _PSControl__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_PSControl__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace bed_messages

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_bed_messages
const rosidl_message_type_support_t *
get_message_type_support_handle<bed_messages::msg::PSControl>()
{
  return &bed_messages::msg::typesupport_fastrtps_cpp::_PSControl__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, bed_messages, msg, PSControl)() {
  return &bed_messages::msg::typesupport_fastrtps_cpp::_PSControl__handle;
}

#ifdef __cplusplus
}
#endif
