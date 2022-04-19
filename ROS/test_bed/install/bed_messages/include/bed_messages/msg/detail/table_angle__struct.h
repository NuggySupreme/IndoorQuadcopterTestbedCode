// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from bed_messages:msg/TableAngle.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__STRUCT_H_
#define BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/TableAngle in the package bed_messages.
typedef struct bed_messages__msg__TableAngle
{
  float roll;
  float pitch;
} bed_messages__msg__TableAngle;

// Struct for a sequence of bed_messages__msg__TableAngle.
typedef struct bed_messages__msg__TableAngle__Sequence
{
  bed_messages__msg__TableAngle * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} bed_messages__msg__TableAngle__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__STRUCT_H_
