# Using Puppet to create a manifest that kills a process

exec { 'killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  provider => shell,
  returns  => [0, 1]
}
