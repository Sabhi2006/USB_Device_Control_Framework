import tkinter as tk
from tkinter import ttk
from pathlib import Path
from collections import Counter


LOG_FILE = Path(__file__).parent / "logs" / "usb_activity.log"


def load_events():
    if not LOG_FILE.exists():
        return []

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def refresh_dashboard():
    events = load_events()

    connected = sum("USB_CONNECTED" in e for e in events)
    disconnected = sum("USB_DISCONNECTED" in e for e in events)
    created = sum("FILE_CREATED" in e for e in events)
    modified = sum("FILE_MODIFIED" in e for e in events)
    deleted = sum("FILE_DELETED" in e for e in events)
    violations = sum("FILE_INTEGRITY_MODIFIED" in e for e in events)

    stats = {
        "USB Connected": connected,
        "USB Disconnected": disconnected,
        "Files Created": created,
        "Files Modified": modified,
        "Files Deleted": deleted,
        "Integrity Violations": violations,
    }

    for widget in stats_frame.winfo_children():
        widget.destroy()

    for i, (name, value) in enumerate(stats.items()):
        card = ttk.Frame(stats_frame, padding=15, relief="ridge")
        card.grid(row=0, column=i, padx=5, pady=10)

        ttk.Label(card, text=name).pack()
        ttk.Label(
            card,
            text=str(value),
            font=("Arial", 20, "bold")
        ).pack()

    event_list.delete(0, tk.END)

    for event in events[-15:]:
        event_list.insert(tk.END, event)

    status_label.config(
        text=f"Total events: {len(events)}"
    )


root = tk.Tk()
root.title("USB Device Control Framework - Security Dashboard")
root.geometry("1100x500")

ttk.Label(
    root,
    text="USB SECURITY DASHBOARD",
    font=("Arial", 18, "bold")
).pack(pady=15)

stats_frame = ttk.Frame(root)
stats_frame.pack()

event_list = tk.Listbox(root, width=140, height=15)
event_list.pack(padx=20, pady=10)

ttk.Button(
    root,
    text="Refresh Dashboard",
    command=refresh_dashboard
).pack(pady=5)

status_label = ttk.Label(root, text="")
status_label.pack()

refresh_dashboard()
root.mainloop()