Linux From Scratch is an attempt to build your own Linux distribution.

The chief aim is to learn and master how Linux works.

1. Create directory to store the downloaded packages and patches and Make this directory writable and sticky
commands: 
	sudo mkdir -v $LFS/sources 
	chmod -v a+wt $LFS/sources
2. To download all of the packages and patches by using wget-list as an input to the wget command, use:
commands:
	wget --input-file=wget-list --continue --directory-prefix=$LFS/sources
