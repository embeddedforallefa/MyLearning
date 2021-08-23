1. sudo apt-get upgrade
2. sudo apt-get update
-----------------------------------------------
Disk Partition:
1. sudo lsblk # The lsblk command also lists the partitions
2. sudo cfdisk /dev/sdb # create partisions for lfs
-----------------------------------------------
echo $LFS
export LFS=/mnt/lfs
-----------------------------------------------
mkdir -v $LFS/sources

chmod -v a+wt $LFS/sources

wget --input-file=wget-list --continue --directory-prefix=$LFS/sources

-----------------------------------------------
mkdir -pv $LFS/{bin,etc,lib,sbin,usr,var}
case $(uname -m) in
x86_64) mkdir -pv $LFS/lib64 ;;
esac

mkdir -pv $LFS/tools

groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs

passwd lfs

chown -v lfs $LFS/{usr,lib,var,etc,bin,sbin,tools}
case $(uname -m) in
x86_64) chown -v lfs $LFS/lib64 ;;
esac

chown -v lfs $LFS/sources

chown -v lfs $LFS/{usr,lib,var,etc,bin,sbin,tools,lib64,sources}
