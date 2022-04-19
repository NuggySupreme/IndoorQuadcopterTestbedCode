// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from bed_messages:msg/TableAngle.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__TRAITS_HPP_
#define BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__TRAITS_HPP_

#include "bed_messages/msg/detail/table_angle__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<bed_messages::msg::TableAngle>()
{
  return "bed_messages::msg::TableAngle";
}

template<>
inline const char * name<bed_messages::msg::TableAngle>()
{
  return "bed_messages/msg/TableAngle";
}

template<>
struct has_fixed_size<bed_messages::msg::TableAngle>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<bed_messages::msg::TableAngle>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<bed_messages::msg::TableAngle>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__TRAITS_HPP_
