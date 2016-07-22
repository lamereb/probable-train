#!/usr/bin/python
import string

manip = "helloworlds!?."
puncts = "?!.".ljust(256)
# print string.translate(manip, ['!','?','.'])

print string.translate(manip, puncts)

