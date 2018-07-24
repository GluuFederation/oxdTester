# File: /core/flask_server.py
# Purpose: Serve the webpage using Flask

# Import required modules
import os
import sys
import logging
import configparser
import urllib2
from webfinger import finger
import oxdpython
from oxdpython import Client
from flask import Flask, redirect, render_template
import uris.authorize
import uris.login_callback
import uris.logout

# Define the process_op_config() function
def process_op_config():
	# Function: process_op_config()
	# Purpose: Process the OP's /.well-known/openid-configuration and return important values
	# Arguments: None
	
	# Fetch the configuration information
	op_openid_conf_response = urllib2.urlopen("https://rp.certification.openid.net:8080/mod_auth_openidc/rp-response_type-code/.well-known/openid-configuration") # QUICK FIX, REPLACE WITH VALUE FROM CONFIG FILE

	# Read the OP's configuration
	op_openid_conf = op_openid_conf_response.read()


# Route and define the index() function
@app.route("/")
def index():
	# Function: index()
	# Purpose: Act as the index directory of the website and register site
	# Arguments: None
	
	# Set the oxd client
	oxd_client = oxdpython.Client(config)
	
	# DEBUGGING
	print("[D] oxd Client: {}".format(oxd_client))
	
	# Register the site
	global oxd_id 
	oxd_id = oxd_client.register_site()
	
	# DEBUGGING
	print("[D] oxd ID: {}".format(oxd_id))
	
	# Specify the path of the index file
	webpage_index_path = "oxd-rp-certification-python/resources/site/index.html"
	
	# Open the index file
	webpage_index = open(webpage_index_path, "r")
	
	# Return the contents of the file
	return webpage_index.read()
	
# Route and define the test_1() function
@app.route("/test_1/", methods=["POST", "GET"])
def test_1():
	# Function: test_1()
	# Purpose: Serve as the first test, preforming a simple Authorization Code Flow
	# Arguments: None
	
	# Specify the issuer and log file for the test
	test_issuer = "https://rp.certification.openid.net:8080/oxd-server/rp-response_type-code"
	test_log = "https://rp.certification.openid.net:8080/log/oxd-server/rp-response_type-code.txt"
	
	return(redirect("/test_1/"))
 
# Create the Flask app
app = Flask(__name__)

# Set the configuration file
config = os.getcwd() + "/config.cfg"

# Set the oxd client
oxd_client = oxdpython.Client(config)

# Fetch the configuration information
op_openid_conf_response = urllib2.urlopen("https://rp.certification.openid.net:8080/mod_auth_openidc/rp-response_type-code/.well-known/openid-configuration") # QUICK FIX, REPLACE WITH VALUE FROM CONFIG FILE

# Read the OP's configuration
op_openid_conf = op_openid_conf_response.read()

# Display the OP's configuration
print(op_openid_conf)
