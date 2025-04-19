# PyQt5 Calculator

A modern desktop calculator application built with Python and PyQt5, featuring a clean dark-themed UI and comprehensive calculation functionality. This elegant calculator mimics the look and feel of modern operating system calculators while providing robust mathematical capabilities for everyday use. The intuitive interface combines aesthetic appeal with practical functionality, making calculations effortless and efficient.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division with precise calculation handling
- **Advanced Functions**: Square, square root, reciprocal, percentage calculations for more complex mathematical needs
- **User-Friendly UI**: Dark theme with responsive buttons designed for optimal visual comfort during extended use
- **Keyboard Support**: Use your keyboard for quick calculations, enhancing productivity and user experience
- **Number Formatting**: Proper comma separation for large numbers to improve readability of calculation results
- **Error Handling**: Prevents division by zero and other calculation errors with informative error messages
- **Responsive Design**: Clean layout adapts well to different screen resolutions and display settings

## Requirements

- Python 3.6 or newer versions required for compatibility with modern dependencies
- PyQt5 framework for the graphical user interface components and styling capabilities
- Standard Python libraries including sys and math for core functionality
- Minimal system requirements - runs efficiently on most modern computers

## Installation

1. Make sure you have Python installed on your system. The application is compatible with Python 3.6 and above.
2. Install the required dependencies by running the following command in your terminal or command prompt:

```bash
pip install -r requirements.txt
```

3. Download the complete source code from this repository to your local machine.
4. Navigate to the directory containing the calculator application files.
5. Run the application using Python:

```bash
python calculator.py
```

The calculator window should appear immediately, ready for use with all functionality available.

## Usage

### Mouse Controls

- Click on the number buttons (0-9) to input numbers for your calculations
- Click on operation buttons (+, -, ×, ÷) to perform calculations between entered values
- Use "=" to calculate and display the final result of your mathematical expression
- "C" clears all input and calculations, providing a fresh start for new calculations
- "CE" clears the current entry only while preserving previous calculation steps
- "⌫" removes the last digit entered, allowing for quick corrections of mistyped numbers
- "±" toggles between positive and negative numbers for convenient sign changes
- "." adds a decimal point for precise fractional values in calculations
- "%" calculates percentages based on the current calculation context
- "x²" squares the current number instantly for exponential calculations
- "²√x" calculates the square root of the displayed number with mathematical precision
- "⅟x" calculates the reciprocal (1/x) for inverse value operations

### Keyboard Controls

- **Numbers**: 0-9 keys for rapid numerical input
- **Operations**: +, -, *, / for standard mathematical operations
- **Equals**: = key processes the complete calculation
- **Clear All**: Escape key resets the calculator completely
- **Clear Entry**: Delete key removes only the current input
- **Backspace**: Backspace key deletes the last character entered
- **Decimal Point**: . (period) adds decimal precision to numbers
- **Square**: Q key quickly squares the displayed value
- **Square Root**: @ key calculates square root instantly
- **Percentage**: % key performs percentage calculations
- **Reciprocal**: R key computes the reciprocal of the current value

## Technical Details

This calculator is built with PyQt5, a powerful set of Python bindings for the Qt application framework. The architecture implements:

- QMainWindow as the main application window providing the foundational structure
- QGridLayout for organizing the calculator buttons in a precise, responsive grid
- QPushButton for interactive, styled buttons with hover and press effects
- QLabel for displaying calculations and results with appropriate formatting
- Custom CSS styling via Qt stylesheets for the modern dark-themed appearance
- Comprehensive event handling for both mouse clicks and keyboard input
- Advanced number formatting algorithms for proper display of calculation results

## Code Structure

- `Calculator` class: Main application class encapsulating all functionality
- User interface setup in the `ui()` method with detailed component configuration
- Specialized number and operation handling methods for mathematical precision
- Keyboard event handling via `keyPressEvent` for convenient keyboard shortcuts
- Helper functions for number formatting and display optimization
- Clear separation of UI and calculation logic for maintainable code architecture

## Acknowledgments

- Inspired heavily by Windows Calculator design for intuitive user experience
