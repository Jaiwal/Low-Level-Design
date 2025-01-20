# Decorator Design Pattern

## **What is the Decorator Pattern?**
The Decorator Pattern is a structural design pattern that allows you to dynamically add new behavior or responsibilities to an object without modifying its existing structure or code. It uses composition over inheritance by wrapping objects with decorator classes.

---

## **Why do we need it?**
1. **Extensibility**: Dynamically add or modify behavior at runtime without changing the existing code.
2. **Avoid Inheritance Explosion**: Prevents the creation of multiple subclasses for every combination of functionality.
3. **Adherence to SOLID Principles**:
   - **Single Responsibility Principle**: Each decorator class handles a single functionality.
   - **Open-Closed Principle**: Existing objects remain closed for modification but open for extension.

---

## **Where to use it?**
1. **Dynamic Features**: When objects need flexible, dynamic behavior (e.g., pizza toppings, UI elements like borders or scrollbars).
2. **Combinatorial Scenarios**: When multiple combinations of functionality are required.
3. **Transparent Extensions**: When enhanced behavior should be transparent to the object.

---

## **How to use it?**
1. **Define a Base Interface**: Start with a common interface or abstract class for the components.
2. **Create Concrete Implementations**: Define concrete classes for the base functionality.
3. **Create a Base Decorator**: Implement a base decorator class that wraps a component.
4. **Extend the Decorator**: Add concrete decorator classes for each additional feature.
5. **Compose Objects**: Dynamically apply one or more decorators to an object.

---

## **Problem it Solves**
- **Flexible Behavior Addition**: Avoids modifying or subclassing existing code to add behavior.
- **Avoids Inheritance Explosion**: Reduces the need for a large number of subclasses for feature combinations.
- **Runtime Behavior Changes**: Allows behavior to be added dynamically at runtime.

---

### Example Use Cases
1. **Pizza Ordering System**: Dynamically add toppings to a pizza.
2. **Video Streaming Platform**: Add features like offline downloads or multi-device support.
3. **UI Frameworks**: Add borders, scrollbars, or themes to UI components.
4. **Logging Frameworks**: Add contextual information like timestamps, log levels, or custom formats.

