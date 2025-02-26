import hashlib
import json
import time
from flask import Flask, request

app = Flask(__name__)
ledger = []
pending_transactions = []

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.tx_id = self.calculate_hash()
    
    def calculate_hash(self):
        tx_data = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}"
        return hashlib.sha256(tx_data.encode()).hexdigest()

@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    data = request.json
    tx = Transaction(data['sender'], data['receiver'], data['amount'])
    pending_transactions.append(tx.__dict__)
    return {"message": "Transaction added to pool", "tx_id": tx.tx_id}, 200

@app.route('/ledger', methods=['GET'])
def get_ledger():
    return {"ledger": ledger}, 200

if __name__ == '__main__':
    app.run(port=5000)
