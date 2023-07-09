# If set, the program will separate every call to youtube in distinct threads.
# This reduce the execution time but raises the CPU usage. Be careful.
ALLOW_THREADING: bool=True

# If set, it will not print advise logs
QUIET: bool=False

VIABLE_NUMBER_OF_LINKS_TO_PROCCESS_WITHOUT_THREADING: int=15