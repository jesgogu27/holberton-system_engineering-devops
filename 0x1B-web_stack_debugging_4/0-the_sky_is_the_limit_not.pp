#change the limit

exec { 'increase':
  command => "sed -i 's/15/2000/g' /etc/default/nginx && /etc/init.d/nginx restart",
  path    => '/bin',
}