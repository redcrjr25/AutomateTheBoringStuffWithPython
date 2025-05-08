import sys


def fix_blank_lines(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    result = []
    prev_was_blank = False
    for line in lines:
        is_blank = line.strip() == ""
        if is_blank and prev_was_blank:
            continue  # Skip if this is a second consecutive blank line
        result.append(line)
        prev_was_blank = is_blank

    with open(file_path, "w") as f:
        f.writelines(result)


if __name__ == "__main__":
    fix_blank_lines(sys.argv[1])
