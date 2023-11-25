# Using Puppet to create a file in tmp

file { 'school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  path    => '/tmp/school',
  content => 'I love Puppet'
}
