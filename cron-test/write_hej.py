from pathlib import Path
from datetime import datetime

file_path = Path("/data/test.txt")

with file_path.open("a", encoding="utf-8") as file:
    file.write("hej\n")

print(f"{datetime.now().isoformat()} - skrev 'hej' til {file_path}")

print("\nFilens nuværende indhold:")
print(file_path.read_text(encoding="utf-8"))