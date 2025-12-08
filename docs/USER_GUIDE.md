# Hotel Reservation System - User Guide

## Prerequisites

- Python 3.7 or higher
- No external libraries required (uses only Python standard library)

## Installation

1. Extract the project to your desired location
2. No additional installation required - the system is ready to run!

## Running the Application

Open a terminal/command prompt in the project directory and run:

```bash
python main.py
```

## Main Menu

When you start the application, you'll see this menu:

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
```

## How to Use Each Feature

### 1. Add Room

Add a new room to the hotel system.

**Steps**:
1. Select option `1`
2. Enter room number (e.g., "101")
3. Enter room type (e.g., "standard", "deluxe", "suite")
4. Enter price per night (e.g., 100.00)
5. Enter capacity (number of guests, e.g., 2)

**Example**:
```
Room number: 101
Room type: standard
Price per night: 100.0
Capacity: 2
```

### 2. View Rooms

Display all rooms in the system.

**Shows**:
- Room number
- Room type
- Price per night
- Availability status

### 3. Add Guest

Register a new guest in the system.

**Steps**:
1. Select option `3`
2. Enter guest name
3. Enter email address
4. Enter phone number

**Example**:
```
Guest name: John Doe
Email: john@example.com
Phone: 1234567890
```

### 4. View Guests

Display all registered guests.

### 5. Create Reservation

Create a new room reservation.

**Steps**:
1. Select option `5`
2. View list of available rooms
3. Select a room by entering its number
4. View list of registered guests
5. Select a guest by entering their number
6. Enter check-in date (format: YYYY-MM-DD)
7. Enter check-out date (format: YYYY-MM-DD)

**Example**:
```
Select room number: 1
Select guest number: 1
Check-in date: 2024-01-15
Check-out date: 2024-01-20
```

**Note**: Check-out date must be after check-in date.

### 6. View Reservations

Display all reservations in the system.

**Shows**:
- Reservation ID
- Guest ID
- Room ID
- Check-in and check-out dates
- Status (pending, confirmed, cancelled)

### 7. Cancel Reservation

Cancel an existing reservation.

**Steps**:
1. Select option `7`
2. View list of reservations
3. Select reservation number to cancel

**Note**: The room will become available again after cancellation.

### 8. Make Payment

Process a payment for a reservation.

**Steps**:
1. Select option `8`
2. View list of reservations
3. Select reservation number
4. Enter payment amount
5. Choose payment type:
   - Type "cash" for cash payment
   - Type "card" for card payment
6. If card payment, enter card number

**Example (Cash)**:
```
Select reservation number: 1
Payment amount: 500.00
Payment type: cash
```

**Example (Card)**:
```
Select reservation number: 1
Payment amount: 500.00
Payment type: card
Card number: 1234567890123456
```

### 9. View Payments

Display all processed payments.

**Shows**:
- Payment ID
- Amount
- Reservation ID
- Payment status

### 0. Exit

Exit the application.

## Data Storage

- All data is stored in: `src/data/hotel_data.json`
- Data persists between sessions
- You can delete this file to reset all data

## Error Messages

### "No rooms found"
- Add rooms first before creating reservations

### "No guests found"
- Register guests before creating reservations

### "No available rooms"
- All rooms are currently reserved

### "Room is not available"
- The selected room is already booked

### "Check-out date must be after check-in date"
- Enter valid dates for your reservation

## Tips

1. **Start Fresh**: Add rooms and guests before creating reservations
2. **Date Format**: Always use YYYY-MM-DD format for dates (e.g., 2024-01-15)
3. **Payment Types**: Currently supports "cash" and "card" payments
4. **Room Availability**: Cancel reservations to make rooms available again

## Testing

To run unit tests:

```bash
python -m unittest discover tests
```

This will run all tests and show results.

## Troubleshooting

### "File not found" errors
- The system will automatically create the data file on first run

### Data appears corrupted
- Delete `src/data/hotel_data.json` and restart the application

### Tests failing
- Make sure you're in the project root directory
- Ensure Python 3.7+ is installed

## Support

For issues or questions, refer to the TECHNICAL.md document for architecture details.
