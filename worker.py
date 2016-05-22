import nmap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import os
from models import Hosts
from config import db_path, db, app

session = db.session

#CREATE DATABASE
def create_db():
    if not os.path.isdir(db_path):
        os.makedirs(db_path)
    db.create_all()



try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)


def scan(addr):
    hosts = {}
    nm.scan(addr, arguments="-sn")
    for ipaddr in nm.all_hosts():
        try:
            hostname = nm[ipaddr]['hostnames'][0]['name']
            hoststate = nm[ipaddr]['status']['state'].upper()
            hostos = nm[ipaddr]['osmatch'][0]['osclass'][0]['osfamily']
            current_host = Hosts(hostname, ipaddr, hoststate, hostos)
            session.add(current_host)
        except:
            session.rollback()
    session.commit()


@app.route('/')
def get_hosts():
    hosts = session.query(Hosts).all()
    return render_template('main.html', hostlist=hosts)

@app.route('/scan', methods=['POST'])
def scan_net():
    scan(request.files.get("network"))
    return render_template('main.html')


if __name__ == "__main__":
    create_db()
    scan('192.168.1.254')
    app.run(debug=True)
