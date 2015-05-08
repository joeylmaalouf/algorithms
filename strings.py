# IMPORT -----------------------------------------------------------------------
import string
import sys
# ------------------------------------------------------------------------------


# CLEAN ------------------------------------------------------------------------
def clean(s):
    """ Replaces all punctuation in a string with spaces,
        then trims down any extra spaces in a row.
    """
    translation = string.maketrans(
        "!#$%&()*+,-.:;<=>?@[]^_`{|}~'\\/\"",
        "                                ")
    s = string.translate(s, translation)
    return " ".join(s.split())
# ------------------------------------------------------------------------------


# BASE CHARS--------------------------------------------------------------------
def base_chars(base):
    """ Returns the usable characters for a given base.
    """
    return list(string.digits+string.ascii_uppercase)[:base]
# ------------------------------------------------------------------------------


# UNIT TEST --------------------------------------------------------------------
def main(argv):
    string = "The fox & the c@ jumped over the big + lazy dog! Oh, no."
    print(string)
    print(clean(string))
    print(base_chars(13))


if __name__ == "__main__":
    main(sys.argv)
# ------------------------------------------------------------------------------
