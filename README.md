# Qpid Proton

https://qpid.apache.org/proton/

## The AMQP messaging toolkit

Qpid Proton is a high-performance, lightweight messaging library.
It can be used in the widest range of messaging applications,
including brokers, client libraries, routers, bridges, proxies, and more.
Proton makes it trivial to integrate with the AMQP 1.0 ecosystem from any platform,
environment, or language

## Source Code

[Releaes](https://qpid.apache.org/releases/)

[Browse via GitHub](https://github.com/apache/qpid-proton)


## Exemplos e testes com qpid-proton

```bash

$ cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local/qpid-proton -DSYSINSTALL_BINDINGS=OFF
$ make
$ sudo make install

# echo '/usr/local/qpid-proton/lib' >>/etc/ld.so.conf.d/qpid-proton.conf 

# ldconf -v
```

## Docker Image Example

https://github.com/apache/activemq-artemis/tree/master/artemis-docker

## Local

[Download ActiveMQ Artemis](https://activemq.apache.org/components/artemis/download/)

wget -c 'https://www.apache.org/dyn/closer.cgi?filename=activemq/activemq-artemis/2.16.0/apache-artemis-2.16.0-bin.tar.gz&action=download' \
       -O apache-artemis-2.16.0-bin.tar.gz'

