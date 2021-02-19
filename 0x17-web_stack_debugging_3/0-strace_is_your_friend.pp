#fix wp settings

exec { 'fix-wp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}