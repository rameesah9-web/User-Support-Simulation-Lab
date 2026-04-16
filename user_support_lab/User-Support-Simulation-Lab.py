# User Support Simulation Lab - Simple but Detailed Version
# Real feel of first-line IT support
# Built by [Your Name] 2026

tickets = [
    {
        "id": 1,
        "user": "Adam",
        "device": "Company Windows Laptop",
        "issue": "Internet keeps disconnecting every 10 minutes",
        "symptoms": "WiFi shows connected but no internet. Started after moving desk.",
        "status": "Open",
        "steps": [],
        "resolution": ""
    },
    {
        "id": 2,
        "user": "James",
        "device": "Home Windows 11 PC",
        "issue": "Forgot Windows login password",
        "symptoms": "Password not accepted after recent update.",
        "status": "Open",
        "steps": [],
        "resolution": ""
    },
    {
        "id": 3,
        "user": "Aria",
        "device": "Work MacBook Air",
        "issue": "Laptop very slow after new software install",
        "symptoms": "Apps take forever to open, high CPU usage.",
        "status": "Open",
        "steps": [],
        "resolution": ""
    }
]

print("=== USER SUPPORT SIMULATION LAB ===")
print("You are the IT Support Technician 🛠️\n")

while True:
    print("\nMenu:")
    print("1. View all tickets")
    print("2. Work on a ticket (troubleshoot)")
    print("3. Create new ticket")
    print("4. Generate Support Log Report")
    print("5. Exit")
    
    choice = input("\nChoose 1-5: ")
    
    if choice == "1":
        print("\n--- ALL TICKETS ---")
        for t in tickets:
            print(f"\nTicket #{t['id']} - {t['user']} ({t['device']})")
            print(f"Issue: {t['issue']}")
            print(f"Symptoms: {t['symptoms']}")
            print(f"Status: {t['status']}")
            if t['steps']:
                print("Steps taken:")
                for s in t['steps']:
                    print(f"  • {s}")
            if t['resolution']:
                print(f"Resolution: {t['resolution']}")
        print("--------------------")
    
    elif choice == "2":
        try:
            num = int(input("\nEnter ticket number to fix (1-3): "))
            for t in tickets:
                if t["id"] == num and t["status"] == "Open":
                    print(f"\nHelping {t['user']} with: {t['issue']}")
                    print(f"Device: {t['device']}")
                    print(f"Details: {t['symptoms']}\n")
                    
                    print("Choose troubleshooting step:")
                    print("1. Restart device")
                    print("2. Check WiFi / internet connection")
                    print("3. Clear temporary files")
                    print("4. Reset password")
                    print("5. Check for software conflict")
                    
                    step = input("Choose 1-5: ")
                    
                    step_text = {
                        "1": "Asked user to restart their device completely",
                        "2": "Guided user to check and reconnect to WiFi",
                        "3": "Instructed user to clear temporary files and cache",
                        "4": "Helped user reset their Windows/Mac password",
                        "5": "Checked Task Manager / Activity Monitor for software issues"
                    }
                    
                    chosen_step = step_text.get(step, "Performed basic checks")
                    t["steps"].append(chosen_step)
                    
                    # Auto feedback from "user"
                    user_feedback = {
                        "1": "User: Restart worked! Internet is stable now.",
                        "2": "User: WiFi reconnected successfully.",
                        "3": "User: Laptop feels much faster now.",
                        "4": "User: Password reset successful, I can log in.",
                        "5": "User: CPU usage is back to normal, apps open quickly."
                    }
                    print(user_feedback.get(step, "User: The problem is now fixed. Thank you!"))
                    
                    # Auto resolution
                    t["resolution"] = "Issue resolved after following troubleshooting steps."
                    t["status"] = "Resolved"
                    print("✅ Ticket resolved and documented!\n")
                    break
            else:
                print("Ticket not found or already resolved.")
        except:
            print("Please type a number.")
    
    elif choice == "3":
        name = input("User name: ")
        device = input("Device: ")
        issue = input("Issue: ")
        symptoms = input("Symptoms: ")
        tickets.append({
            "id": len(tickets) + 1,
            "user": name,
            "device": device,
            "issue": issue,
            "symptoms": symptoms,
            "status": "Open",
            "steps": [],
            "resolution": ""
        })
        print("✅ New ticket created!\n")
    
    elif choice == "4":
        filename = "My_Support_Log.txt"
        with open(filename, "w") as f:
            f.write("IT SUPPORT SIMULATION LAB - SUPPORT LOG\n")
            f.write("Technician: [Your Name]\n")
            f.write("Date: April 2026\n\n")
            for t in tickets:
                f.write(f"Ticket #{t['id']} - {t['user']}\n")
                f.write(f"Device: {t['device']}\n")
                f.write(f"Issue: {t['issue']}\n")
                f.write(f"Symptoms: {t['symptoms']}\n")
                f.write(f"Status: {t['status']}\n")
                if t['steps']:
                    f.write("Steps Taken:\n")
                    for s in t['steps']:
                        f.write(f"- {s}\n")
                if t['resolution']:
                    f.write(f"Resolution: {t['resolution']}\n")
                f.write("\n")
        print(f"✅ Support Log saved as {filename}")
        print("Open this file to see your full work!")
    
    elif choice == "5":
        print("Thanks for practising! This shows real support skills 💪")
        break
    
    else:
        print("Please choose 1-5 only.")