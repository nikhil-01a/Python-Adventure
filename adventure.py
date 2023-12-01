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
        print(f"\n> {room['name']}\n")
        print(room['desc'])
        if 'items' in room:
            print("\nItems:", ", ".join(room['items']))
        print("\nExits:", " ".join(room['exits'].keys()))

    def process_command(self, command):
        if command.startswith("go "):
            self.go(command[3:])
            self.show_current_room()
        elif command == "go":
            print("Sorry, you need to 'go' somewhere.")
        elif command == "get":
            print("Sorry, you need to 'get' something.")
        elif command == "look":
            self.show_current_room()
        elif command.startswith("get "):
            self.get(command[4:])
        elif command == "inventory":
            self.show_inventory()
        else:
            print("I don't understand that command.")

    def go(self, direction):
        current_exits = self.map[self.current_room]['exits']
        if direction in current_exits:
            self.current_room = current_exits[direction]
            print(f"You go {direction}.")
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
            print("You are carrying:", ", ".join(self.inventory))
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
