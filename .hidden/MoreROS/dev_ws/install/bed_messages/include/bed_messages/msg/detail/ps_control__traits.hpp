// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from bed_messages:msg/PSControl.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__PS_CONTROL__TRAITS_HPP_
#define BED_MESSAGES__MSG__DETAIL__PS_CONTROL__TRAITS_HPP_

#include "bed_messages/msg/detail/ps_control__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<bed_messages::msg::PSControl>()
{
  return "bed_messages::msg::PSControl";
}

template<>
inline const char * name<bed_messages::msg::PSControl>()
{
  return "bed_messages/msg/PSControl";
}

template<>
struct has_fixed_size<bed_messages::msg::PSControl>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<bed_messages::msg::PSControl>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<bed_messages::msg::PSControl>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // BED_MESSAGES__MSG__DETAIL__PS_CONTROL__TRAITS_HPP_
