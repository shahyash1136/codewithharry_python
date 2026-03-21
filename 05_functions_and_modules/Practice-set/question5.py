# 5. Modules and Pip – Using External Libraries
# 1. Import the  math  module and use it to:
#     a. Find the square root of 144
#     b. Calculate  sin(90°)  (hint: use  math.radians() )
import math
import requests

print(math.sqrt(144))
print(math.sin(math.radians(90)))

# 2. Install and import the  requests  module (if available) and use it to fetch data from  "https://api.github.com" .
r = requests.get("https://api.github.com")
print(r.json())
