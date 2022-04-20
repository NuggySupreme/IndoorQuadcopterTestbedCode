// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from bed_messages:msg/FanControl.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__TRAITS_HPP_
#define BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__TRAITS_HPP_

#include "bed_messages/msg/detail/fan_control__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<bed_messages::msg::FanControl>()
{
  return "bed_messages::msg::FanControl";
}

template<>
inline const char * name<bed_messages::msg::FanControl>()
{
  return "bed_messages/msg/FanControl";
}

template<>
struct has_fixed_size<bed_messages::msg::FanControl>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<bed_messages::msg::FanControl>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<bed_messages::msg::FanControl>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__TRAITS_HPP_
