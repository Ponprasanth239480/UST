
string1 = """Python is a widely used general-purpose, high level programming language.
It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation.
It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code"""
string1 = string1.lower();  
print("the count of a is ",string1.count('a'))
print("the count of e is ",string1.count('e'))
print("the count of i is ",string1.count('i'))
print("the count of o is ",string1.count('o'))
print("the count of u is ",string1.count('u'))

vowels=0
consonants=0
for i in string1:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u'):
           vowels=vowels+1;
    else:
        consonants=consonants+1;
print("The number of vowels:",vowels);
print("\nThe number of consonant:",consonants);
