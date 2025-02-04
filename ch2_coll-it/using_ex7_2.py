# Write Python code to replace all the : characters in the string below with +.
# str.replace(old, new, count=-1)

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

new_info = info.replace(':', '+')

print(info)
print(new_info)