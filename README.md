# DDD Interpreter (D3I)

Welcome to **DDD Interpreter (D3I)** – a tool designed for interpreting, analyzing, and transforming a specialized domain-specific language called **D3I**. This project enables developers to work with Domain-Driven Design (DDD) elements directly through the D3I language, allowing seamless conversion of domain models into multiple formats, as well as code generation to support domain-centric software systems.

**Domain-Driven Design** (DDD) has been embraced by major technology leaders like Netflix, Amazon, Uber, and LinkedIn to tackle the complex demands of their rapidly evolving businesses. These organizations leverage DDD to structure their systems in a way that reflects the real-world intricacies of their domains, from content recommendations and e-commerce logistics to ride-sharing and professional networking. By focusing on the core problem space, or "domain," these companies can maintain software architectures that are both highly flexible and deeply aligned with business goals, enabling them to continuously innovate and respond to new challenges.

With DDD, these companies build systems composed of modular, independent components that can scale and evolve. This enables them to introduce new features and services efficiently while keeping existing functionalities robust and maintainable. DDD's principles help ensure that software not only meets current needs but is also prepared to handle future growth and changes seamlessly.

## What is Domain-Driven Design (DDD)?

**Domain-Driven Design** (DDD) is a software design philosophy that emphasizes deep alignment between software and complex business requirements by focusing on the "domain" or problem area the software aims to address. DDD promotes collaboration between developers and domain experts, leveraging structured design patterns to model and implement complex domains effectively.

## Core Elements of DDD Supported by D3I

The D3I language and the DDD Interpreter recognize and interpret all major components of Domain-Driven Design. The following are the DDD core elements supported by the interpreter:

- **Entities**  
  Entities are unique objects in the domain with a specific identity. DDD Interpreter reads D3I entity definitions, allowing these to be translated into relevant constructs and made available for further transformation or code generation.

- **Value Objects**  
  Value Objects represent descriptive characteristics within the domain without a unique identity, such as measurements or addresses. The interpreter integrates value objects into the domain model with precise mapping.

- **Aggregates and Aggregate Roots**  
  Aggregates are clusters of entities and value objects considered a single unit when handling data changes. The aggregate root serves as the primary access point, enforcing consistency within the aggregate. D3I syntax allows for defining aggregates, and the interpreter maintains integrity by validating these relationships.

- **Bounded Contexts**  
  A Bounded Context is a boundary within which a particular domain model applies. It allows different parts of a large system to operate with models tailored to their specific needs, avoiding conflicts and dependencies. The interpreter supports Bounded Contexts, enabling modularity and clear boundaries in complex systems.

- **Repositories**  
  Repositories abstract data access, providing methods to retrieve and store aggregates while hiding specifics of the data storage. DDD Interpreter translates repository structures into storage mechanisms based on the selected data layer.

- **Services**  
  Services encapsulate domain logic that doesn’t fit neatly within entities or value objects. These can be domain or application services, and the interpreter integrates them within the model to manage specialized processes in a standalone manner.

- **Interfaces**  
  Interfaces expose certain functionalities to external systems, making them accessible for integration without exposing underlying details. D3I allows for the definition of interfaces, which the interpreter structures as part of the external access layer.

- **Domain Events and Context Events**  
  Domain Events are meaningful occurrences within the domain itself, whereas Context Events are events that occur when data crosses bounded contexts. The interpreter supports both types of events, enabling integration in event-driven architectures and ensuring a clear distinction between internal and external domain events.

- **Anti-Corruption Layers (ACLs)**  
  Anti-Corruption Layers serve as boundaries between different systems, ensuring that an external system’s data and logic do not compromise the domain model's integrity. The interpreter recognizes ACL structures in D3I, implementing secure boundaries to maintain domain purity.

## Getting Started

To begin using DDD Interpreter in a Python environment, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/gyorgy-gulyas/d3i.git
    cd d3i
    ```

2. **Set up a virtual environment and install dependencies**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the interpreter**:
    ```bash
    python main.py
    ```

4. **Create a D3I file** with domain definitions. You can follow the syntax in the [example.d3i](examples/example.d3i) file for guidance.

## Example D3I Input

Below is a basic example of D3I input that DDD Interpreter can process:

```plaintext
entity Customer {
  id: UUID
  name: String
  email: String
}

aggregate Order {
  id: UUID
  customer: Customer
  items: List<OrderItem>
}

service OrderService {
  placeOrder(Customer, List<OrderItem>): Order
}

event OrderPlaced {
  orderId: UUID
  date: DateTime
}

acl ExternalSystemAcl {
  method: "fetchExternalOrder"
  params: {
    externalOrderId: String
  }
}
```

## Supported Outputs

Once you run DDD Interpreter on your D3I input file, you can generate various outputs:
- **Domain model diagrams** (e.g., UML, ERD)
- **Domain documentation** (Markdown, JSON)
- **Generated Code** (Python, C#)

## Contributing

We welcome contributions! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to submit pull requests, report issues, and request features.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

This README provides a comprehensive guide to the DDD Interpreter project, detailing the core DDD elements supported and how to get started with the Python-based interpreter. D3I makes it easier to model, interpret, and implement complex domains, enhancing productivity and alignment with domain-driven principles.
