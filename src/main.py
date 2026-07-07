from parser import parse_input
from matching import match_residents
from stability import check_matching, print_report
import sys

    # Pseudocode for the modified Gale-Shapley Stable Matching algorithm function:
    # Input: hospitals, residents
    # Initialization:
    #   all residents in residents are unmatched
    #   for each resident r in residents:
    #     r has the first hospital in their preference list as their next choice
    #   for each hospital h in hospitals:
    #     h has no matched residents
    # Loop:
    #   while there are unmatched residents:
    #     get the next unmatched resident r from the top of residents
    #
    #     if r has no hospitals left to try:
    #       continue to the next resident
    #     
    #     get the next hospital h from r's preference list
    #     if r is not in h's rank list:
    #       continue to the next resident
    #
    #     add r to h's matched residents
    #     if h has more matched residents than its slots:
    #       find the worst resident w in h's matched residents
    #       remove w from h's matched residents
    #       if w has more hospitals left to try:
    #         add w back to the list of unmatched residents
    # Return: matches, a dictionary mapping each hospital to its matched residents

def main():
    print("CS4306 Assignment 1")
    print("Paste input, then press Ctrl+Z then Enter on Windows:")

    text = sys.stdin.read()
    text = text.replace("\x1a", "").strip()

    hospitals, residents = parse_input(text)
    matches = match_residents(hospitals, residents)

    print("\nMatching:")
    for hospital, assigned_residents in matches.items():
        print(hospital + ", " + ", ".join(assigned_residents))
    
    report = check_matching(hospitals, residents, matches)
    print()
    print_report(report)


if __name__ == "__main__":
    main()