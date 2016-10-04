import sys
import yaml

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

for p in packages:
    print "RUN stack build {}".format(p)
