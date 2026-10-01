"""Day 1: core types and strings"""

# --- Numbers & booleans ---
salary_lpa: float = 18.5
years_exp: int = 4
is_fde_ready: bool = False
print(
    type(salary_lpa), type(years_exp), type(is_fde_ready)
)  # type() prints the type of the var

hike = salary_lpa * 0.30
# f before "String" followed by {} inside "" is string interpolation. Inside {} we can pass the var which contains the value to be printed.
print(f"Target after switch: {salary_lpa + hike} LPA")

# --- Strings are immutable and indexing is EASY ---
role = "Forward Deployed Engineer"
print(role[0])  # 'F'
print(role[-1])  # 'r'
print(role[0:7])  # 'Forward' [start:stop] stop excluded
print(role[::-1])  # reverse string: classic interview one-liner
print(len(role))  # prints the lenght of the string

# --- Essential string methods (you'll use these daily in LLM work) ---
raw = "  GenAI, RAG, LangGraph, MCP  "
clean = (
    raw.strip()
)  # -> 'GenAI, RAG, LangGraph, MCP' removes trailing and leading spaces in a string
skills = clean.split(", ")  # -> creates list of strings
print(skills)
print(" | ".join(skills))  # -> join is called ON the seperator
print(clean.upper(), clean.lower())
print(clean.replace("MCP", "Modal Context Protocol"))
print("RAG" in clean)  # substring check -> True
print(clean.startswith("GenAI"), clean.count(","))

# --- Multi-line strings ---
system_prompt = """You're a suport assistant for a telecom client.
Answer only from the provided contect.
If unsure, say "I don;t know"."""
print(system_prompt)


# --- None and type hints ---
def greet(name: str | None = None) -> str:
    if name is None:
        return "Hello, engineer!"
    return f"Hello {name.title()}"


print(greet())
print(greet("geeta kumari"))

# --- The reference-semantics trap, seen with your own eyes ---
a = [1, 2, 3]
b = a
b.append(4)
print(f"a is {a}  a is b: {a is b}")
c = a.copy()
print(f"a is {a}  a is c: {a is c}")
