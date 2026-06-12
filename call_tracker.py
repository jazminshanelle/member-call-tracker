print("=== Member Call Tracker ===")

member_id = input("Member ID: ")
call_type = input("Call type (Claims, Benefits, Eligibility, Pharmacy): ")
call_minutes = float(input("Call length (minutes): "))
resolved = input("Was the issue resolved? (yes/no): ")

print("\n--- CALL SUMMARY ---")
print("Member ID:", member_id)
print("Call Type:", call_type)
print("Duration:", call_minutes, "minutes")
print("Resolved:", resolved)
