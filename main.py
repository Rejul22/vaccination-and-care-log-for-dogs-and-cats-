import sqlite3
import datetime

db = "pet_care.db"

# database initialize
con = sqlite3.connect(db)
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS pets (pet_id INTEGER PRIMARY KEY AUTOINCREMENT, pet_name TEXT, pet_type TEXT, breed TEXT, age TEXT, owner_name TEXT, medical_history TEXT, last_vaccination TEXT, doctor TEXT, appointment_time TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS medical_logs (log_id INTEGER PRIMARY KEY AUTOINCREMENT, pet_id INTEGER, log_date TEXT, log_type TEXT, details TEXT)")
con.commit()
con.close()

while True:
    print("\n==============================")
    print("   PET CARE MANAGEMENT MENU   ")
    print("==============================")
    print("1. Care & Vaccine Tips")
    print("2. Register New Pet")
    print("3. Search Pet Records")
    print("4. Add Medical Log")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- PET CARE INFORMATION ---")
        print("Dog Tips: Daily walks, regular feeding, dental hygiene.")
        print("Cat Tips: Clean litter box daily, keep fresh water.")
        print("Vaccines: Rabies shots, annual boosters, flea/tick care.")
        input("\nPress enter to go back...")

    elif choice == "2":
        print("\n--- Add New Pet ---")
        name = input("Enter Pet Name: ")
        if name == "":
            print("Error: Name cannot be empty!")
            continue
            
        pet_type = input("Enter Pet Type (Dog/Cat/etc): ")
        breed = input("Enter Breed: ")
        age = input("Enter Age: ")
        owner = input("Enter Owner Name: ")
        if owner == "":
            print("Error: Owner name required!")
            continue
            
        med_history = input("Enter Medical History: ")
        last_vax = input("Enter Last Vaccination Date: ")
        
        print("\nChoose Doctor Slot:")
        print("1. Dr. Rejul (10:00 AM)")
        print("2. Dr. Vaibhav (12:00 PM)")
        print("3. Dr. Animesh (03:00 PM)")
        slot = input("Enter choice (1-3): ")
        
        doc = "None"
        time = "None"
        if slot == "1":
            doc = "Dr. Rejul"
            time = "10:00 AM"
        elif slot == "2":
            doc = "Dr. Vaibhav"
            time = "12:00 PM"
        elif slot == "3":
            doc = "Dr. Animesh"
            time = "03:00 PM"

        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("INSERT INTO pets VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, pet_type, breed, age, owner, med_history, last_vax, doc, time))
        pid = cur.lastrowid
        today = str(datetime.date.today())
        cur.execute("INSERT INTO medical_logs VALUES (NULL, ?, ?, ?, ?)", (pid, today, "Registration", "Registered pet. History: " + med_history))
        conn.commit()
        conn.close()
        
        print("Pet registered successfully! Generated Pet ID:", pid)
        input("Press enter...")

    elif choice == "3":
        query = input("\nEnter Pet Name, Owner Name, or ID: ")
        if query == "":
            print("Nothing entered!")
            continue

        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("SELECT * FROM pets WHERE pet_name LIKE ? OR owner_name LIKE ? OR pet_id = ?", ('%' + query + '%', '%' + query + '%', query))
        results = cur.fetchall()
        
        if len(results) == 0:
            print("No pet records found!")
        else:
            for row in results:
                print("\n--------------------------------")
                print("ID:", row[0], "| Name:", row[1], "| Type:", row[2])
                print("Breed:", row[3], "| Age:", row[4], "| Owner:", row[5])
                print("Medical Notes:", row[6])
                print("Vaccine Date:", row[7])
                print("Appt:", row[8], "at", row[9])
                
                cur.execute("SELECT * FROM medical_logs WHERE pet_id = ?", (row[0],))
                logs = cur.fetchall()
                print("Medical Logs:")
                if len(logs) == 0:
                    print("  No logs found.")
                else:
                    for log in logs:
                        print("  - Date:", log[2], "| Type:", log[3], "| Details:", log[4])
                print("--------------------------------")
        conn.close()
        input("\nPress enter...")

    elif choice == "4":
        pet_id_in = input("\nEnter Pet ID to add log: ")
        if not pet_id_in.isdigit():
            print("Please enter a valid numeric ID!")
            continue

        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("SELECT * FROM pets WHERE pet_id = ?", (pet_id_in,))
        pet = cur.fetchone()
        
        if pet is None:
            print("Pet with this ID does not exist.")
            conn.close()
            continue

        print("Found Pet:", pet[1])
        log_type = input("Enter Log Type (Checkup/Vaccine/Other): ")
        if log_type == "":
            log_type = "General"
            
        details = input("Enter Details: ")
        today = str(datetime.date.today())
        
        cur.execute("INSERT INTO medical_logs VALUES (NULL, ?, ?, ?, ?)", (pet_id_in, today, log_type, details))
        conn.commit()
        conn.close()
        
        print("Log added successfully!")
        input("Press enter...")

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, please try again!")