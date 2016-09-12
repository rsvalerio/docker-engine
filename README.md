docker-engine
=========

Install Docker Engine in a couple of different linux versions


Requirements
------------

Vagrant to create VMs for test purpose
Testinfra to verify installation/configuration

Role Variables
--------------

docker_pkg_name: 'docker-engine'

apt_cache_valid_time: 0

apt_key_url: ''

apt_key_sig: ''

apt_repository: deb https://apt.dockerproject.org/repo ubuntu-{{ ansible_distribution_release }} main

Dependencies
------------

n/a

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

Test
-------

Create VMs to test (will download and start all vms, take a coffee :)

```bash
cd test
vagrant up 
```

Running the role (run two times to see idempotency)

```bash
ansible-playbook -i hosts playbook.yml -u vagrant
```


Verify if is everything ok

```bash
testinfra test_default.py -v --connection=ssh --ssh-config=ssh_config --hosts=trusty,wily,xenial,centos6,centos7
```


License
-------

BSD

Author Information
------------------

Rodrigo Valerio
github.com/rsvalerio
twitter.com/rsvalerio
