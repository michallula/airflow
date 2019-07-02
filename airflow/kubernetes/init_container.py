# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


class InitContainer:
    """Defines Kubernetes Init Container"""

    def __init__(self, name, image, security_context, init_environment=None, volume_mounts=None):
        """Initialize a Kubernetes Init Container. Used for setup Pods.
        :param name: the name of the volume mount
        :type name: str
        :param image:
        :type image: str
        :param security_context: subpath within the volume mount
        :type security_context: dict
        :param init_environment: whether to access pod with read-only mode
        :type init_environment: dict
        :param volume_mounts: whether to access pod with read-only mode
        :type volume_mounts: dict
        """
        self.name = name
        self.image = image
        self.security_context = security_context
        self.init_environment = init_environment or {}
        self.volume_mounts = volume_mounts or {}
