Linux From Scratch is an attempt to build your own Linux distribution.

The chief aim is to learn and master how Linux works.

1. Creating a New Disk Partition
commands: 
	sudo lsblk # The lsblk command also lists the partitions
	sudo cfdisk /dev/sdb # create partisions for lfs
	create sdb1 for root and sdb2 for swap
2. Creating a File System on the Partition
commands:
	mkfs -v -t ext4 /dev/sdb1
	mkswap /dev/sdb2
3. Setting The $LFS Variable
commands:
	export LFS=/mnt/lfs
	echo $LFS
	update .bashrc  and bash_profile with above command
4. Mounting the New Partition
commands:
	mkdir -pv $LFS
	mount -v -t ext4 /dev/sdb1 $LFS
update /etc/fstab with 
	/dev/sdb1  /mnt/lfs ext4   defaults      1     1
for swap partision
	/sbin/swapon -v /dev/sdb2
