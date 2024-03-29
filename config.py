# WORLD SET UP
NUM_AGENTS = 50
WORLD_SIZE = 20
NUM_ITERS = 100
NUM_SITES = 3 # optimal: 20
NUM_PREDS = 0
SITE_REGEN_TIME = 10
SITE_MAX_RESOURCE = 200
PADDING = 0.5
DT = 0.01
NUM_GROUPS = 3

# hard code some color constants for 3 groups. will randomize later
PINK = "#FF00FF"
CYAN = "#00FFFF"
GREEN = "#00FF00"
COLORS = {0: PINK, 1: CYAN, 2: GREEN}

# AGENT PROPERTIES
AGENT_SENSING_RADIUS = 5
MAX_HUNGER = 100
MAX_SPEED = 5.0
MAX_SITE_MEMORY = 3
AGENT_NEIGHBOR_THRESHOLD = 10
MAX_NETWORK_SIZE = (NUM_AGENTS // NUM_GROUPS) + 1
# Used for base states
AGENT_NEIGHBOR_THRESHOLD = NUM_AGENTS//10


# PREDATOR PROPERTIES
PREDATOR_SENSING_RADIUS = 5
HUNTING_MULTIPLIER = 3
PREDATOR_NEIGHBOR_THRESHOLD = 5
