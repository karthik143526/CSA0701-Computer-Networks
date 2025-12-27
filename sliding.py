# Simple Sliding Window Simulation (Stop-and-Wait variant)
def sliding_window(sender_frames, window_size):
    n = len(sender_frames)
    base = 0

    while base < n:
        end = min(base + window_size, n)
        print(f"\nSender is sending frames: {sender_frames[base:end]}")

        # Simulate receiver ACK for each frame
        for i in range(base, end):
            ack = input(f"Enter ACK for frame {sender_frames[i]} (Y/N): ").upper()
            if ack == 'Y':
                print(f"Frame {sender_frames[i]} acknowledged")
            else:
                print(f"Frame {sender_frames[i]} lost, will resend")
                break  # Stop and resend from lost frame

        base = i + 1  # Slide window to next set of frames

# ---------------- MAIN ----------------
frames = input("Enter frames to send (comma-separated, e.g., F1,F2,F3,F4): ").split(',')
window_size = int(input("Enter window size: "))

sliding_window(frames, window_size)
