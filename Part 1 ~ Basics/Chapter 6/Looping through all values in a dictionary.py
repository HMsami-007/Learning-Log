FavouriteLanguages={
    'Jen':'Python',
    'Sarah':'C++',
    'Alice':'Ruby',
    'Bob':'Java',
    }

for Language in sorted(FavouriteLanguages.values()):
    print(Language)

print("")
print("")

for Language in reversed(sorted(FavouriteLanguages.values())):
    print(Language)

FavouriteLanguages={
    'Jen':'Python',
    'Sarah':'C++',
    'Alice':'Ruby',
    'Bob':'Python',
    }

print("")
print("")
for Language in reversed(sorted(FavouriteLanguages.values())):
    print(Language)


for Language in set(FavouriteLanguages.values()):
    print(Language)