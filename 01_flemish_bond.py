
import os
import json

import compas
from compas.geometry import Translation
from assembly import Element, Assembly

HERE = os.path.dirname(__file__)
DATA = os.path.abspath(os.path.join(HERE, "data"))

# The name of the json file to save the assembly into
PATH_TO = os.path.join(DATA, "flemish_bond.json")

# Load assembly settings
settings_file = os.path.join(DATA, "settings.json")
with open(settings_file, 'r') as f:
    data = json.load(f)

brick = Element.from_data(data['brick'])
halfbrick = Element.from_data(data['halfbrick'])
width, length, height = data['brick_dimensions']

# Create assembly
assembly = Assembly()

# ==============================================================================
# Your code comes here




# ==============================================================================

# Transform assembly to correct location and adjust if needed
assembly.transform(Translation([-0.26, -0.34, 0]))

# Save assembly to json
assembly.to_json(PATH_TO)

# Run this in rhino
if compas.IPY:
    from assembly.rhino import AssemblyArtist
    artist = AssemblyArtist(assembly)
    artist.draw()
