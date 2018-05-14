#!/bin/bash
ansible-playbook -vvvv ./init_config.yml --private-key=/Users/jurajklucka/.ssh/id_rsa -u root -i ./hosts

