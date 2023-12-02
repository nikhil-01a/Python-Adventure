import json
import sys


class AdventureGame:
    def __init__(self, map_file):
        self.map = self.load_map(map_file)
        if self.map is None:
            raise ValueError("Invalid map file.")
        self.current_room = 0
        self.inventory = []

    def load_map(self, map_file):
        try:
            with open(map_file, 'r') as file:
                game_map = json.load(file)
            # Validation part
            if not self.validate_map(game_map):
                print("Map validation failed.")
                return None
            return game_map
        except json.JSONDecodeError:
            print("Error reading map file. Please ensure it's valid JSON.")
            return None

    def validate_map(self, game_map):
        if not isinstance(game_map, list):
            return False

        for room_id, room in enumerate(game_map):
            # Check for name, desc, and exits in each room
            if not all(key in room for key in ["name", "desc", "exits"]):
                return False

            # Check if exits are valid
            for exit_direction, exit_room_id in room["exits"].items():
                if not isinstance(exit_room_id, int) or exit_room_id < 0 or exit_room_id >= len(game_map):
                    return False

        return True

    def start(self):
        self.show_current_room()
        while True:
            try:
                command = input("What would you like to do? ").strip().lower()
            except EOFError:
                print("\nUse 'quit' to exit.")
                continue
            if command == "quit":
                print("Goodbye!")
                break
            else:
                self.process_command(command)

    def show_current_room(self):
        room = self.map[self.current_room]
        print(f"> {room['name']}\n")
        print(room['desc'])
        if 'items' in room and room['items']:
            print("\nItems:", ", ".join(room['items']))
        print("\nExits:", " ".join(room['exits'].keys()), "\n")

    def process_command(self, command):
        command_parts = command.split()
        if not command_parts:
            print("Print enter a command.")
            return

        action = command_parts[0]
        args = command_parts[1:]

        if self.is_command(action, "go") and args:
            self.process_direction(args)
        elif self.is_command(action, "get") and args:
            self.process_item(args)
        elif self.is_command(action, "inventory"):
            self.show_inventory()
        elif self.is_command(action, "look"):
            self.show_current_room()
        else:
            print("I don't understand that command.")

    def is_command(self, action, command):
        return command.startswith(action)

    def process_direction(self, args):
        if not args:
            print("Sorry, you need to 'go' somewhere.")
            return

        direction = args[0]
        current_exits = self.map[self.current_room]['exits']
        matching_exits = [
            exit for exit in current_exits if exit.startswith(direction)]

        if len(matching_exits) == 1:
            self.go(matching_exits[0])
        elif len(matching_exits) > 1:
            if direction in matching_exits:
                # Direct match, no ambiguity
                self.go(direction)
            else:
                # Ambiguity exists, ask for clarification
                print(f"Did you want to go {' or '.join(matching_exits)}?")
        else:
            print(f"There's no way to go {' '.join(args)}.")

    def find_matching_exits(self, partial):
        current_exits = self.map[self.current_room]['exits']
        return [exit for exit in current_exits if exit.startswith(partial)]

    def process_item(self, args):
        if not args:
            print("Sorry, you need to 'get' something.")
            return
        room = self.map[self.current_room]
        if 'items' in room:
            matching_items = self.find_matching_items(
                ' '.join(args), room['items'])
            if len(matching_items) == 1:
                self.get(matching_items[0])
            elif len(matching_items) > 1:
                print(f"Did you want to get {' or '.join(matching_items)}?")
            else:
                print(f"There's no {' '.join(args)} anywhere.")
        else:
            print("There are no items to get here.")

    def find_matching_items(self, partial, items):
        return [item for item in items if partial in item]

    def go(self, direction):
        current_exits = self.map[self.current_room]['exits']
        if direction in current_exits:
            self.current_room = current_exits[direction]
            print(f"You go {direction}.\n")
            self.show_current_room()
        else:
            print(f"There's no way to go {direction}.")

    def get(self, item):
        room = self.map[self.current_room]
        if 'items' in room and item in room['items']:
            self.inventory.append(item)
            room['items'].remove(item)
            print(f"You pick up the {item}.")
        else:
            print(f"There's no {item} anywhere.")

    def show_inventory(self):
        if self.inventory:
            print("Inventory:")
            for item in reversed(self.inventory):
                print(f"  {item}")
        else:
            print("You're not carrying anything.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        return

    game = AdventureGame(sys.argv[1])
    game.start()


if __name__ == "__main__":
    main()
