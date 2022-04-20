// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from bed_messages:msg/FanControl.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__FUNCTIONS_H_
#define BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "bed_messages/msg/rosidl_generator_c__visibility_control.h"

#include "bed_messages/msg/detail/fan_control__struct.h"

/// Initialize msg/FanControl message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * bed_messages__msg__FanControl
 * )) before or use
 * bed_messages__msg__FanControl__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
bool
bed_messages__msg__FanControl__init(bed_messages__msg__FanControl * msg);

/// Finalize msg/FanControl message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
void
bed_messages__msg__FanControl__fini(bed_messages__msg__FanControl * msg);

/// Create msg/FanControl message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * bed_messages__msg__FanControl__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
bed_messages__msg__FanControl *
bed_messages__msg__FanControl__create();

/// Destroy msg/FanControl message.
/**
 * It calls
 * bed_messages__msg__FanControl__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
void
bed_messages__msg__FanControl__destroy(bed_messages__msg__FanControl * msg);


/// Initialize array of msg/FanControl messages.
/**
 * It allocates the memory for the number of elements and calls
 * bed_messages__msg__FanControl__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
bool
bed_messages__msg__FanControl__Sequence__init(bed_messages__msg__FanControl__Sequence * array, size_t size);

/// Finalize array of msg/FanControl messages.
/**
 * It calls
 * bed_messages__msg__FanControl__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
void
bed_messages__msg__FanControl__Sequence__fini(bed_messages__msg__FanControl__Sequence * array);

/// Create array of msg/FanControl messages.
/**
 * It allocates the memory for the array and calls
 * bed_messages__msg__FanControl__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
bed_messages__msg__FanControl__Sequence *
bed_messages__msg__FanControl__Sequence__create(size_t size);

/// Destroy array of msg/FanControl messages.
/**
 * It calls
 * bed_messages__msg__FanControl__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
void
bed_messages__msg__FanControl__Sequence__destroy(bed_messages__msg__FanControl__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__FUNCTIONS_H_
