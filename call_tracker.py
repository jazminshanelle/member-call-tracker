import json
print("=== Member Call Tracker ===")


def get_call_data():
    member_id = input("Member ID: ")
    call_type = input("Call type (Claims, Benefits, Eligibility, Pharmacy): ")
    call_minutes = float(input("Call length (minutes): "))
    resolved = input("Was the issue resolved? (yes/no): ")
    call_notes = input("Enter Call Notes: ")

    return member_id, call_type, call_minutes, resolved, call_notes


def generate_summary(call_type, call_notes, resolved):
    return f"""
Member contacted support regarding a {call_type.lower()} issue.
Notes: {call_notes}
Resolution status: {resolved}
"""


def print_summary(member_id, call_type, call_minutes, resolved, call_notes, generated_summary):
    print("\n--- CALL SUMMARY ---")
    print("Member ID:", member_id)
    print("Call Type:", call_type)
    print("Duration:", call_minutes, "minutes")
    print("Resolved:", resolved)
    print("Call Notes:", call_notes)
    print("Generated Summary:", generated_summary)


def save_to_file(call_record):

    try:
        with open("call_log.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(call_record)

    with open("call_log.json", "w") as file:
        json.dump(data, file, indent=4)


def read_call_log():
    print("\n=== PAST CALLS ===")

    try:
        with open("call_log.json", "r") as file:
            data = json.load(file)
            for record in data:
                print(f"Member: {record['member_id']}, Type: {record['call_type']}, Resolved: {record['resolved']}")
    except FileNotFoundError:
        print("No call history found yet.")

def create_call_record(member_id, call_type, call_minutes, resolved, call_notes, generated_summary):

    call_record = {
        "member_id": member_id,
        "call_type": call_type,
        "call_minutes": call_minutes,
        "resolved": resolved,
        "call_notes": call_notes,
        "generated_summary": generated_summary
    }

    return call_record

def view_analytics():
    print("\n=== ANALYTICS DASHBOARD ===")

    try:
        with open("call_log.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No data available yet.")
        return

    total_calls = len(data)

    resolved_calls = 0
    total_minutes = 0

    call_type_counts = {}

    for record in data:
        # resolved stats
        if record["resolved"].lower() == "yes":
            resolved_calls += 1

        # total minutes
        total_minutes += record["call_minutes"]

        # call type count
        ctype = record["call_type"]
        if ctype in call_type_counts:
            call_type_counts[ctype] += 1
        else:
            call_type_counts[ctype] = 1

    unresolved_calls = total_calls - resolved_calls
    avg_duration = total_minutes / total_calls if total_calls > 0 else 0

    most_common_type = max(call_type_counts, key=call_type_counts.get)

    print(f"Total Calls: {total_calls}")
    print(f"Resolved Calls: {resolved_calls}")
    print(f"Unresolved Calls: {unresolved_calls}")
    print(f"Average Call Duration: {avg_duration:.2f} minutes")
    print(f"Most Common Call Type: {most_common_type}")

while True:

    print("\n=== MENU ===")
    print("1. Add new call")
    print("2. View past calls")
    print("3. View analytics")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        member_id, call_type, call_minutes, resolved, call_notes = get_call_data()

        generated_summary = generate_summary(call_type, call_notes, resolved)

        call_record = create_call_record(
            member_id,
            call_type,
            call_minutes,
            resolved,
            call_notes,
            generated_summary
        )

        print(call_record)
        print_summary(member_id, call_type, call_minutes, resolved, call_notes, generated_summary)
        save_to_file(call_record)

    elif choice == "2":
        read_call_log()

    elif choice == "3":
        view_analytics()

    elif choice == "4":
        print("Exiting Member Call Tracker. Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
