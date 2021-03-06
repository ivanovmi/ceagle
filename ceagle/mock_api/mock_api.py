# Copyright 2016: Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import random

import flask


def _gen_values(mode):

    if mode == 1:
        return [["24-Sep-16T%s" % i, random.uniform(0.9, 1)]
                for i in range(24)]
    elif mode == 2:
        return [["24-Sep-16T%s" % i, random.randint(20, 2000)]
                for i in range(24)]
    else:
        return [["24-Sep-16T%s" % i, random.randint(100, 40000)]
                for i in range(24)]


def health_projects():
    return flask.jsonify(**{
        "project_names": ["keystone", "nova", "glance", "cinder", "neutron"],
        "projects": {

            "keystone": {
                "fci": 0.9,
                "fci_score_data": _gen_values(1),
                "response_time_data": _gen_values(2),
                "response_size_data": _gen_values(3)
            },
            "nova": {
                "fci": 1.0,
                "fci_score_data": _gen_values(1),
                "response_time_data": _gen_values(2),
                "response_size_data": _gen_values(3)
            },
            "glance": {
                "fci": 0.96,
                "fci_score_data": _gen_values(1),
                "response_time_data": _gen_values(2),
                "response_size_data": _gen_values(3)
            },
            "cinder": {
                "fci": 0.995,
                "fci_score_data": _gen_values(1),
                "response_time_data": _gen_values(2),
                "response_size_data": _gen_values(3)

            },
            "neutron": {
                "fci": 0.999,
                "fci_score_data": _gen_values(1),
                "response_time_data": _gen_values(2),
                "response_size_data": _gen_values(3)

            }
        }
    })
