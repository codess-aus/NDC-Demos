import sys
from burnout_types import BurnoutCollection


collection = BurnoutCollection()


def show_burnout_types(entries):
    """Display burnout types in a user-friendly format."""
    if not entries:
        print("No burnout types found.")
        return

    print("\nBurnout Guide:\n")

    for index, entry in enumerate(entries, start=1):
        status = "x" if entry.reviewed else " "
        print(f"{index}. [{status}] {entry.title}")
        print(f"   What it looks like: {entry.what_it_looks_like}")
        print(f"   Signs: {', '.join(entry.signs)}")
        print(f"   Steps towards healing: {entry.healing_steps}")
        print()


def handle_list():
    entries = collection.list_burnout_types()
    show_burnout_types(entries)


def handle_add():
    print("\nAdd a Burnout Type\n")

    title = input("Type name: ").strip()
    what_it_looks_like = input("What it looks like: ").strip()
    signs_input = input("Signs (comma-separated): ").strip()
    healing_steps = input("Steps towards healing: ").strip()

    signs = [sign.strip() for sign in signs_input.split(",") if sign.strip()]

    try:
        collection.add_burnout_type(title, what_it_looks_like, signs, healing_steps)
        print("\nBurnout type added successfully.\n")
    except ValueError as error:
        print(f"\nError: {error}\n")


def handle_remove():
    print("\nRemove a Burnout Type\n")

    title = input("Enter the burnout type to remove: ").strip()
    removed = collection.remove_burnout_type(title)

    if removed:
        print("\nBurnout type removed.\n")
    else:
        print("\nNo burnout type matched that name.\n")


def handle_find():
    print("\nFind Burnout Types by Healing Keyword\n")

    keyword = input("Healing keyword: ").strip()
    entries = collection.find_by_healing_keyword(keyword)

    show_burnout_types(entries)


def show_help():
    print(
        """
Burnout Guide Helper

Commands:
  list     - Show all burnout types
  add      - Add a new burnout type
  remove   - Remove a burnout type by name
  find     - Find burnout types by healing keyword
  help     - Show this help message
"""
    )


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "list":
        handle_list()
    elif command == "add":
        handle_add()
    elif command == "remove":
        handle_remove()
    elif command == "find":
        handle_find()
    elif command == "help":
        show_help()
    else:
        print("Unknown command.\n")
        show_help()


if __name__ == "__main__":
    main()