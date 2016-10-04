## Usage

```shell
$ wget -qO- https://github.com/fpco/lts-haskell/blob/master/lts-7.2.yaml | python generate.py > dockerfiles/lts-7.2/Dockerfile
$ cd dockerfiles/lts-7.2
$ docker build .
```
