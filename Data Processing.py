import csv

csv_path = "C:\\Users\\MOHAMED SHAFAR\\Documents\\old_data.csv"


# -------------------------------
# 📄 DISPLAY FUNCTION
# -------------------------------
def show_data(data):
    print("\n📄 Current Data:\n")

    if not data:
        print("No data available\n")
        return

    headers = data[0].keys()
    print(" | ".join(headers))
    print("-" * 60)

    for row in data:
        print(" | ".join(row.values()))
    print()


# -------------------------------
# 🔁 MAIN LOOP
# -------------------------------
while True:

    # Load CSV
    with open(csv_path, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Show current data
    show_data(data)

    # Menu
    print("Choose operation:")
    print("1. Update value")
    print("2. Delete row")
    print("3. Remove column")
    print("4. Add new row")
    print("5. Exit")

    choice = input("Enter choice: ")

    # -------------------------------
    # ✏️ UPDATE
    # -------------------------------
    if choice == "1":
        target_id = input("Enter ID to update: ")
        column = input("Enter column name: ")
        new_value = input("Enter new value: ")

        found = False

        for row in data:
            if row["id"] == target_id:
                if column in row:
                    row[column] = new_value
                    found = True

        if found:
            print("✅ Value updated")
        else:
            print("❌ ID or column not found")

    # -------------------------------
    # ❌ DELETE ROW
    # -------------------------------
    elif choice == "2":
        target_id = input("Enter ID to delete: ")

        new_data = [row for row in data if row["id"] != target_id]

        if len(new_data) != len(data):
            data = new_data
            print("✅ Row deleted")
        else:
            print("❌ ID not found")

    # -------------------------------
    # 🧹 REMOVE COLUMN
    # -------------------------------
    elif choice == "3":
        column = input("Enter column to remove: ")

        if column == "id":
            print("❌ Cannot remove ID column")
        else:
            for row in data:
                row.pop(column, None)
            print("✅ Column removed")

    # -------------------------------
    # ➕ ADD NEW ROW
    # -------------------------------
    elif choice == "4":
        if not data:
            print("❌ No structure available to add row")
            continue

        new_row = {}

        print("Enter values for new row:")

        for field in data[0].keys():
            value = input(f"{field}: ")
            new_row[field] = value

        data.append(new_row)
        print("✅ New row added")

    # -------------------------------
    # 🚪 EXIT
    # -------------------------------
    elif choice == "5":
        print("👋 Exiting program...")
        break

    else:
        print("❌ Invalid choice")
        continue

    # -------------------------------
    # 💾 SAVE BACK TO CSV
    # -------------------------------
    if data:
        fieldnames = data[0].keys()

        with open(csv_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print("💾 Changes saved\n")