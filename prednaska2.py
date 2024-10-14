import re


# [vycet_znaku] - definice skupin znaku pro danou pozici v textu
# [0-9] - vycet cisel
# [a-z] - pismena anglicke abecedy mala
# [A-Z] - pismena anglicke abecedy velka
# [a-zA-Z] - retezeni
# opakovani vzoru
# - \\d - digits
# - \\w - words
# - \\s - spaces -> mnozina bilych znaku
# - \\D - negace \\d -> vse bez cisel
# / \\W - negace \\w -> vse bez pismen a bez mezery
# logicke vyrazy


#zneprijemneni - inicialy

jmeno = "Tim J. Smith"

#print(bool(re.search("[A-Z][a-z]+(\\s([A-Z]\\.|[A-Z][a-z]+))?\\s[A-Z][a-z]+", jmeno)))


#domaci ukol - overeni emailove adresy

s1 = "jmeno@domena.narod"
s2 = "jmeno.prijmeni@domena.narod"

pattern = "[a-z]+((\\@[a-z]+)|(\\.[a-z]+\\@[a-z]+))\\.[a-z]+"

print(bool(re.search(pattern, s1)))
print(bool(re.search(pattern, s2)))


