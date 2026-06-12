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


def save_to_file(member_id, call_type, call_minutes, resolved, call_notes, generated_summary):
    with open("call_log.txt", "a") as file:
        file.write("\n--- NEW CALL ---\n")
        file.write(f"Member ID: {member_id}\n")
        file.write(f"Call Type: {call_type}\n")
        file.write(f"Duration: {call_minutes}\n")
        file.write(f"Resolved: {resolved}\n")
        file.write(f"Notes: {call_notes}\n")
        file.write(f"Summary: {generated_summary}\n")

def read_call_log():
    print("\n=== PAST CALLS ===")

    try:
        with open("call_log.txt", "r") as file:
            content = file.read()
            print(content)
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

while True:

    print("\n=== MENU ===")
    print("1. Add new call")
    print("2. View past calls")
    print("3. Exit")

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
        python(call_record)

        print_summary(member_id, call_type, call_minutes, resolved, call_notes, generated_summary)

        save_to_file(member_id, call_type, call_minutes, resolved, call_notes, generated_summary)

    elif choice == "2":
        read_call_log()

    elif choice == "3":
        print("Exiting Member Call Tracker. Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
