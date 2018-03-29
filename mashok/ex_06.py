""" to extract a number at the end of a line """
# The given text is X-DSPAM-Confidence: 0.8475

data = 'X-DSPAM-Confidence: 0.8475'

""" Using find and moving two spaces to account for the colon and space after
colon. Then leaving blank the 'end' so that all numbers are extracted """
atpos = data.find(':')
print(atpos)
last_text = data[atpos+1: ]
print(last_text)
strip_last_text = last_text.lstrip(' ')
print(strip_last_text)
