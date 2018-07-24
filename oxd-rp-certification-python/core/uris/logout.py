# File: /oxd-rp-certification-python/core/uris/logout.py
# Purpose: Act as the /logout/ path

# Import required modules
import os
import sys
import oxdpython

# Define the logout() function
def logout(oxd_client):
	# Function: logout()
	# Purpose: Fetch the logout URI
	# Arguments:
	#	oxd_client - The oxd client
	
	# Fetch the logout URI
	logout_uri = oxd_client.get_logout_uri()
	
	# Return the logout URI
	return logout_uri
