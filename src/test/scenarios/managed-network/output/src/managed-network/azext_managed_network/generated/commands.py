# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from ._client_factory import cf_managed_network
    managed_network_managed_network = CliCommandType(
        operations_tmpl='azext_managed_network.vendored_sdks.managednetwork.operations._managed_network_operations#ManagedNetworkOperations.{}',
        client_factory=cf_managed_network)
    with self.command_group('managed-network managed-network', managed_network_managed_network, client_factory=cf_managed_network) as g:
        g.custom_command('list', 'managed_network_managed_network_list')
        g.custom_show_command('show', 'managed_network_managed_network_show')
        g.custom_command('create', 'managed_network_managed_network_create')
        g.custom_command('update', 'managed_network_managed_network_update')
        g.custom_command('delete', 'managed_network_managed_network_delete')

    from ._client_factory import cf_scope_assignment
    managed_network_scope_assignment = CliCommandType(
        operations_tmpl='azext_managed_network.vendored_sdks.managednetwork.operations._scope_assignment_operations#ScopeAssignmentOperations.{}',
        client_factory=cf_scope_assignment)
    with self.command_group('managed-network scope-assignment', managed_network_scope_assignment, client_factory=cf_scope_assignment) as g:
        g.custom_command('list', 'managed_network_scope_assignment_list')
        g.custom_show_command('show', 'managed_network_scope_assignment_show')
        g.custom_command('create', 'managed_network_scope_assignment_create')
        g.custom_command('update', 'managed_network_scope_assignment_update')
        g.custom_command('delete', 'managed_network_scope_assignment_delete')

    from ._client_factory import cf_managed_network_group
    managed_network_managed_network_group = CliCommandType(
        operations_tmpl='azext_managed_network.vendored_sdks.managednetwork.operations._managed_network_group_operations#ManagedNetworkGroupOperations.{}',
        client_factory=cf_managed_network_group)
    with self.command_group('managed-network managed-network-group', managed_network_managed_network_group, client_factory=cf_managed_network_group) as g:
        g.custom_command('list', 'managed_network_managed_network_group_list')
        g.custom_show_command('show', 'managed_network_managed_network_group_show')
        g.custom_command('create', 'managed_network_managed_network_group_create')
        g.custom_command('update', 'managed_network_managed_network_group_update')
        g.custom_command('delete', 'managed_network_managed_network_group_delete')

    from ._client_factory import cf_managed_network_peering_policy
    managed_network_managed_network_peering_policy = CliCommandType(
        operations_tmpl='azext_managed_network.vendored_sdks.managednetwork.operations._managed_network_peering_policy_operations#ManagedNetworkPeeringPolicyOperations.{}',
        client_factory=cf_managed_network_peering_policy)
    with self.command_group('managed-network managed-network-peering-policy', managed_network_managed_network_peering_policy, client_factory=cf_managed_network_peering_policy) as g:
        g.custom_command('list', 'managed_network_managed_network_peering_policy_list')
        g.custom_show_command('show', 'managed_network_managed_network_peering_policy_show')
        g.custom_command('create', 'managed_network_managed_network_peering_policy_create')
        g.custom_command('update', 'managed_network_managed_network_peering_policy_update')
        g.custom_command('delete', 'managed_network_managed_network_peering_policy_delete')

    from ._client_factory import cf_operation
    managed_network_operation = CliCommandType(
        operations_tmpl='azext_managed_network.vendored_sdks.managednetwork.operations._operation_operations#OperationOperations.{}',
        client_factory=cf_operation)
    with self.command_group('managed-network operation', managed_network_operation, client_factory=cf_operation) as g:
        g.custom_command('list', 'managed_network_operation_list')
