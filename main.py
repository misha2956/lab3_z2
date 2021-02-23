"""
This module realises an intereface for navigating json
"""
import sys
import json
from copy import deepcopy

def perform_navigation(json_obj: dict, path_toapply: list):
    """
    This function performs the json object navigation
    """

    json_obj_new = deepcopy(json_obj)
    for key in path_toapply:
        json_obj_new = json_obj_new[key]

    return json_obj_new


def navigate(json_obj: dict):
    """
    This function navigates a json file
    """
    path_toapply = []
    json_obj_cur = perform_navigation(json_obj, path_toapply)
    while True:
        print()
        if isinstance(json_obj_cur, dict):
            print("Current object is a dictionary.")
            print(f"The keys are: {list(json_obj_cur.keys())}")
            prompt = "none of those"
            while prompt not in json_obj_cur:
                prompt = input("Please, choose a key (copy it here): ")
            path_toapply.append(prompt)
        elif isinstance(json_obj_cur, list):
            print(f"Current object is a list of {len(json_obj_cur)} elements.")
            prompt = 'q'
            while not prompt.isnumeric():
                prompt = input("Pick element number: ")
            path_toapply.append(int(prompt))
        else:
            print(
                f"Current object is:\n{json_obj_cur}"
            )
            prompt = input("Type 'b' if you want to go back or 'q' to quit: ")
            if prompt == 'b':
                if len(path_toapply) > 0:
                    path_toapply.pop()
                else:
                    print("Already at the upmost level!")
            elif prompt == 'q':
                break

        json_obj_cur = perform_navigation(json_obj, path_toapply)


def main():
    """
    An intereactive function of the module
    """

    if len(sys.argv) <= 1:
        json_path = input(
            "Please enter name of the json file you want to explore: "
        )
        print("NOTE: You may also pass filename as an argument")
    else:
        json_path = sys.argv[1]
    with open(json_path, "r") as file_in:
        json_obj: dict = json.load(file_in)

    navigate(json_obj)


if __name__ == "__main__":
    main()
