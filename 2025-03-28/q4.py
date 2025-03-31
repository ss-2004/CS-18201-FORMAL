# Q4 Develop a formal specification of an online transaction processing system using Process Algebra.

class Process:
    def execute(self, input_data):
        raise NotImplementedError("Subclasses must implement the execute method.")

class User(Process):
    def execute(self, input_data):
        print("User requests a transaction.")
        return ("authenticate", input_data)

class Authentication(Process):
    def execute(self, input_data):
        if input_data.get("authenticated", False):
            print("Authentication successful.")
            return ("process_transaction", input_data)
        else:
            print("Authentication failed.")
            return ("terminate", None)

class Transaction(Process):
    def execute(self, input_data):
        print(f"Processing transaction: {input_data['transaction']}")
        input_data["status"] = "completed"
        return ("log_transaction", input_data)

class Logger(Process):
    def execute(self, input_data):
        print(f"Logging transaction: {input_data}")
        return ("terminate", None)

class OLTPSystem:
    def __init__(self):
        self.processes = {
            "user": User(),
            "authenticate": Authentication(),
            "process_transaction": Transaction(),
            "log_transaction": Logger()
        }

    def run(self, input_data):
        current_process = "user"
        while current_process != "terminate":
            next_process, input_data = self.processes[current_process].execute(input_data)
            current_process = next_process

if __name__ == "__main__":
    input_data = {
        "authenticated": True,
        "transaction": "Deposit $100"
    }
    system = OLTPSystem()
    system.run(input_data)
