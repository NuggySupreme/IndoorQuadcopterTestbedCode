// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from bed_messages:msg/PSControl.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__PS_CONTROL__BUILDER_HPP_
#define BED_MESSAGES__MSG__DETAIL__PS_CONTROL__BUILDER_HPP_

#include "bed_messages/msg/detail/ps_control__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace bed_messages
{

namespace msg
{

namespace builder
{

class Init_PSControl_turn_off
{
public:
  explicit Init_PSControl_turn_off(::bed_messages::msg::PSControl & msg)
  : msg_(msg)
  {}
  ::bed_messages::msg::PSControl turn_off(::bed_messages::msg::PSControl::_turn_off_type arg)
  {
    msg_.turn_off = std::move(arg);
    return std::move(msg_);
  }

private:
  ::bed_messages::msg::PSControl msg_;
};

class Init_PSControl_current
{
public:
  explicit Init_PSControl_current(::bed_messages::msg::PSControl & msg)
  : msg_(msg)
  {}
  Init_PSControl_turn_off current(::bed_messages::msg::PSControl::_current_type arg)
  {
    msg_.current = std::move(arg);
    return Init_PSControl_turn_off(msg_);
  }

private:
  ::bed_messages::msg::PSControl msg_;
};

class Init_PSControl_voltage
{
public:
  explicit Init_PSControl_voltage(::bed_messages::msg::PSControl & msg)
  : msg_(msg)
  {}
  Init_PSControl_current voltage(::bed_messages::msg::PSControl::_voltage_type arg)
  {
    msg_.voltage = std::move(arg);
    return Init_PSControl_current(msg_);
  }

private:
  ::bed_messages::msg::PSControl msg_;
};

class Init_PSControl_ps_num
{
public:
  Init_PSControl_ps_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PSControl_voltage ps_num(::bed_messages::msg::PSControl::_ps_num_type arg)
  {
    msg_.ps_num = std::move(arg);
    return Init_PSControl_voltage(msg_);
  }

private:
  ::bed_messages::msg::PSControl msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::bed_messages::msg::PSControl>()
{
  return bed_messages::msg::builder::Init_PSControl_ps_num();
}

}  // namespace bed_messages

#endif  // BED_MESSAGES__MSG__DETAIL__PS_CONTROL__BUILDER_HPP_
