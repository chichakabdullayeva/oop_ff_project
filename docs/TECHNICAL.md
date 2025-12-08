# Hotel Reservation System - Technical Documentation

## Project Overview
A simple, console-based Hotel Reservation System built with Python using OOP principles and design patterns.

## Architecture

### Directory Structure
```
src/
    models/         # Domain models (Room, Guest, Reservation, Payment)
    repositories/   # Data access layer (CRUD operations)
    services/       # Business logic layer
    factories/      # Factory pattern for creating objects
    utils/          # Utility functions (logging)
    data/           # JSON storage files
tests/              # Unit tests
docs/               # Documentation
main.py             # Console application entry point
```

## Core Classes and Responsibilities

### Models (`src/models/`)

#### BaseModel
- **Purpose**: Base class for all models
- **Responsibility**: Provides ID generation and dictionary conversion
- **OOP Concepts**: Abstraction, Inheritance

#### Room
- **Attributes**: id, number, room_type, price_per_night, capacity, is_available
- **Responsibility**: Represents a hotel room
- **OOP Concepts**: Encapsulation

#### Guest
- **Attributes**: id, name, email, phone
- **Responsibility**: Represents a hotel guest
- **OOP Concepts**: Encapsulation

#### Reservation
- **Attributes**: id, guest_id, room_id, check_in_date, check_out_date, status
- **Responsibility**: Links guests to rooms with booking dates
- **Validation**: Ensures check-out date is after check-in date
- **OOP Concepts**: Encapsulation, Validation

#### Payment (Base Class)
- **Attributes**: id, reservation_id, amount, status, payment_type
- **Responsibility**: Base class for all payment types
- **Methods**: process() - can be overridden by subclasses
- **OOP Concepts**: Abstraction, Polymorphism

#### CashPayment (Inherits from Payment)
- **Responsibility**: Handles cash payments
- **OOP Concepts**: Inheritance, Polymorphism

#### CardPayment (Inherits from Payment)
- **Attributes**: Adds card_number
- **Responsibility**: Handles card payments
- **OOP Concepts**: Inheritance, Polymorphism

### Repositories (`src/repositories/`)

#### JSONStorage (Singleton Pattern)
- **Purpose**: Manages JSON file operations
- **Pattern**: Singleton - ensures only one instance exists
- **Methods**: read_all(), write_all(), read_collection(), write_collection()

#### BaseRepository
- **Purpose**: Provides CRUD operations for all models
- **Principle**: Dependency Inversion - depends on storage abstraction
- **Methods**: create(), get_by_id(), get_all(), update(), delete()

#### Specific Repositories
- RoomRepository
- GuestRepository
- ReservationRepository
- PaymentRepository

All inherit from BaseRepository and specialize for their model type.

### Factories (`src/factories/`)

#### PaymentFactory (Factory Pattern)
- **Purpose**: Creates payment objects based on payment type
- **Pattern**: Factory - encapsulates object creation logic
- **Method**: create_payment(payment_type, reservation_id, amount, card_number)
- **Returns**: CashPayment, CardPayment, or base Payment object

### Services (`src/services/`)

#### ReservationService (Controller)
- **Purpose**: Orchestrates business operations
- **Pattern**: GRASP Controller
- **Principle**: Single Responsibility - handles business logic only
- **Dependencies**: All repositories (Dependency Inversion)

**Key Methods**:
- add_room(), get_all_rooms(), get_room()
- add_guest(), get_all_guests()
- create_reservation(), get_all_reservations(), cancel_reservation()
- process_payment(), get_all_payments()

## Design Principles Applied

### SOLID Principles

1. **Single Responsibility Principle (SRP)**
   - Each class has one responsibility
   - Room handles room data, Guest handles guest data, etc.
   - Repositories handle only data access
   - Service handles only business logic

2. **Open/Closed Principle (OCP)**
   - Payment hierarchy is open for extension (new payment types)
   - BaseRepository can be extended without modification

3. **Liskov Substitution Principle (LSP)**
   - CashPayment and CardPayment can replace Payment anywhere
   - All payment types have the same interface

4. **Interface Segregation Principle (ISP)**
   - Classes only have methods they need
   - No unnecessary methods forced on classes

5. **Dependency Inversion Principle (DIP)**
   - Service depends on repository abstraction, not concrete storage
   - Repositories depend on storage interface

### GRASP Principles

1. **Controller**: ReservationService acts as the controller
2. **Creator**: Factories create complex objects
3. **Low Coupling**: Classes are independent
4. **High Cohesion**: Each class has focused responsibility

### CUPID Principles

1. **Composable**: Components can work together
2. **Understandable**: Simple, readable code
3. **Predictable**: Consistent behavior
4. **Idiomatic**: Follows Python conventions
5. **Domain-based**: Names match real-world concepts

## Design Patterns Used

### 1. Singleton Pattern
- **Where**: JSONStorage class
- **Purpose**: Ensure only one storage instance
- **Implementation**: Uses `__new__` method to return same instance

### 2. Factory Pattern
- **Where**: PaymentFactory class
- **Purpose**: Create payment objects without specifying exact class
- **Benefits**: Centralizes object creation, easy to add new types

## Data Storage

- **Format**: JSON
- **Location**: src/data/hotel_data.json
- **Structure**:
```json
{
    "rooms": [],
    "guests": [],
    "reservations": [],
    "payments": []
}
```

## OOP Concepts Demonstrated

1. **Abstraction**: BaseModel, BaseRepository, Payment base class
2. **Encapsulation**: All models encapsulate their data
3. **Inheritance**: Payment hierarchy (CashPayment, CardPayment)
4. **Polymorphism**: Different payment types process differently

## Exception Handling

- Try/except blocks in:
  - Repository operations (file I/O)
  - Service operations (business logic)
  - Main console application (user input)
- Logging of errors for debugging

## Testing

- **Framework**: unittest
- **Coverage**: Models, Services, Factory pattern
- **Tests**:
  - Model creation and validation
  - Inheritance and polymorphism
  - Service operations
  - Factory pattern functionality

## Class Diagram (Text Format)

```
BaseModel
    ├── Room
    ├── Guest
    ├── Reservation
    └── Payment
            ├── CashPayment
            └── CardPayment

BaseRepository
    ├── RoomRepository
    ├── GuestRepository
    ├── ReservationRepository
    └── PaymentRepository

JSONStorage (Singleton)

PaymentFactory

ReservationService
    ├── uses RoomRepository
    ├── uses GuestRepository
    ├── uses ReservationRepository
    └── uses PaymentRepository
```
