#!/usr/bin/env python
#
# Copyright 2010 Google Inc.
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

from distutils import core

core.setup(
  name='google-protorpc',
  version='1.0.0',
  url='https://github.com/gregorynicholas/google-protorpc',
  packages=[
    'protorpc',
    'protorpc._google',
    'protorpc._google.net',
    'protorpc._google.net.proto',
    'protorpc._google.net.proto2',
    'protorpc._google.net.proto2.proto',
    'protorpc._google.net.proto2.python',
    'protorpc._google.net.proto2.python.internal',
    'protorpc._google.net.proto2.python.public',
    'protorpc._google.pyglib',
    'protorpc.wsgi',
  ],
  namespace_packages=[
    'protorpc',
  ],
  scripts=[
    'gen_protorpc.py',
  ],
  install_requires=[
  ],
)
