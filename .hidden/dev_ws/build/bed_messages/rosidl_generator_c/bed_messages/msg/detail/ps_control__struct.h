// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from bed_messages:msg/PSControl.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__PS_CONTROL__STRUCT_H_
#define BED_MESSAGES__MSG__DETAIL__PS_CONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/PSControl in the package bed_messages.
typedef struct bed_messages__msg__PSControl
{
  int32_t ps_num;
  float voltage;
  float current;
  int32_t turn_off;
} bed_messages__msg__PSControl;

// Struct for a sequence of bed_messages__msg__PSControl.
typedef struct bed_messages__msg__PSControl__Sequence
{
  bed_messages__msg__PSControl * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} bed_messages__msg__PSControl__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // BED_MESSAGES__MSG__DETAIL__PS_CONTROL__STRUCT_H_
