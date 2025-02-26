import requests
nodes = ["http://localhost:5000", "http://localhost:5001"]

def broadcast_transaction(transaction):
    for node in nodes:
        try:
            response = requests.post(f"{node}/transaction/new", json=transaction)
            print(f"Broadcasted to {node}: {response.json()}")
        except Exception as e:
            print(f"Failed to reach {node}: {e}")

if __name__ == "__main__":
    sample_tx = {"sender": "Alice", "receiver": "Bob", "amount": 10}
    broadcast_transaction(sample_tx)
