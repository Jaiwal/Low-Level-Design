from abc import ABC, abstractmethod

# Base subscription interface
class Subscription(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass

class BasicSubscription(Subscription):
    def cost(self) -> int:
        return 100

# Base decorator
class SubscriptionAddon(Subscription):
    def __init__(self, wrapped_subscription: Subscription):
        self.wrapped_subscription = wrapped_subscription

    @abstractmethod
    def cost(self) -> int:
        pass

# Concrete decorators
class AdditionalDevice(SubscriptionAddon):
    def cost(self) -> int:
        return self.wrapped_subscription.cost() + 50

class OfflineDownloads(SubscriptionAddon):
    def cost(self) -> int:
        return self.wrapped_subscription.cost() + 75

# Main Execution
if __name__ == '__main__':
    subscription = OfflineDownloads(AdditionalDevice(BasicSubscription()))
    print(f"Cost of subscription with additional device and offline downloads: {subscription.cost()}")
