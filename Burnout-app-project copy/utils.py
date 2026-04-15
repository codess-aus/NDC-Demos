def print_menu():
    print("\nBurnout Guide App")
    print("1. Add a burnout type")
    print("2. List burnout types")
    print("3. Mark burnout type as reviewed")
    print("4. Remove a burnout type")
    print("5. Exit")


def get_user_choice() -> str:
    return input("Choose an option (1-5): ").strip()


def get_burnout_details():
    title = input("Enter burnout type: ").strip()
    what_it_looks_like = input("Enter what it looks like: ").strip()
    signs_input = input("Enter signs (comma-separated): ").strip()
    healing_steps = input("Enter steps towards healing: ").strip()
    signs = [sign.strip() for sign in signs_input.split(",") if sign.strip()]
    return title, what_it_looks_like, signs, healing_steps


def print_burnout_types(entries):
    if not entries:
        print("No burnout types in your guide.")
        return

    print("\nBurnout Types:")
    for index, entry in enumerate(entries, start=1):
        status = "Reviewed" if entry.reviewed else "New"
        print(f"{index}. {entry.title} - {status}")
        print(f"   Signs: {', '.join(entry.signs)}")