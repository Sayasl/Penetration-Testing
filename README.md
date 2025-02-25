# Penetration-Testing:

The repository contains two versions of the brute-force script:
## brute_force_attack.py:
A basic script that sends HTTP POST requests to a target login endpoint, iterating through a list of common passwords until a successful login is detected.
## brute_force_attack 2.py:
An enhanced version that includes additional handling for rate limiting (HTTP 429 responses), which stops the brute-force process if too many requests are sent in a short period.
Both scripts use the requests library to perform HTTP POST requests and simulate login attempts against a local test server hosted at http://127.0.0.2:4000/login.
## login_system.py:
A basic login system that verifies usernames and passwords using a predefined dictionary. It runs a Flask API at http://127.0.0.2:4000/login that accepts POST requests with login credentials.
## login_system(limit 5 IP per mnt).py:
An enhanced version that includes rate limiting to block excessive login attempts. It uses Flask-Limiter to allow only 5 login attempts per minute per IP.

## Disclaimer:
These projects are designed for learning and testing in controlled environments only. Unauthorized use against systems you do not own or have explicit permission to test is illegal and unethical.
