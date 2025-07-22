import time

def countdown(seconds: int):
    """
    Countdown from the given number of seconds.

    Args:
        seconds (int): The number of seconds to count down from.
    """
    if seconds < 0:
        raise ValueError("Seconds must be a non-negative integer.")

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Time remaining: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up!")

if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter countdown time in seconds: "))
        countdown(total_seconds)
    except ValueError:
        print("Please enter a valid non-negative integer.")
