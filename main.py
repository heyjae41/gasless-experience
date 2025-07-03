import os
import requests
import json

# --- Configuration ---
# IMPORTANT: Replace these with your actual data
CIRCLE_API_KEY = os.environ.get("CIRCLE_API_KEY", "YOUR_API_KEY_HERE")
CIRCLE_API_URL = "https://api-sandbox.circle.com/v1/w3s"

# A unique identifier for the user, managed by your application
USER_ID = "example-gasless-user-123"

# --- API Helper Functions ---

def api_request(method, endpoint, payload=None):
    """A helper function to make requests to the Circle API."""
    if CIRCLE_API_KEY == "YOUR_API_KEY_HERE":
        raise ValueError("Please replace 'YOUR_API_KEY_HERE' with your actual Circle API Key.")

    headers = {
        "Authorization": f"Bearer {CIRCLE_API_KEY}",
        "Content-Type": "application/json",
    }
    url = f"{CIRCLE_API_URL}{endpoint}"
    
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, json=payload)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()
        return response.json().get("data")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response body: {response.text}")
    except Exception as err:
        print(f"An other error occurred: {err}")
    return None

# --- Core Logic ---

def initialize_user_wallet(user_id):
    """
    Initializes a user-controlled wallet and returns the challenge ID for PIN/Passkey setup.
    """
    print(f"Initializing wallet for user: {user_id}")
    payload = {"userIds": [user_id]}
    return api_request('POST', '/users/initialize', payload)

def create_programmable_wallet(user_token, account_type="SCA", blockchains=["ETH-SEPOLIA"]):
    """
    Creates a new programmable wallet for the user.
    """
    print(f"Creating programmable wallet for user with token: {user_token[:10]}...")
    payload = {
        "accountType": account_type,
        "blockchains": blockchains,
        "userToken": user_token # This token is obtained after user initialization challenge
    }
    return api_request('POST', '/wallets', payload)

def simulate_gasless_transaction(wallet_id, destination_address, amount, currency="USD"): 
    """
    Simulates a gasless transaction from a programmable wallet.
    In a real scenario, this would involve signing a transaction and the Gas Station
    automatically sponsoring the gas.
    """
    print(f"Simulating gasless transaction from wallet {wallet_id}...")
    # This is a conceptual representation. The actual API call for a gasless transaction
    # would typically be initiated from the client-side SDK or a backend service
    # that integrates with the Programmable Wallets and Gas Station.
    # The Gas Station policy would automatically pick up and sponsor the gas.
    
    # Example of what a transfer payload might look like (simplified):
    transfer_payload = {
        "walletId": wallet_id,
        "destinationAddress": destination_address,
        "amount": {"amount": str(amount), "currency": currency},
        "chain": "ETH-SEPOLIA" # Assuming Sepolia for this example
    }
    print("Simulated transaction details:")
    print(json.dumps(transfer_payload, indent=2))
    print("\n--> Gas Station would automatically sponsor the gas for this transaction based on configured policies.")
    return {"status": "SIMULATED_SUCCESS", "transactionId": "sim-tx-123"}

if __name__ == "__main__":
    print("--- Creating a Gasless Experience with Circle ---")

    try:
        # 1. Initialize a user. This is the first step to creating a user-controlled wallet.
        # It returns a challenge to be completed on the client-side (e.g., in a mobile app).
        init_data = initialize_user_wallet(USER_ID)
        if init_data:
            print("\nStep 1: User initialization successful.")
            print(f"Challenge ID: {init_data.get('challengeId')}")
            print("Action: Complete this challenge on a client device to get a user_token.")
        else:
            raise Exception("User initialization failed.")

        # 2. (SIMULATED) Assume the user completes the challenge and we get a user_token.
        # In a real application, you would receive this token from your client-side integration.
        simulated_user_token = "SIMULATED_USER_TOKEN_FROM_CHALLENGE"
        print(f"\nStep 2: (SIMULATED) User challenge completed, obtained user_token: {simulated_user_token[:10]}...")

        # 3. Create a programmable wallet for the user.
        # This wallet will be a Smart Contract Account (SCA) which is required for gasless transactions.
        wallet_creation_data = create_programmable_wallet(simulated_user_token)
        if wallet_creation_data:
            print("\nStep 3: Programmable Wallet created successfully.")
            print(f"Wallet ID: {wallet_creation_data.get('id')}")
            created_wallet_id = wallet_creation_data.get('id')
        else:
            raise Exception("Programmable Wallet creation failed.")

        # 4. (SIMULATED) Configure Gas Station policies in the Circle Developer Console.
        # This step is done manually in the console, not via API.
        print("\nStep 4: (MANUAL) Configure Gas Station policies in the Circle Developer Console.")
        print("Ensure policies are set to sponsor gas for transactions from this wallet.")

        # 5. Simulate a gasless transaction.
        destination_address = "0x..." # Replace with a test destination address
        amount_to_send = 5
        simulate_gasless_transaction(created_wallet_id, destination_address, amount_to_send)

        print("\n--- Gasless Experience Setup Simulated Successfully! ---")

    except Exception as e:
        print(f"\n--- An error occurred ---")
        print(e)
