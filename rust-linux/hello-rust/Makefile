# check something in container : docker run -it --rm -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust /bin/sh

all:
	docker run --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust cargo build --release
