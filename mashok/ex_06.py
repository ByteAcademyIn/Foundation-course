""" to extract a number at the end of a line """
# The given text is X-DSPAM-Confidence: 0.8475

data = 'X-DSPAM-Confidence: 0.8475'

"""" Using find and moving two spaces to account for the colon and space after
colon. Then leaving blank the end so that all numbers are extracted """

Numbers = print(float(data[(data.find(':')) + 2 :]))
