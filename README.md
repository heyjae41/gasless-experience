# Gasless Experience

This project demonstrates how to create a gasless experience for users in Web3 applications, leveraging Circle's Programmable Wallets and Gas Station. This addresses the DoraHacks challenge: "Create a Gasless Experience."

## 1. Project Overview

The primary goal is to remove the friction of gas fees for end-users, making Web3 applications more accessible. This is achieved by having the application (developer) sponsor the gas fees on behalf of the users, who then don't need to hold native blockchain tokens.

## 2. Requirements

*   **Core Functionality:** Enable users to perform on-chain transactions without directly paying gas fees.
*   **Circle Programmable Wallets:** Utilize Smart Contract Accounts (SCAs) for users, which are essential for gasless transactions.
*   **Circle Gas Station:** Integrate with Circle's Gas Station service to sponsor gas fees based on predefined policies.
*   **Python Implementation:** The solution is implemented using Python, interacting with Circle's APIs.

## 3. Source Code Structure

```
gasless-experience/
├── main.py             # Main script for simulating gasless transactions
├── requirements.txt    # Python dependencies (e.g., requests)
└── README.md           # Project documentation
```

*   `main.py`: Contains the core logic for initializing a user, creating a programmable wallet (simulated), and simulating a gasless transaction. It includes placeholders for API keys and user IDs.
*   `requirements.txt`: Lists Python packages required to run the project.

## 4. TODO List & Setup

Before running the `main.py` script, you need to configure the following:

*   **Circle API Key:**
    *   Obtain a Circle API Key from your Circle Developer Account.
    *   Set it as an environment variable: `export CIRCLE_API_KEY="YOUR_ACTUAL_CIRCLE_API_KEY"` or replace `"YOUR_API_KEY_HERE"` in `main.py`.
*   **User ID:**
    *   Define a unique `USER_ID` for the user whose wallet you are managing. This can be any string that uniquely identifies your user within your application.
*   **Simulated User Token:**
    *   The `main.py` script simulates obtaining a `user_token` after user initialization. In a real application, this token is received from your client-side integration after the user completes the PIN/Passkey setup challenge.
*   **Gas Station Configuration (Manual):**
    *   **Crucially**, you need to configure Gas Station policies in the Circle Developer Console. This is a manual step and not done via API in this script.
    *   Ensure policies are set to sponsor gas for transactions originating from your programmable wallets.
*   **Destination Address:**
    *   Replace `"0x..."` in `main.py` with a valid test destination address for the simulated transaction.
*   **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 5. Usage Scenario

This script demonstrates a conceptual flow for providing a gasless experience:

1.  **User Initialization:** A new user is initialized, leading to the creation of a user-controlled programmable wallet (SCA).
2.  **Wallet Creation:** A programmable wallet is created for the user. This wallet is a Smart Contract Account, which is a prerequisite for gasless transactions.
3.  **Gas Station Policy Setup:** The developer configures Gas Station policies in the Circle Developer Console to specify which transactions will have their gas fees sponsored.
4.  **Gasless Transaction:** When the user initiates a transaction from their programmable wallet that matches the configured Gas Station policy, Circle's Gas Station automatically pays the gas fee on behalf of the user. The user experiences a seamless, gas-free transaction.

## 6. Future Enhancements

*   **Full Wallet Creation Flow:** Implement the complete flow for creating user-controlled programmable wallets, including handling the client-side challenge for PIN/Passkey setup.
*   **Real-time Transaction Monitoring:** Track the status of gasless transactions on-chain.
*   **Dynamic Gas Station Policies:** Explore if there are API-driven ways to manage Gas Station policies programmatically.
*   **User Interface:** Develop a user-friendly interface to demonstrate the gasless transaction flow.
*   **Integration with DApps:** Integrate the gasless transaction mechanism into a sample decentralized application.
*   **Comprehensive Testing:** Write unit and integration tests for the gasless transaction logic.