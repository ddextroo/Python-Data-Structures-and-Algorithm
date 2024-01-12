filename = "singly.py"
line_number = 40

with open(filename, 'r') as file:
    lines = file.readlines()

# Check if the line has been modified
if len(lines) >= line_number:
    original_line = lines[line_number - 1].strip()

    # Iterate over the file's content to find the first modification
    for i, commit_line in enumerate(lines):
        if commit_line.strip() != original_line:
            print(f"The first modification of line {line_number} in {filename} occurred at line {i + 1}")
            break
else:
    print(f"The file {filename} does not have {line_number} lines.")
