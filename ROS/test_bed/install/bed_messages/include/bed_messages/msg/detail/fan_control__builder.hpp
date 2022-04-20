// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from bed_messages:msg/FanControl.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__BUILDER_HPP_
#define BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__BUILDER_HPP_

#include "bed_messages/msg/detail/fan_control__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace bed_messages
{

namespace msg
{

namespace builder
{

class Init_FanControl_speed
{
public:
  explicit Init_FanControl_speed(::bed_messages::msg::FanControl & msg)
  : msg_(msg)
  {}
  ::bed_messages::msg::FanControl speed(::bed_messages::msg::FanControl::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::bed_messages::msg::FanControl msg_;
};

class Init_FanControl_address
{
public:
  explicit Init_FanControl_address(::bed_messages::msg::FanControl & msg)
  : msg_(msg)
  {}
  Init_FanControl_speed address(::bed_messages::msg::FanControl::_address_type arg)
  {
    msg_.address = std::move(arg);
    return Init_FanControl_speed(msg_);
  }

private:
  ::bed_messages::msg::FanControl msg_;
};

class Init_FanControl_channel
{
public:
  Init_FanControl_channel()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FanControl_address channel(::bed_messages::msg::FanControl::_channel_type arg)
  {
    msg_.channel = std::move(arg);
    return Init_FanControl_address(msg_);
  }

private:
  ::bed_messages::msg::FanControl msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::bed_messages::msg::FanControl>()
{
  return bed_messages::msg::builder::Init_FanControl_channel();
}

}  // namespace bed_messages

#endif  // BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__BUILDER_HPP_
