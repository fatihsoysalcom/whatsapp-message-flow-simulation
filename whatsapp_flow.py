import time
import random

class User:
    def __init__(self, name):
        self.name = name
        self.messages_received = []

    def send_message(self, recipient, content):
        print(f"\n{self.name} is typing: '{content}' to {recipient.name}")
        # Simulate network latency and processing
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{self.name} sent message.")
        
        # Simulate message being sent to WhatsApp servers
        whatsapp_server.process_message(self, recipient, content)

class WhatsAppServer:
    def process_message(self, sender, recipient, content):
        print("WhatsApp Server: Received message.")
        # Simulate encryption/decryption (simplified)
        encrypted_content = f"[ENCRYPTED:{content}]"
        print("WhatsApp Server: Encrypting message.")
        time.sleep(random.uniform(0.2, 0.8))
        
        # Simulate routing to recipient's device
        print(f"WhatsApp Server: Routing message to {recipient.name}'s device.")
        recipient.receive_message(sender, encrypted_content)

    def receive_message(self, sender, encrypted_content):
        # This method is called by the recipient's device simulation
        pass

class RecipientDevice:
    def receive_message(self, sender, encrypted_content):
        print(f"\n{self.name} (Device): Message received from {sender.name}.")
        # Simulate decryption
        decrypted_content = encrypted_content.replace("[ENCRYPTED:", "").replace("]", "")
        print(f"{self.name} (Device): Decrypting message.")
        time.sleep(random.uniform(0.3, 0.7))
        self.display_message(sender, decrypted_content)

    def display_message(self, sender, content):
        print(f"{self.name} (Device): Displaying message from {sender.name}: '{content}'")
        sender.messages_received.append({'from': sender.name, 'content': content})

# --- Simulation --- 

# Instantiate users and the server
alice = User("Alice")
bob = User("Bob")

# Simulate Bob's device
bob_device = RecipientDevice()
bob_device.name = "Bob's Phone"

# Simulate the WhatsApp server
whatsapp_server = WhatsAppServer()

# Override Bob's receive_message to use the simulated device
bob.receive_message = bob_device.receive_message

# Alice sends a message to Bob
alice.send_message(bob, "Merhaba Bob, nasılsın?")

# Simulate Bob sending a reply
bob.send_message(alice, "İyiyim Alice, sen nasılsın?")

print("\n--- Simulation End ---")
print(f"{alice.name} received: {alice.messages_received}")
