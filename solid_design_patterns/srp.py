
# Single Responsibility Principle
# separation of concerns

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    # break SRP
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass

    def __str__(self) -> str:
        return "\n".join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filepath):
        file = open(filepath, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("first record.")
j.add_entry("second record.")
print(f"Journal entries:\n{j}\n")


p = PersistenceManager()
file = f'/Builder/journal.txt'

p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
