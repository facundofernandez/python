'''Simple million word count program.
    main idea is Python pairs words
    with the number of times
    that number appears in the triple quoted string.
    Credit to William J. Turkel and Adam Crymble for the word
    frequency code used below. I just merged the two ideas.
'''

wordstring = '''SCENE I. Yorkshire. Gaultree Forest.
Enter the ARCHBISHOP OF YORK, MOWBRAY, LORD HASTINGS, and others
ARCHBISHOP OF YORK
What is this forest call'd?
HASTINGS
'Tis Gaultree Forest, an't shall please your grace.
ARCHBISHOP OF YORK
Here stand, my lords; and send discoverers forth
To know the numbers of our enemies.
HASTINGS
We have sent forth already.
ARCHBISHOP OF YORK
'Tis well done.
My friends and brethren in these great affairs,
I must acquaint you that I have received
New-dated letters from Northumberland;
Their cold intent, tenor and substance, thus:
Here doth he wish his person, with such powers
As might hold sortance with his quality,
The which he could not levy; whereupon
He is retired, to ripe his growing fortunes,
To Scotland: and concludes in hearty prayers
That your attempts may overlive the hazard
And fearful melting of their opposite.
MOWBRAY

Exeunt'''

wordlist = wordstring.split()

wordfreq = [wordlist.count(w) for w in wordlist]

print("String\n {} \n".format(wordstring))
print("List\n {} \n".format(str(wordlist)))
print("Frequencies\n {} \n".format(str(wordfreq)))
print("Pairs\n {}".format(str(list(zip(wordlist, wordfreq)))))