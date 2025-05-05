# Lab 6: Modal Logic and Temporal Properties
# PyNuSMV can be used to verify temporal properties:
# Install PyNuSMV
# !pip install pynusmv

# Install PyNuSMV
# !pip install pynusmv

# Import and initialize
from pynusmv import init, glob
# Load the SMV model
init(["example.smv"])
# Check and evaluate CTL properties
if glob.prop_database.size > 0:
    for i in range(glob.prop_database.size):
        print(f"Property {i}: {glob.prop_database.get(i).evaluate()}")
else:
    print("No properties found.")
# You’ll need an .smv file containing the NuSMV model uploaded to Colab.