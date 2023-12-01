import json
import sys


class AdventureGame:
    def __init__(self, map_file):
        with open(map_file, 'r') as file:
            self.map = json.load(file)
        self.current_room = 0
        self.inventory = []

    def start(self):
        while True:
            self.show_current_room()
            command = input("What would you like to do? ").strip().lower()
            if command == "quit":
                print("Goodbye!")
                break
            else:
                self.process_command(command)

    def show_current_room(self):
        room = self.map[self.current_room]
        print(f"\n> {room['name']}\n")
        print(room['desc'])
        print("\nExits:", " ".join(room['exits'].keys()))
        if 'items' in room:
            print("\nItems in the room:", ", ".join(room['items']))

    def process_command(self, command):
        if command.startswith("go "):
            self.go(command[3:])
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
            print(f"There's no {item} to get.")

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
