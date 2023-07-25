import os

# Unicorn
HOST = os.getenv('HOST', "0.0.0.0")
PORT = int(os.getenv('PORT', 8001))


# Other
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]