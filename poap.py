import random

class PoAPConsensus:
    def __init__(self, nodes):
        self.nodes = nodes

    def validate_transaction(self, tx):
        approval_count = 0
        required_approvals = len(self.nodes) // 2

        for node in self.nodes:
            if self.simulate_validation():
                approval_count += 1
        
        return approval_count >= required_approvals

    def simulate_validation(self):
        return random.choice([True, False])

if __name__ == "__main__":
    nodes = ["Node1", "Node2", "Node3", "Node4"]
    poap = PoAPConsensus(nodes)
    test_tx = {"sender": "Alice", "receiver": "Bob", "amount": 50}
    
    if poap.validate_transaction(test_tx):
        print("Transaction Approved")
    else:
        print("Transaction Rejected")
