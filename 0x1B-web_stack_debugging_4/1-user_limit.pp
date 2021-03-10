#Change the user limitations

exec { 'permissions':
  command => "sed -i 's/4/32000/g' /etc/security/limits.conf && sed -i 's/5/32000/g' /etc/security/limits.conf",
  path    => '/bin',
}
