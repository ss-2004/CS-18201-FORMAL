# Install PyNuSMV if not already installed
# !pip install pynusmv

from pynusmv import init, glob
# Load the NuSMV model file
init(["traffic_light.smv"])
# Evaluate CTL properties in the model
if glob.prop_database.size > 0:
    for i in range(glob.prop_database.size):
        prop = glob.prop_database.get(i)
        result = prop.evaluate()
        print(f"Property {i} result: {result}")
else:
    print("No CTL properties found in the SMV file.")
