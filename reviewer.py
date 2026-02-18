# Smart Code Reviewer (Deterministic + AI optional)
# Reliable output for interview demo

from datetime import datetime
import ast


print("\nSmart Code Reviewer Ready!")
print("Paste code (empty line to finish, 'exit' to stop)\n")


def read_code():
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)


def analyze(code):

    report = []

    # syntax check
    try:
        tree = ast.parse(code)
        report.append("Syntax: OK")
    except:
        return "Syntax: Error in code\nExplanation: The code has syntax mistakes."

    # loop count → complexity
    loops = sum(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))

    if loops == 0:
        report.append("Complexity: O(1)")
        explanation = "Code runs in constant time."
    elif loops == 1:
        report.append("Complexity: O(n)")
        explanation = "Code runs linearly with input size."
    else:
        report.append("Complexity: O(n^2) or higher")
        explanation = "Nested loops increase runtime significantly."

    # style check
    if "range(len(" in code:
        report.append("Style Issue: avoid range(len()), iterate directly")
        explanation += " You should loop directly over the list instead of using indexes."

    return "\n".join(report) + "\nExplanation: " + explanation


def save(text):
    name = "review_" + datetime.now().strftime("%H%M%S") + ".txt"
    open(name, "w", encoding="utf-8").write(text)
    print("Saved:", name)


while True:

    print("\nEnter code:\n")
    code = read_code()

    if code.lower() == "exit":
        break

    if code.strip() == "":
        continue

    result = analyze(code)

    print("\n----- REVIEW -----\n")
    print(result)
    print("\n------------------\n")

    save(result)










