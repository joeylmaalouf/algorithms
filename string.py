# IMPORT -----------------------------------------------------------------------
import sys
# ------------------------------------------------------------------------------


# CLEAN ------------------------------------------------------------------------
def clean(string):
    """ Replaces all punctuation in a string with spaces.
    """
    translation = string.maketrans(
        "!#$%&()*+,-.:;<=>?@[]^_`{|}~'\\/\"",
        "                                ")
    return string.translate(translation)
# ------------------------------------------------------------------------------


# UNIT TEST --------------------------------------------------------------------
def main(argv):
    string = "The fox & the cat jumped over the big, lazy dog! Oh no."
    print(string)
    print(clean(string))


if __name__ == "__main__":
    main(sys.argv)
# ------------------------------------------------------------------------------
