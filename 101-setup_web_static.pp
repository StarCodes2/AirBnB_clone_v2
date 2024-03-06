# Sets up web servers for deployment of web_static.

$page = "<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>
"

$conf = "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By ${$hostname};
        root /var/www/html;
        index index.html index.htm;
        location /hbnb_static {
                alias /data/web_static/current;
                index index.html index.htm;
        }
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        error_page 404 /404.html;
        location /404 {
                root /var/www/html;
                internal;
        }
}
"

exec { 'apt-get update':
  path   => '/usr/bin/:/usr/local/bin/:/bin/'
} ->

exec { 'apt-get install -y nginx':
  path   => '/usr/bin/:/usr/local/bin/:/bin/'
} ->

exec { 'mkdir -p /data/web_static/shared /data/web_static/releases/test':
  path   => '/usr/bin/:/usr/local/bin/:/bin/'
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $page
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/'
}

exec { 'chown -R ubuntu:ubuntu /data':
  path   => '/usr/bin/:/usr/local/bin/:/bin/'
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $conf
} ->

exec { 'nginx restart':
  path   => '/etc/init.d/'
}
