// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from bed_messages:msg/TableAngle.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__BUILDER_HPP_
#define BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__BUILDER_HPP_

#include "bed_messages/msg/detail/table_angle__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace bed_messages
{

namespace msg
{

namespace builder
{

class Init_TableAngle_pitch
{
public:
  explicit Init_TableAngle_pitch(::bed_messages::msg::TableAngle & msg)
  : msg_(msg)
  {}
  ::bed_messages::msg::TableAngle pitch(::bed_messages::msg::TableAngle::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return std::move(msg_);
  }

private:
  ::bed_messages::msg::TableAngle msg_;
};

class Init_TableAngle_roll
{
public:
  Init_TableAngle_roll()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TableAngle_pitch roll(::bed_messages::msg::TableAngle::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_TableAngle_pitch(msg_);
  }

private:
  ::bed_messages::msg::TableAngle msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::bed_messages::msg::TableAngle>()
{
  return bed_messages::msg::builder::Init_TableAngle_roll();
}

}  // namespace bed_messages

#endif  // BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__BUILDER_HPP_
