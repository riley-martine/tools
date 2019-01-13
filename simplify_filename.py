#!/usr/bin/python3
import os
import sys

if len(sys.argv) < 2:
    print("Usage: <program.py> filename1...")
    sys.exit()


def change_names(mock: bool) -> None:
    for filename in sys.argv[1:]:

        new_filename = filename
        new_filename = (
            (
                "".join(
                    ch
                    for ch in new_filename.replace(" ", "_")
                    if ch.isalnum() or ch in "._"
                )
            )
            .lower()
            .replace("__", "_")
        )

        if mock:
            print(filename)
            print(new_filename)
        else:
            os.rename(filename, new_filename)


if __name__ == "__main__":
    change_names(mock=True)
    if input("Change filenames? (Y/n): ") != "n":
        change_names(mock=False)
