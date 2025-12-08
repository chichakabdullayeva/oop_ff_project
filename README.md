# Hotel Reservation System

A simple, console-based Hotel Reservation System built with Python demonstrating Object-Oriented Programming principles and design patterns.

## Features

- ✅ **Room Management**: Add and view hotel rooms
- ✅ **Guest Management**: Register and view guests
- ✅ **Reservations**: Create, view, and cancel reservations
- ✅ **Payments**: Process cash and card payments
- ✅ **Data Persistence**: JSON-based storage
- ✅ **Console Interface**: Simple text-based menu

## OOP Concepts Demonstrated

### Core OOP Principles
- **Abstraction**: BaseModel, BaseRepository, Payment base class
- **Encapsulation**: All models encapsulate their data with private attributes
- **Inheritance**: Payment hierarchy (Payment → CashPayment, CardPayment)
- **Polymorphism**: Different payment types process differently

### Design Principles

#### SOLID
- **S**ingle Responsibility: Each class has one clear purpose
- **O**pen/Closed: Payment hierarchy is extensible
- **L**iskov Substitution: Payment subclasses are interchangeable
- **I**nterface Segregation: Clean, focused interfaces
- **D**ependency Inversion: Service depends on abstractions

#### GRASP
- **Controller**: ReservationService orchestrates operations
- **Creator**: Factories handle object creation
- **Low Coupling**: Independent, loosely-coupled classes
- **High Cohesion**: Focused class responsibilities

#### CUPID
- **Composable**: Components work together seamlessly
- **Understandable**: Simple, readable code
- **Predictable**: Consistent behavior
- **Idiomatic**: Follows Python conventions
- **Domain-based**: Real-world naming

## Design Patterns

### 1. Singleton Pattern
**JSONStorage** ensures only one storage instance exists

```python
class JSONStorage:
    _instance = None
    
    def __new__(cls, file_path):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### 2. Factory Pattern
**PaymentFactory** creates payment objects based on type

```python
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type, reservation_id, amount, card_number=""):
        if payment_type == "cash":
            return CashPayment(reservation_id, amount)
        elif payment_type == "card":
            return CardPayment(reservation_id, amount, card_number)
```

## Project Structure

```
oop_ff_Project/
│
├── src/
│   ├── models/              # Domain models
│   │   ├── base.py         # BaseModel (abstraction)
│   │   ├── room.py         # Room model
│   │   ├── guest.py        # Guest model
│   │   ├── reservation.py  # Reservation model
│   │   └── payment.py      # Payment hierarchy (inheritance & polymorphism)
│   │
│   ├── repositories/        # Data access layer
│   │   ├── base_repository.py      # Base CRUD operations
│   │   ├── json_storage.py         # Singleton storage
│   │   ├── room_repository.py
│   │   ├── guest_repository.py
│   │   ├── reservation_repository.py
│   │   └── payment_repository.py
│   │
│   ├── services/            # Business logic
│   │   └── reservation_service.py  # Controller (GRASP)
│   │
│   ├── factories/           # Factory pattern
│   │   └── payment_factory.py
│   │
│   ├── utils/               # Utilities
│   │   └── logging_config.py
│   │
│   └── data/                # JSON storage
│       └── hotel_data.json
│
├── tests/                   # Unit tests
│   ├── test_models.py
│   └── test_reservation_service.py
│
├── docs/                    # Documentation
│   ├── TECHNICAL_NEW.md    # Technical documentation
│   └── USER_GUIDE_NEW.md   # User guide
│
└── main.py                  # Console application entry point
```

## Quick Start

### 1. Run the Application

```bash
python main.py
```

### 2. Basic Workflow

1. **Add a room**: Option 1
2. **Add a guest**: Option 3
3. **Create reservation**: Option 5
4. **Make payment**: Option 8

### 3. Run Tests

```bash
python -m unittest discover tests
```

## Example Usage

```
==================================================
     HOTEL RESERVATION SYSTEM
==================================================
1. Add Room
2. View Rooms
3. Add Guest
4. View Guests
5. Create Reservation
6. View Reservations
7. Cancel Reservation
8. Make Payment
9. View Payments
0. Exit
==================================================

Enter your choice: 1

--- Add Room ---
Room number: 101
Room type: standard
Price per night: 100.0
Capacity: 2
✓ Room added successfully!
```

## Class Hierarchy

### Payment Hierarchy (Inheritance & Polymorphism)

```
Payment (Base Class)
├── process() method
├── CashPayment
│   └── process() override
└── CardPayment
    └── process() override
```

**Demonstrates**:
- Inheritance: CashPayment and CardPayment inherit from Payment
- Polymorphism: Each payment type processes differently

## CRUD Operations

All repositories support full CRUD:

- **Create**: Add new records
- **Read**: Get by ID or get all
- **Update**: Modify existing records
- **Delete**: Remove records

## Exception Handling

Comprehensive error handling throughout:
- File I/O operations (try/except)
- Business logic validation
- User input validation
- Logging for debugging

## Testing

### Test Coverage

- ✅ Model creation and validation
- ✅ Inheritance testing
- ✅ Polymorphism demonstration
- ✅ Service operations
- ✅ Factory pattern functionality

### Run All Tests

```bash
python -m unittest discover tests -v
```

## Requirements

- Python 3.7+
- No external dependencies (uses only Python standard library)

## Key Features Implementation

### 1. Four Core Classes (Interconnected)
- **Room**: Hotel room entity
- **Guest**: Customer entity
- **Reservation**: Links guests and rooms
- **Payment**: Payment processing (with subclasses)

### 2. Controller Pattern
- **ReservationService**: Acts as controller following GRASP principles

### 3. Repository Pattern
- Abstraction for data access
- Follows Dependency Inversion Principle

### 4. Data Storage
- JSON file-based storage
- Singleton pattern for storage management

### 5. Console UI
- Interactive text-based menu
- Complete CRUD operations
- User-friendly prompts

## Documentation

- **TECHNICAL_NEW.md**: Architecture, design principles, patterns
- **USER_GUIDE_NEW.md**: How to use the system
- **README.md**: Project overview (this file)

## Code Quality

### Characteristics
- ✅ Simple, readable code
- ✅ Humanized variable names
- ✅ Clear comments and docstrings
- ✅ No unnecessary complexity
- ✅ Follows Python conventions (PEP 8)

### Principles Applied
- Single Responsibility
- Don't Repeat Yourself (DRY)
- Keep It Simple (KISS)
- Separation of Concerns

