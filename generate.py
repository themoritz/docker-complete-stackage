import sys
import yaml

def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

snapshot = yaml.load(sys.stdin)
packages = snapshot['packages'].keys()

print """
FROM fpco/stack-build:lts-7.2

RUN stack update

RUN mkdir -p /root/.stack/global-project
RUN echo 'flags: {}\\n\\
extra-package-dbs: []\\n\\
packages: []\\n\\
extra-deps: []\\n\\
resolver: lts-7.2\\n'\\
> /root/.stack/global-project/stack.yaml

"""

chunkSize = 1 + len(packages) / 120

for ps in chunks(packages, chunkSize):
    print "RUN stack build {}".format(" ".join(ps))
