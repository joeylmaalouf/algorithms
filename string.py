# IMPORT -----------------------------------------------------------------------
import sys
# ------------------------------------------------------------------------------


# CLEAN ------------------------------------------------------------------------
def clean(string):
    """ Replaces all punctuation in a string with spaces,
    then trims down any extra spaces in a row.
    """
    translation = string.maketrans(
        "!#$%&()*+,-.:;<=>?@[]^_`{|}~'\\/\"",
        "                                ")
    string = string.translate(translation)
    return " ".join(string.split())
# ------------------------------------------------------------------------------


# UNIT TEST --------------------------------------------------------------------
def main(argv):
    string = "The fox & the c@ jumped over the big + lazy dog! Oh, no."
    print(string)
    print(clean(string))


if __name__ == "__main__":
    main(sys.argv)
# ------------------------------------------------------------------------------
