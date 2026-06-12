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

Updated call tracker with generated summary formatting
