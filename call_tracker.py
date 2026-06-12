while True:

    print("=== Member Call Tracker ===")

    member_id = input("Member ID: ")
    call_type = input("Call type (Claims, Benefits, Eligibility, Pharmacy): ")
    call_minutes = float(input("Call length (minutes): "))
    resolved = input("Was the issue resolved? (yes/no): ")
    call_notes = input('Enter Call Notes: ')

    generated_summary = f"""
Member contacted support regarding a {call_type.lower()} issue.
Notes: {call_notes}
Resolution status: {resolved}
"""

    print("\n--- CALL SUMMARY ---")
    print("Member ID:", member_id)
    print("Call Type:", call_type)
    print("Duration:", call_minutes, "minutes")
    print("Resolved:", resolved)
    print("Call Notes:", call_notes)
    print("Generated Summary:", generated_summary)

    with open("call_log.txt", "a") as file:
        file.write("\n--- NEW CALL ---\n")
        file.write(f"Member ID: {member_id}\n")
        file.write(f"Call Type: {call_type}\n")
        file.write(f"Duration: {call_minutes}\n")
        file.write(f"Resolved: {resolved}\n")
        file.write(f"Notes: {call_notes}\n")
        file.write(f"Summary: {generated_summary}\n")

    again = input("\nDo you want to enter another call? (yes/no): ")

    if again.lower() != "yes":
        print("Exiting Member Call Tracker. Goodbye!")
        break
