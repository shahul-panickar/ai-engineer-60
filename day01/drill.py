def initials(full_name: str) -> str:
    """Return the initials of a full name."""

    return "".join(name[0].upper() for name in full_name.split())

def is_palindrome(text: str) -> bool:
    """Ignore space and case."""
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

def mask_email(email: str) -> str:
    """keep first character of the username and the domain."""
    username, domain = email.split("@")
    masked_username = username[0] + "*" * (len(username)-1)
    return f"{masked_username}@{domain}"

assert initials("John Doe") == "JD"
assert is_palindrome("  Never Odd or Even ") is True
assert is_palindrome("Hello") is False
assert mask_email("john.doe@example.com") == "j*******@example.com"
print("All tests passed!")