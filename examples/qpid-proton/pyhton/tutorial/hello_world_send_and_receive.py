#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import print_function, unicode_literals

from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container


class HelloWorld(MessagingHandler):
    def __init__(self, server, address, user, password):
        super(HelloWorld, self).__init__()
        self.server = server
        self.address = address
        self.user = user
        self.password = password

    def on_start(self, event):
        conn = event.container.connect(self.server,
                                       user=self.user,
                                       password=self.password)
        event.container.create_receiver(conn, self.address)
        event.container.create_sender(conn, self.address)

    def on_sendable(self, event):
        event.sender.send(Message(body='Hello World!'))
        event.sender.close()

    def on_message(self, event):
        print(event.message.body)
        event.connection.close()


Container(HelloWorld('localhost:5672', 'examples', 'artemis', 'artemis')).run()
