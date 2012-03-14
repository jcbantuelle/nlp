import re

def replace_whitespace(match):
    return re.sub(r'\s', r'.', match.group())

line = "email: pal at cs stanford edu, but I receive more email than I can handle. Please don't be offended if I don't reply."

# @ symbol
line = re.sub(r'\sat\s', r'@', line)
line = re.sub(r'\(at\)', r'@', line)
line = re.sub(r'\(@\)', r'@', line)
line = re.sub(r'\sWHERE\s', r'@', line)
line = re.sub(r'\s@\s', r'@', line)
line = re.sub(r'&#x40;', r'@', line)

# Strip out
line = re.sub(r'Server@', r'', line)
line = re.sub(r'-', r'', line)
line = re.sub(r'&.*?;', r'', line)

# . symbol
line = re.sub(r'\sdot\s', r'.', line)
line = re.sub(r'\sDOM\s', r'.', line)
line = re.sub(r';', r'.', line)

# obfuscated
line = re.sub(r'\(\'([a-zA-Z][a-zA-Z\.]*[a-zA-Z]\.[a-zA-Z]{2,3})\',\'([a-zA-Z][a-zA-Z\.]*[a-zA-Z])\'\)', r'\(\2@\1\)', line)
line = re.sub(r'([a-zA-Z][a-zA-Z\.]*[a-zA-Z])\s\(followed\sby\s[\"]?(@[a-zA-Z][a-zA-Z\.]*[a-zA-Z]\.[a-zA-Z]{2,3})[\"]?\)', r'\1\2', line)
re.sub(r'([a-zA-Z][a-zA-Z\.]*[a-zA-Z])\s\(followed\sby\s[\"]?(@[a-zA-Z][a-zA-Z\.]*[a-zA-Z]\.[a-zA-Z]{2,3})[\"]?\)', r'\1\2', line)

line = re.sub(r'[a-zA-Z][a-zA-Z\.]*[a-zA-Z]@[a-zA-Z][a-zA-Z\s]*[a-zA-Z]\s[a-zA-Z]{2,3}', replace_whitespace, line)

print line

email_pattern = (r'([a-zA-Z][a-zA-Z\.]*[a-zA-Z])@([a-zA-Z][a-zA-Z\.]*[a-zA-Z])\.([a-zA-Z]{2,3})')

matches = re.findall(email_pattern, line)
for m in matches:
	print m
	