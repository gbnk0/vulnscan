#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import db

class Hosts(db.Model):

    hostid = db.Column(db.Integer, autoincrement = True, primary_key=True)
    hostname = db.Column(db.String)
    ipaddr = db.Column(db.String)
    hoststate = db.Column(db.String)
    hostos = db.Column(db.String)
    hostvendor = db.Column(db.String)


    def __init__(self, hostname, ipaddr, hoststate, hostos=None, hostvendor=None):
        
        self.hostname = hostname
        self.ipaddr = ipaddr
        self.hoststate = hoststate
        self.hostos = hostos
        self.hostvendor = hostvendor
