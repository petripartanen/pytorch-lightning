# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from abc import ABC, abstractmethod
from typing import Optional


class ClusterEnvironment(ABC):
    """ Specification of a cluster environment. """

    @abstractmethod
    def spawns_children(self) -> bool:
        """ Whether the environment spawns the subprocesses or not. """

    @abstractmethod
    def master_address(self) -> str:
        """ The master address through which all processes connect and communicate. """

    @abstractmethod
    def master_port(self) -> int:
        """ An open and configured port in the master node through which all processes communicate. """

    @abstractmethod
    def world_size(self) -> Optional[int]:
        """ The number of processes across all devices and nodes. """

    @abstractmethod
    def local_rank(self) -> int:
        """ The rank (index) of the currently running process inside of the current node. """

    @abstractmethod
    def node_rank(self) -> int:
        """ The rank (index) of the node on which the current process runs. """

    def node_rank(self) -> int:
        pass
