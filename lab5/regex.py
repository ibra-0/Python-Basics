import re

# 1. 
def match_a_b(s):
    return bool(re.fullmatch(r'a*b*', s))
print(match_a_b("abbb"))
# 2. 
def match_a_bb(s):
    return bool(re.fullmatch(r'a(bb|bbb)', s))
print(match_a_bb("abbdk"))
# 3. 
def find_lowercase_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

# 4. 
def find_upper_followed_by_lower(s):
    return re.findall(r'[A-Z][a-z]+', s)

# 5. 
def match_a_any_b(s):
    return bool(re.fullmatch(r'a.*b', s))

# 6. 
def replace_space_comma_dot(s):
    return re.sub(r'[ ,.]+', ':', s)

# 7. 
def snake_to_camel(s):
    return ''.join(word.capitalize() for word in s.split('_'))

# 8.
def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

# 9. 
def insert_spaces_in_camel(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

# 10. 
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
