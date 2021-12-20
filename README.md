# Goal
This is an Ansible role that is intended to be used as part of the setup
process for Linux machines.

# Dependencies
- This depends on https://github.com/mcgrof/create_partition.
   - "create_partition" is being used because it's a robust idempotent role manage Linux partitions.

# Example usage
- You can look at ./test/README.md for details on setting up a limited local test.
- The configuration data is described in ./test/group_vars/all
- An example of The necessary configuration is in ./test/group_vars/all
- Run "make" here or in the test directory to invoke the test.

# License

GPLv2
