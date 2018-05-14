#!/bin/bash
ansible-playbook -vvvv ./deploy.yml --private-key=/Users/jurajklucka/.ssh/id_rsa -u deployer -i ./hosts

