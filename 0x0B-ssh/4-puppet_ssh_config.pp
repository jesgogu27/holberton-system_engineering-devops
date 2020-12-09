#!/usr/bin/env bash
# Client configuration file (w/ Puppet)

file_line { 'No passwd authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes'
}

file_line { 'State identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => ' IdentityFile ~/.ssh/holberton',
}