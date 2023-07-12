# create_wordlist.py
# run in shell: ex:  python create_wordlist.py wyrdl.py wordlist.txt
# creates general wordlist from file, doesn't limit word lenth
import pathlib
import sys
from string import ascii_letters

#existing file path to convert to wordlist
in_path = pathlib.Path(sys.argv[1])

#filepath of outputed wordlist (overwrites file if already exists at path)
out_path = pathlib.Path(sys.argv[2])

# only allows letters A-Z (can be to limiting outside of english wordle)
# sorts words by length (smallest to longest and then alphabetically within length)
words = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding="utf-8").split()
        if all(letter in ascii_letters for letter in word)
    },
    key=lambda word: (len(word), word),
)
out_path.write_text("\n".join(words))