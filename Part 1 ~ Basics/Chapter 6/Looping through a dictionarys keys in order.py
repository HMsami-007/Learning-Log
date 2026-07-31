FavouriteLanguages={
    'Jen':'Python',
    'Sarah':'C++',
    'Alice':'Ruby',
    'Bob':'Java',
    }

for name in sorted(FavouriteLanguages.keys()):
    print(name.title())

print(" ")
print(" ")

for name in reversed(sorted(FavouriteLanguages.keys())):
    print(name.title())