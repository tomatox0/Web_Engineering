# order-management

## ADDED Requirements

### Requirement: Order lifecycle defined

The order management module SHALL track customer orders through a defined lifecycle with status transitions.

#### Scenario: Order status transitions
- **WHEN** an agent designs order statuses
- **THEN** the valid transitions MUST be documented in the order management spec
- **THEN** the `apps/orders/services.py` SHALL enforce valid transitions

#### Scenario: Order status change tests
- **WHEN** an agent implements order status changes
- **THEN** tests MUST be added for each transition in the status lifecycle

### Requirement: Business logic in services layer

All order business workflow logic SHALL live in a services layer, not in views or serializers.

#### Scenario: Service layer separation
- **WHEN** an agent implements order creation, status transitions, or fulfillment
- **THEN** the logic MUST be in `apps/orders/services.py`
- **THEN** views and serializers MUST call into services, not implement business rules

### Requirement: Read logic in selectors

Reusable query logic for orders SHALL live in a selectors layer.

#### Scenario: Selector separation
- **WHEN** an agent implements order queries (list, filter, search)
- **THEN** the query logic MUST be in `apps/orders/selectors.py`
