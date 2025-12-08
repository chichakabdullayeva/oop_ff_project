# OOP, SOLID, GRASP, and CUPID Principles Guide

## Project Structure with Principles

```
oop_ff_Project/
│
├── src/
│   ├── models/                    # OOP – Encapsulation: Domain entities
│   │   ├── base.py               # OOP – Inheritance: Base class for all models
│   │   │                         # GRASP – Information Expert: Knows ID generation
│   │   ├── guest.py              # SOLID – SRP: Only handles guest data
│   │   ├── room.py               # SOLID – SRP: Only handles room data
│   │   ├── reservation.py        # GRASP – Information Expert: Manages own dates/status
│   │   └── payment.py            # OOP – Inheritance: Payment hierarchy (Cash, Card)
│   │                             # SOLID – LSP: Subclasses can replace parent
│   │
│   ├── repositories/             # GRASP – Pure Fabrication: Separates persistence
│   │   ├── base_repository.py   # OOP – Inheritance: Abstract CRUD operations
│   │   │                         # SOLID – DIP: Depends on storage abstraction
│   │   ├── json_storage.py      # OOP – Singleton: Single storage instance
│   │   │                         # SOLID – SRP: Only handles JSON operations
│   │   ├── guest_repository.py  # SOLID – SRP: Guest persistence only
│   │   ├── room_repository.py   # SOLID – SRP: Room persistence only
│   │   ├── reservation_repository.py
│   │   └── payment_repository.py
│   │
│   ├── services/                 # GRASP – Controller: Coordinates business logic
│   │   └── reservation_service.py # SOLID – DIP: Depends on repositories
│   │                             # GRASP – Low Coupling: Minimal dependencies
│   │
│   ├── factories/                # OOP – Factory Pattern: Object creation
│   │   ├── payment_factory.py   # SOLID – OCP: Extensible for new payment types
│   │   │                         # GRASP – Creator: Decides which class to create
│   │   └── reservation_factory.py
│   │
│   └── utils/
│       └── logging_config.py     # SOLID – SRP: Only logging configuration
│                                 # CUPID – Idiomatic: Uses Python logging properly
│
└── main.py                       # GRASP – Pure Fabrication: UI presentation layer
                                  # GRASP – Controller: Application flow control

```

## Key Principles Applied

### OOP (Object-Oriented Programming)
1. **Inheritance**: `BaseModel` → `Guest`, `Room`, `Payment`
2. **Polymorphism**: Subclasses override `to_dict()`, `from_dict()`, `process()`
3. **Encapsulation**: Private attributes, public methods
4. **Abstraction**: BaseRepository defines interface for all repositories

### SOLID Principles
1. **SRP (Single Responsibility)**: Each class has one reason to change
   - `Guest` only manages guest data
   - `GuestRepository` only handles guest persistence
   - `PaymentFactory` only creates payments

2. **OCP (Open/Closed)**: Open for extension, closed for modification
   - Adding new payment types doesn't modify `PaymentFactory`
   - `RotatingFileHandler` extends logging without changing it

3. **LSP (Liskov Substitution)**: Subclasses can replace parent
   - `CashPayment`/`CardPayment` can replace `Payment`
   
4. **DIP (Dependency Inversion)**: Depend on abstractions
   - Service depends on repository interface, not concrete implementation

### GRASP Patterns
1. **Information Expert**: Objects handle their own data
   - `Reservation` validates its own dates
   - `Payment` processes itself

2. **Creator**: Objects create related objects
   - `ReservationService` creates `Room`, `Guest`, `Reservation`
   - `PaymentFactory` creates payment objects

3. **Controller**: Coordinates operations
   - `ReservationService` orchestrates business logic
   - `main.py` controls application flow

4. **Low Coupling**: Minimal dependencies
   - UI only talks to service, not repositories
   
5. **Pure Fabrication**: Non-domain objects for architecture
   - Repository pattern (not a real-world concept)
   - Factory pattern

### CUPID Principles
1. **Composable**: Services compose repositories
2. **Unix Philosophy**: Each module does one thing well
3. **Predictable**: Validates input (dates, amounts)
4. **Idiomatic**: Uses Python idioms (logging, `__str__`, properties)
5. **Domain-based**: Models reflect hotel domain

## Where to Find Each Principle

| Principle | Files | Line/Comment |
|-----------|-------|--------------|
| OOP – Inheritance | base.py, guest.py, room.py, payment.py | Class definitions |
| OOP – Polymorphism | All models | `to_dict()`, `from_dict()` |
| OOP – Singleton | json_storage.py | `__new__()` method |
| OOP – Factory | payment_factory.py | `create_payment()` |
| SOLID – SRP | All files | One responsibility per class |
| SOLID – OCP | payment_factory.py, logging_config.py | Extension without modification |
| SOLID – LSP | payment.py | CashPayment/CardPayment substitution |
| SOLID – DIP | reservation_service.py, base_repository.py | Depends on abstractions |
| GRASP – Controller | reservation_service.py, main.py | Coordinates operations |
| GRASP – Creator | reservation_service.py, payment_factory.py | Creates objects |
| GRASP – Information Expert | All models | Self-management |
| GRASP – Pure Fabrication | repositories/, factories/ | Architecture patterns |
| CUPID – Predictable | reservation.py, payment.py | Input validation |
| CUPID – Idiomatic | logging_config.py | Python idioms |
