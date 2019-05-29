#!/usr/bin/env python3

from charmhelpers.core.services.base import ServiceManager
from charmhelpers.core.services import helpers

import actions


def manage():
    manager = ServiceManager([
        {
            'service': 'kamailio',
            'ports': [],  # ports to after start
            'provided_data': [
                # context managers for provided relations
                # e.g.: helpers.HttpRelation()
            ],
            'required_data': [
                # data (contexts) required to start the service
                # e.g.: helpers.RequiredConfig('domain', 'auth_key'),
                #       helpers.MysqlRelation(),
            ],
            'data_ready': [
                helpers.render_template(
                    source='upstart.conf',
                    target='/etc/init/kamailio'),
                actions.log_start,
            ],
        },
    ])
    manager.manage()
