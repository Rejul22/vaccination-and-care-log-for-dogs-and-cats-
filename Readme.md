# Pet Care Management System

## Introduction

As a dog owner, I know how easy it can be to forget when a pet needs a vaccine. My two-year-old dog, Sultan, inspired me to make this project. I hope it can help pet owners and veterinary clinics keep pet records and medical logs in one place, so they can remember appointments and provide pets with timely care and medication.

This beginner Python program can register pets, save appointment choices, search records, add medical notes, and show basic pet-care tips.

## Requirements

- Python 3
- No extra packages are needed.

## Run the program

Follow these steps to start the program:

1. **Install Python 3.** If it is not already installed, download it from [python.org](https://www.python.org/downloads/). On Windows, select **Add Python to PATH** during setup if that option appears.
2. **Save the program.** Copy the program code into a text editor and save the file as `pet_care.py`. Make a note of the folder where you saved it. Check that the filename is not `pet_care.py.txt`.
3. **Open a command window.** On Windows, open Command Prompt or PowerShell. On macOS, open Terminal. On Linux, open Terminal.
4. **Go to the folder containing the program.** In the command window, type `cd ` followed by the folder's location, then press Enter. For example:

   ```bash
   cd Desktop/pet-care-project
   ```

   On Windows, an example is:

   ```bat
   cd %USERPROFILE%\Desktop\pet-care-project
   ```

   Replace the example folder with the one where you saved `pet_care.py`.
5. **Start the program.** Type this command and press Enter:

   ```bash
   python pet_care.py
   ```

   If your computer does not recognize `python`, try `python3 pet_care.py` (often used on macOS/Linux) or `py pet_care.py` (often used on Windows).
6. **Use the menu.** When the menu appears, type the number for the action you want and press Enter. Follow the questions shown on screen. Type `5` and press Enter when you want to close the program.

The first time it runs, the program creates `pet_care.db` in the same folder. Keep that file because it holds the saved pet records and medical logs.

## Menu options

- `1` — View pet-care and vaccine tips.
- `2` — Register a pet and choose an appointment slot.
- `3` — Search by pet name, owner name, or pet ID.
- `4` — Add a dated medical log using the pet ID.
- `5` — Exit.

## Example: add a pet and appointment

Choose `2`, then enter details when prompted. For example:

```text
Enter your choice (1-5): 2
Enter Pet Name: Bruno
Enter Pet Type (Dog/Cat/etc): Dog
Enter Breed: Labrador
Enter Age: 3
Enter Owner Name: Asha
Enter Medical History: No known health problems
Enter Last Vaccination Date: 2026-06-10
Enter choice (1-3): 2
Pet registered successfully! Generated Pet ID: 1
```

For the appointment, choice `2` means **Dr. Patel at 12:00 PM**. The program prints the pet's ID; use it to add medical logs. To check the saved appointment, choose `3` and search for Bruno or the ID.

## Saved data

The program creates `pet_care.db` in the folder where it is run. It stores pet details and medical logs, so keep this file to keep your records. The appointment is saved when registering a pet; the program does not let you change it later.

## Troubleshooting

### The `python` command is not recognized

Python may not be installed, or your computer may use a different command. Install Python 3 from [python.org](https://www.python.org/downloads/) and reopen the command window. Then try `python3 pet_care.py` or, on Windows, `py pet_care.py`.

### The program says it cannot find `pet_care.py`

The command window may be open in the wrong folder. Go to the folder where you saved the file using `cd`, then run the program again. Check the filename too: it should be `pet_care.py`, not `pet_care.py.txt`.

### The program opens and closes quickly

Start it from Command Prompt, PowerShell, or Terminal by typing the run command there. This keeps the window open so you can read any error message. If an error appears, check that the code was copied completely into `pet_care.py`.

### A menu choice does not work

Enter one of the listed numbers and press Enter. For example, type `2` to register a pet. If you enter a letter or a number that is not shown, the program will ask you to try again.

### I cannot find a pet record

Search with the pet's name, the owner's name, or the pet ID printed after registration. You can search with part of a name. Check the spelling and make sure the pet was registered successfully.

### My saved records are missing

The database file is named `pet_care.db`. The program creates it in the folder it is run from. Make sure you are running the program in the same folder as the database containing your records. Avoid deleting or moving that database file; if it is deleted, the saved records are lost.

### I entered the wrong appointment choice

During registration, choose `1`, `2`, or `3` for one of the displayed doctor slots. The current program does not have an option to edit an appointment after the pet is registered, so check the choice before entering it.


## About the Author

**Name:** Rejul Kumar Naharwara

I am a dog owner and beginner programmer. I created this project based on my experience caring for Sultan and my interest in making it easier to keep track of pets’ health needs.

## Conclusion

This project is a simple way to practise Python while helping organize pet information. I hope it encourages pet owners and veterinary clinics to keep useful records and provide pets with care on time.
# vaccination-and-care-log-for-dogs-and-cats-
# vaccination-and-care-log-for-dogs-and-cats-
