// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from bed_messages:msg/PSControl.idl
// generated code does not contain a copyright notice
#include "bed_messages/msg/detail/ps_control__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
bed_messages__msg__PSControl__init(bed_messages__msg__PSControl * msg)
{
  if (!msg) {
    return false;
  }
  // ps_num
  // voltage
  // current
  // turn_off
  return true;
}

void
bed_messages__msg__PSControl__fini(bed_messages__msg__PSControl * msg)
{
  if (!msg) {
    return;
  }
  // ps_num
  // voltage
  // current
  // turn_off
}

bed_messages__msg__PSControl *
bed_messages__msg__PSControl__create()
{
  bed_messages__msg__PSControl * msg = (bed_messages__msg__PSControl *)malloc(sizeof(bed_messages__msg__PSControl));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(bed_messages__msg__PSControl));
  bool success = bed_messages__msg__PSControl__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
bed_messages__msg__PSControl__destroy(bed_messages__msg__PSControl * msg)
{
  if (msg) {
    bed_messages__msg__PSControl__fini(msg);
  }
  free(msg);
}


bool
bed_messages__msg__PSControl__Sequence__init(bed_messages__msg__PSControl__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  bed_messages__msg__PSControl * data = NULL;
  if (size) {
    data = (bed_messages__msg__PSControl *)calloc(size, sizeof(bed_messages__msg__PSControl));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = bed_messages__msg__PSControl__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        bed_messages__msg__PSControl__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
bed_messages__msg__PSControl__Sequence__fini(bed_messages__msg__PSControl__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      bed_messages__msg__PSControl__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

bed_messages__msg__PSControl__Sequence *
bed_messages__msg__PSControl__Sequence__create(size_t size)
{
  bed_messages__msg__PSControl__Sequence * array = (bed_messages__msg__PSControl__Sequence *)malloc(sizeof(bed_messages__msg__PSControl__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = bed_messages__msg__PSControl__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
bed_messages__msg__PSControl__Sequence__destroy(bed_messages__msg__PSControl__Sequence * array)
{
  if (array) {
    bed_messages__msg__PSControl__Sequence__fini(array);
  }
  free(array);
}
