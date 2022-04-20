// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from bed_messages:msg/FanControl.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__STRUCT_HPP_
#define BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__bed_messages__msg__FanControl __attribute__((deprecated))
#else
# define DEPRECATED__bed_messages__msg__FanControl __declspec(deprecated)
#endif

namespace bed_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FanControl_
{
  using Type = FanControl_<ContainerAllocator>;

  explicit FanControl_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->channel = 0l;
      this->address = 0l;
      this->speed = 0.0f;
    }
  }

  explicit FanControl_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->channel = 0l;
      this->address = 0l;
      this->speed = 0.0f;
    }
  }

  // field types and members
  using _channel_type =
    int32_t;
  _channel_type channel;
  using _address_type =
    int32_t;
  _address_type address;
  using _speed_type =
    float;
  _speed_type speed;

  // setters for named parameter idiom
  Type & set__channel(
    const int32_t & _arg)
  {
    this->channel = _arg;
    return *this;
  }
  Type & set__address(
    const int32_t & _arg)
  {
    this->address = _arg;
    return *this;
  }
  Type & set__speed(
    const float & _arg)
  {
    this->speed = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    bed_messages::msg::FanControl_<ContainerAllocator> *;
  using ConstRawPtr =
    const bed_messages::msg::FanControl_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<bed_messages::msg::FanControl_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<bed_messages::msg::FanControl_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      bed_messages::msg::FanControl_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<bed_messages::msg::FanControl_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      bed_messages::msg::FanControl_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<bed_messages::msg::FanControl_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<bed_messages::msg::FanControl_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<bed_messages::msg::FanControl_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__bed_messages__msg__FanControl
    std::shared_ptr<bed_messages::msg::FanControl_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__bed_messages__msg__FanControl
    std::shared_ptr<bed_messages::msg::FanControl_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FanControl_ & other) const
  {
    if (this->channel != other.channel) {
      return false;
    }
    if (this->address != other.address) {
      return false;
    }
    if (this->speed != other.speed) {
      return false;
    }
    return true;
  }
  bool operator!=(const FanControl_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FanControl_

// alias to use template instance with default allocator
using FanControl =
  bed_messages::msg::FanControl_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace bed_messages

#endif  // BED_MESSAGES__MSG__DETAIL__FAN_CONTROL__STRUCT_HPP_
