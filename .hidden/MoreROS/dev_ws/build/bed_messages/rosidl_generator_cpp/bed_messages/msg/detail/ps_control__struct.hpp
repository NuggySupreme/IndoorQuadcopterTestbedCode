// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from bed_messages:msg/PSControl.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__PS_CONTROL__STRUCT_HPP_
#define BED_MESSAGES__MSG__DETAIL__PS_CONTROL__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__bed_messages__msg__PSControl __attribute__((deprecated))
#else
# define DEPRECATED__bed_messages__msg__PSControl __declspec(deprecated)
#endif

namespace bed_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PSControl_
{
  using Type = PSControl_<ContainerAllocator>;

  explicit PSControl_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ps_num = 0l;
      this->voltage = 0.0f;
      this->current = 0.0f;
      this->turn_off = 0l;
    }
  }

  explicit PSControl_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ps_num = 0l;
      this->voltage = 0.0f;
      this->current = 0.0f;
      this->turn_off = 0l;
    }
  }

  // field types and members
  using _ps_num_type =
    int32_t;
  _ps_num_type ps_num;
  using _voltage_type =
    float;
  _voltage_type voltage;
  using _current_type =
    float;
  _current_type current;
  using _turn_off_type =
    int32_t;
  _turn_off_type turn_off;

  // setters for named parameter idiom
  Type & set__ps_num(
    const int32_t & _arg)
  {
    this->ps_num = _arg;
    return *this;
  }
  Type & set__voltage(
    const float & _arg)
  {
    this->voltage = _arg;
    return *this;
  }
  Type & set__current(
    const float & _arg)
  {
    this->current = _arg;
    return *this;
  }
  Type & set__turn_off(
    const int32_t & _arg)
  {
    this->turn_off = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    bed_messages::msg::PSControl_<ContainerAllocator> *;
  using ConstRawPtr =
    const bed_messages::msg::PSControl_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<bed_messages::msg::PSControl_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<bed_messages::msg::PSControl_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      bed_messages::msg::PSControl_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<bed_messages::msg::PSControl_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      bed_messages::msg::PSControl_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<bed_messages::msg::PSControl_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<bed_messages::msg::PSControl_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<bed_messages::msg::PSControl_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__bed_messages__msg__PSControl
    std::shared_ptr<bed_messages::msg::PSControl_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__bed_messages__msg__PSControl
    std::shared_ptr<bed_messages::msg::PSControl_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PSControl_ & other) const
  {
    if (this->ps_num != other.ps_num) {
      return false;
    }
    if (this->voltage != other.voltage) {
      return false;
    }
    if (this->current != other.current) {
      return false;
    }
    if (this->turn_off != other.turn_off) {
      return false;
    }
    return true;
  }
  bool operator!=(const PSControl_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PSControl_

// alias to use template instance with default allocator
using PSControl =
  bed_messages::msg::PSControl_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace bed_messages

#endif  // BED_MESSAGES__MSG__DETAIL__PS_CONTROL__STRUCT_HPP_
