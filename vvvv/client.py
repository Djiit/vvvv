import logging

from pythonosc import osc_message_builder
from pythonosc import udp_client


class VVVVClientError(Exception):
    """ Base Exception for VVVVClient. """
    pass


class VVVVClient:
    """ vvvv OSC client. """
    def __init__(self, host='127.0.0.1', port='4444'):
        self.conn = udp_client.UDPClient(host, port)
        return

    def send_msg(self, address, args=[]):
        """ Send multiple args into a single message to a given address. 

        Args:
           address (str): OSC Address.
           args (list): Arguments to be parsed in VVVV.
        """
        if not address.startswith('/'):
            address = '/{}'.format(address)
    
        msg = osc_message_builder.OscMessageBuilder(address=address)
    
        for arg in args:
            msg.add_arg(arg)
        self.conn.send(msg.build())
        return
