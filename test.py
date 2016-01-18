import urllib2

print "Everything is working"
print "This is fine"

text = urllib2.urlopen("http://codesoftwarecomputation.github.io/test").read()

print text