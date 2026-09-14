# Car-Rental-System-Python

A CLI-based Car Rental System built in Python that manages vehicle rentals, calculates liability and full insurance options with a 5% rental tax, handles car returns with inventory tracking, and generates financial summaries.

## Features

### 1. Car Rental

The user can:

- View the available car models and their prices.
- Select a car type.
- Enter the number of rental days.
- Select an insurance type:
  - **L** — Liability Insurance
  - **F** — Full/Comprehensive Insurance
- View the rental cost, insurance cost, tax, and total bill.
- Continue with another operation or exit.

> The 5% tax is applied only to the rental cost, not to the insurance cost.

### 2. Car Return

- The user can select the type of car being returned.
- The program increases the available quantity of that car while preventing the available quantity from exceeding the original fleet quantity.

### 3. Print Totals

The program stores completed rental operations and displays:

- Individual rental records
- Rental income
- Total insurance collected
- Total tax collected

## Available Cars

The initial fleet configured in the program is:

| Car Model | Available | Rental / Day | Liability Insurance / Day | Comprehensive Insurance / Day |
|-----------|-----------|--------------|----------------------------|--------------------------------|
| Pajero    | 2         | 150 PKR      | 30 PKR                     | 70 PKR                         |
| Altima    | 2         | 70 PKR       | 20 PKR                     | 50 PKR                         |
| Camry     | 3         | 90 PKR       | 20 PKR                     | 50 PKR                         |

## Technologies Used

- Python 3
- Python built-in `copy` module
- Lists
- Dictionaries
- Functions
- Conditional statements
- Loops/iteration
- User input
- Basic data management

No external Python packages are required.

## Program Structure

The main functions in the program are:

**start_app()**
Displays the main menu:
```
MAIN MENU
1-Car Rent
2-Car Return
3-Print the totals
```

**bussiness_logic()**
Processes the user's main-menu selection and calls the appropriate operation.

**menu(cars_data)**
Displays the available car information, including model, availability, rental price, and insurance prices.

**car_rent()**
Handles the complete car-rental process, calculates the bill, records the operation, and decreases the available car count.

**car_return()**
Handles returned cars and increases the available quantity when the return is valid.

**print_totals()**
Displays stored rental operations and calculates total rental income, insurance, and tax.

**more_options()**
Allows the user to return to the main menu or stop the program.

## Cost Calculation

The rental cost is calculated as:

```
Rental Cost = Daily Rental Price × Number of Days
```

Tax is calculated as:

```
Tax = Rental Cost × 5%
```

The final bill is:

```
Total Bill = Rental Cost + Insurance Cost + Tax
```

## Data Management

The program uses a list of dictionaries to store the original car information.

A deep copy is then created for the current available-car data:

```python
available_cars_data = copy.deepcopy(car_rental_db)
```

This allows the program to update availability while preserving the original fleet quantities for return validation.

Completed rental operations are stored in:

```python
total_opreations
```

## Input Handling

The program checks several user selections and asks the user again when an invalid menu/car/insurance selection is entered.

Supported selections include:

- **Main menu:** 1, 2, 3
- **Car type:** 1, 2, 3
- **Insurance:** L or F (case-insensitive)
- **More operations:** Y or N (case-insensitive)

## Requirements

- Python 3.x (uses only the built-in `copy` module — no external dependencies)

## Running the Program

```bash
python Car_Rental_Project.py
```
