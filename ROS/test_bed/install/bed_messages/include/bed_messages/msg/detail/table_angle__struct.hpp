// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from bed_messages:msg/TableAngle.idl
// generated code does not contain a copyright notice

#ifndef BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__STRUCT_HPP_
#define BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__bed_messages__msg__TableAngle __attribute__((deprecated))
#else
# define DEPRECATED__bed_messages__msg__TableAngle __declspec(deprecated)
#endif

namespace bed_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TableAngle_
{
  using Type = TableAngle_<ContainerAllocator>;

  explicit TableAngle_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->roll = 0.0f;
      this->pitch = 0.0f;
    }
  }

  explicit TableAngle_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->roll = 0.0f;
      this->pitch = 0.0f;
    }
  }

  // field types and members
  using _roll_type =
    float;
  _roll_type roll;
  using _pitch_type =
    float;
  _pitch_type pitch;

  // setters for named parameter idiom
  Type & set__roll(
    const float & _arg)
  {
    this->roll = _arg;
    return *this;
  }
  Type & set__pitch(
    const float & _arg)
  {
    this->pitch = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    bed_messages::msg::TableAngle_<ContainerAllocator> *;
  using ConstRawPtr =
    const bed_messages::msg::TableAngle_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<bed_messages::msg::TableAngle_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<bed_messages::msg::TableAngle_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      bed_messages::msg::TableAngle_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<bed_messages::msg::TableAngle_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      bed_messages::msg::TableAngle_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<bed_messages::msg::TableAngle_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<bed_messages::msg::TableAngle_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<bed_messages::msg::TableAngle_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__bed_messages__msg__TableAngle
    std::shared_ptr<bed_messages::msg::TableAngle_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__bed_messages__msg__TableAngle
    std::shared_ptr<bed_messages::msg::TableAngle_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TableAngle_ & other) const
  {
    if (this->roll != other.roll) {
      return false;
    }
    if (this->pitch != other.pitch) {
      return false;
    }
    return true;
  }
  bool operator!=(const TableAngle_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TableAngle_

// alias to use template instance with default allocator
using TableAngle =
  bed_messages::msg::TableAngle_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace bed_messages

#endif  // BED_MESSAGES__MSG__DETAIL__TABLE_ANGLE__STRUCT_HPP_
