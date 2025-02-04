# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info_split = info.split(':')

print(info_split)

info_rejoined = '+'.join(info_split)
# info_rejoined = info_split.join('+')

print(info_rejoined)