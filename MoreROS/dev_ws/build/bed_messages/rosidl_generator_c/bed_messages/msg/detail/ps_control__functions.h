// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from bed_messages:msg/PSControl.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__PS_CONTROL__FUNCTIONS_H_
#define BED_MESSAGES__MSG__DETAIL__PS_CONTROL__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "bed_messages/msg/rosidl_generator_c__visibility_control.h"

#include "bed_messages/msg/detail/ps_control__struct.h"

/// Initialize msg/PSControl message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * bed_messages__msg__PSControl
 * )) before or use
 * bed_messages__msg__PSControl__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
bool
bed_messages__msg__PSControl__init(bed_messages__msg__PSControl * msg);

/// Finalize msg/PSControl message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
void
bed_messages__msg__PSControl__fini(bed_messages__msg__PSControl * msg);

/// Create msg/PSControl message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * bed_messages__msg__PSControl__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
bed_messages__msg__PSControl *
bed_messages__msg__PSControl__create();

/// Destroy msg/PSControl message.
/**
 * It calls
 * bed_messages__msg__PSControl__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
void
bed_messages__msg__PSControl__destroy(bed_messages__msg__PSControl * msg);


/// Initialize array of msg/PSControl messages.
/**
 * It allocates the memory for the number of elements and calls
 * bed_messages__msg__PSControl__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
bool
bed_messages__msg__PSControl__Sequence__init(bed_messages__msg__PSControl__Sequence * array, size_t size);

/// Finalize array of msg/PSControl messages.
/**
 * It calls
 * bed_messages__msg__PSControl__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
void
bed_messages__msg__PSControl__Sequence__fini(bed_messages__msg__PSControl__Sequence * array);

/// Create array of msg/PSControl messages.
/**
 * It allocates the memory for the array and calls
 * bed_messages__msg__PSControl__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
bed_messages__msg__PSControl__Sequence *
bed_messages__msg__PSControl__Sequence__create(size_t size);

/// Destroy array of msg/PSControl messages.
/**
 * It calls
 * bed_messages__msg__PSControl__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_bed_messages
void
bed_messages__msg__PSControl__Sequence__destroy(bed_messages__msg__PSControl__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // BED_MESSAGES__MSG__DETAIL__PS_CONTROL__FUNCTIONS_H_
