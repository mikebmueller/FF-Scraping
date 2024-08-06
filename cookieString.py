
# Paste your cookie string here
cookie_string = "179643557%7CMCIDTS%7C19942%7CMCMID%7C72901627170543240313289426438946126625%7CMCAID%7CNONE%7CMCOPTOUT-1722981050s%7CNONE%7CvVersion%7C5.5.0"

# Dict to store cookies
cookies = {}

# Loop through each cookie
for cookie in cookie_string.split('; '):
    # Split cookie into name and value
    cookie_parts = cookie.split('=')
    cookies[cookie_parts[0]] = cookie_parts[1]
