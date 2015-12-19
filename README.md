# dnd_deitySearch
Python code for searching a list of D&amp;D deities.

Commands:

Deity, Alignment, Domain, or Symbol - enter any string to find entries that contain that string in their respective categorry

Advanced - enter strings to each field to find entries that match all your input. If a field is left blank, if won't impact the search.
  ex: Entering "t" in the name field, and "life" for the domain field, while just pressing enter for the for others will return        all entries that have the Life domain, and have a "t" in their name.

Debug - all (lists all entries in file), or domainAll (lists all domains found in file)
Exit - type this just about anywhere to end the program

---
Adding to input file:
Add entries by making a new line in the file, and formatting the entry as NAME: ALIGNMENT: DOMAINS: SYMBOL
If something has multiple domains, separate the domains with anything besides a colon(":") (in the sample file, they are separated with a comma and a space).

---
Potential issues:

*As is, searching for something with a true neutral alignment will return anything with any kind of neutral alignment. This happens because LN (lawful neutral), for example, contains an "N" in it. This can be avoided by changing the input file to represent true neutral some other way (like NN, or TN).

---
I don't know what kind of disclaimers I have to put on this, but I don't own the rights to D&D, people can change this code how they want, etc. 
