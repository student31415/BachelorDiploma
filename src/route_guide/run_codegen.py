# Copyright 2015 gRPC authors.
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
"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""

from grpc_tools import protoc
import grpc_tracer
def main():
    traced = True

    if not traced :
        protoc.main((
            '',
            '-I.',
            '--python_out=.',
            '--grpc_python_out=.',
            './route_guide.proto',
        ))
    else:
        grpc_tracer.main((
            '',
            '-I.',
            '--python_out=.',
            '--grpc_python_out=.',
            './route_guide.proto',
        ))

if __name__ == "__main__":
    main()