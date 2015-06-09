#!/usr/bin/python

import os, imp

testlocation = os.path.dirname(os.path.realpath(__file__)) + "/tests"
print("Searching test files in " + testlocation)
statusCode = 0
for test in os.listdir(testlocation):
	if test.endswith(".py"):
		print("Preparing test " + test)
		absfile = testlocation + "/" + test
		fileContent = open(absfile, "r").read()
		# replace the Firefox driver with phantomjs
		fileContent = fileContent.replace("        self.driver = webdriver.Firefox()", "        self.driver = webdriver.PhantomJS()", 1)
		print("Executing test " + test)
		exec(fileContent)
