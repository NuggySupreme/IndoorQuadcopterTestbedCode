// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from bed_messages:msg/FanControl.idl
// generated code does not contain a copyright notice
#include "bed_messages/msg/detail/fan_control__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
bed_messages__msg__FanControl__init(bed_messages__msg__FanControl * msg)
{
  if (!msg) {
    return false;
  }
  // channel
  // address
  // speed
  return true;
}

void
bed_messages__msg__FanControl__fini(bed_messages__msg__FanControl * msg)
{
  if (!msg) {
    return;
  }
  // channel
  // address
  // speed
}

bed_messages__msg__FanControl *
bed_messages__msg__FanControl__create()
{
  bed_messages__msg__FanControl * msg = (bed_messages__msg__FanControl *)malloc(sizeof(bed_messages__msg__FanControl));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(bed_messages__msg__FanControl));
  bool success = bed_messages__msg__FanControl__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
bed_messages__msg__FanControl__destroy(bed_messages__msg__FanControl * msg)
{
  if (msg) {
    bed_messages__msg__FanControl__fini(msg);
  }
  free(msg);
}


bool
bed_messages__msg__FanControl__Sequence__init(bed_messages__msg__FanControl__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  bed_messages__msg__FanControl * data = NULL;
  if (size) {
    data = (bed_messages__msg__FanControl *)calloc(size, sizeof(bed_messages__msg__FanControl));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = bed_messages__msg__FanControl__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        bed_messages__msg__FanControl__fini(&data[i - 1]);
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
bed_messages__msg__FanControl__Sequence__fini(bed_messages__msg__FanControl__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      bed_messages__msg__FanControl__fini(&array->data[i]);
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

bed_messages__msg__FanControl__Sequence *
bed_messages__msg__FanControl__Sequence__create(size_t size)
{
  bed_messages__msg__FanControl__Sequence * array = (bed_messages__msg__FanControl__Sequence *)malloc(sizeof(bed_messages__msg__FanControl__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = bed_messages__msg__FanControl__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
bed_messages__msg__FanControl__Sequence__destroy(bed_messages__msg__FanControl__Sequence * array)
{
  if (array) {
    bed_messages__msg__FanControl__Sequence__fini(array);
  }
  free(array);
}
