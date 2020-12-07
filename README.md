# Goal
This is an Ansible role that is intended to be used as part of the setup
process for Linux machines, especially for K8S development.

This will find any unused block devices and make them available for use under /mnt/disks/.

# Non-goal
This does not support different configurations per device.
This is done so that this role can allow the caller to create as many devices
as possible without requiring coordination between this role and its caller.

# Dependencies
This depends on https://github.com/pwyoung/ansible-role-create-partition which is a fork
of the https://github.com/mcgrof/create_partition.

"create_partition" is being used because it's a robust, idempotent role to mount Linux partitions.

The fork exists in case the dependency is renamed and because this project tried to be consistent in
how it names its dependencies (ansible-role-foo and ansible-playbook-bar).

# Algorithm
Find any unused block devices via lsblk.
Make the partition available under /mnt/disks/ via the dependency described above.

# License

GPLv2
