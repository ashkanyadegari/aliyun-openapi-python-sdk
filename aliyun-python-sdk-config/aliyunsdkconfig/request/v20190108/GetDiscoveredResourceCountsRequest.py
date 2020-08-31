# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class GetDiscoveredResourceCountsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Config', '2019-01-08', 'GetDiscoveredResourceCounts','config')
		self.set_method('GET')

	def get_MultiAccount(self):
		return self.get_query_params().get('MultiAccount')

	def set_MultiAccount(self,MultiAccount):
		self.add_query_param('MultiAccount',MultiAccount)

	def get_GroupByKey(self):
		return self.get_query_params().get('GroupByKey')

	def set_GroupByKey(self,GroupByKey):
		self.add_query_param('GroupByKey',GroupByKey)

	def get_MemberId(self):
		return self.get_query_params().get('MemberId')

	def set_MemberId(self,MemberId):
		self.add_query_param('MemberId',MemberId)