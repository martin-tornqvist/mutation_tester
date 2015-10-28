'''
Global paths and variables
'''

#===============================================================================
# Config directory
#===============================================================================
EXECUTE_TESTS_HOOK_NAME = 'execute-tests'
MUTATION_FILES_NAME = 'mutation-files'
SRC_BASE_NAME = 'src-base'

#===============================================================================
# Output directory
#===============================================================================
SRC_BASE_SHA1 = 'src-base-sha1'
CLEAN_TEST_RESULTS = 'test-results-clean'
TEST_RESULTS = 'test-results'

#===============================================================================
# Current sequence directory
#===============================================================================
CUR_SEQ_DIR = ''

#===============================================================================
# Serial numbered directory under the sequence directory to store output
# specific for the current mutation (e.g. a patch and test result)
#===============================================================================
CUR_MUTATION_DIR = ''

#===============================================================================
# User arguments
#===============================================================================
MUTATION_TOOL_ROOT = ''
PROJECT_ROOT = ''
CONFIG_PATH = ''
OUTPUT_PATH = ''
RNG_SEED = ''

# Default global timeout in seconds (two hours)
GLOBAL_TIMEOUT = 7200

#===============================================================================
# Start time of this program
#===============================================================================
TOOL_START_TIME = -1
