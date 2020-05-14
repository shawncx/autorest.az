# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['datafactory'] = """
    type: group
    short-summary: datafactory
"""

helps['datafactory list'] = """
    type: command
    short-summary: Lists factories under the specified subscription.
    examples:
      - name: Factories_ListByResourceGroup
        text: |-
               az datafactory list --resource-group "exampleResourceGroup"
"""

helps['datafactory show'] = """
    type: command
    short-summary: Gets a factory.
    examples:
      - name: Factories_Get
        text: |-
               az datafactory show --name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory create'] = """
    type: command
    short-summary: Creates or updates a factory.
    examples:
      - name: Factories_CreateOrUpdate
        text: |-
               az datafactory create --location "East US" --name "exampleFactoryName" --resource-group "exampleResource\
Group"
"""

helps['datafactory update'] = """
    type: command
    short-summary: Updates a factory.
    examples:
      - name: Factories_Update
        text: |-
               az datafactory update --name "exampleFactoryName" --tags exampleTag="exampleValue" --resource-group "exa\
mpleResourceGroup"
"""

helps['datafactory delete'] = """
    type: command
    short-summary: Deletes a factory.
    examples:
      - name: Factories_Delete
        text: |-
               az datafactory delete --name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory configure-factory-repo'] = """
    type: command
    short-summary: Updates a factory's repo information.
    examples:
      - name: Factories_ConfigureFactoryRepo
        text: |-
               az datafactory configure-factory-repo --factory-resource-id "/subscriptions/12345678-1234-1234-1234-1234\
5678abc/resourceGroups/exampleResourceGroup/providers/Microsoft.DataFactory/factories/exampleFactoryName" --factory-vst\
s-configuration account-name="ADF" collaboration-branch="master" last-commit-id="" project-name="project" repository-na\
me="repo" root-folder="/" tenant-id="" --location-id "East US"
"""

helps['datafactory get-data-plane-access'] = """
    type: command
    short-summary: Get Data Plane access.
    examples:
      - name: Factories_GetDataPlaneAccess
        text: |-
               az datafactory get-data-plane-access --name "exampleFactoryName" --access-resource-path "" --expire-time\
 "2018-11-10T09:46:20.2659347Z" --permissions "r" --profile-name "DefaultProfile" --start-time "2018-11-10T02:46:20.265\
9347Z" --resource-group "exampleResourceGroup"
"""

helps['datafactory get-git-hub-access-token'] = """
    type: command
    short-summary: Get GitHub Access Token.
    examples:
      - name: Factories_GetGitHubAccessToken
        text: |-
               az datafactory get-git-hub-access-token --name "exampleFactoryName" --git-hub-access-code "some" --git-h\
ub-access-token-base-url "some" --git-hub-client-id "some" --resource-group "exampleResourceGroup"
"""

helps['datafactory trigger'] = """
    type: group
    short-summary: datafactory trigger
"""

helps['datafactory trigger list'] = """
    type: command
    short-summary: Lists triggers.
    examples:
      - name: Triggers_ListByFactory
        text: |-
               az datafactory trigger list --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory trigger show'] = """
    type: command
    short-summary: Gets a trigger.
    examples:
      - name: Triggers_Get
        text: |-
               az datafactory trigger show --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup" \
--name "exampleTrigger"
"""

helps['datafactory trigger create'] = """
    type: command
    short-summary: Creates or updates a trigger.
    examples:
      - name: Triggers_Create
        text: |-
               az datafactory trigger create --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup\
" --properties "{\\"type\\":\\"ScheduleTrigger\\",\\"pipelines\\":[{\\"parameters\\":{\\"OutputBlobNameList\\":[\\"exam\
pleoutput.csv\\"]},\\"pipelineReference\\":{\\"type\\":\\"PipelineReference\\",\\"referenceName\\":\\"examplePipeline\\\
"}}],\\"typeProperties\\":{\\"recurrence\\":{\\"endTime\\":\\"2018-06-16T00:55:13.8441801Z\\",\\"frequency\\":\\"Minute\
\\",\\"interval\\":4,\\"startTime\\":\\"2018-06-16T00:39:13.8441801Z\\",\\"timeZone\\":\\"UTC\\"}}}" --name "exampleTri\
gger"
      - name: Triggers_Update
        text: |-
               az datafactory trigger create --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup\
" --properties "{\\"type\\":\\"ScheduleTrigger\\",\\"description\\":\\"Example description\\",\\"pipelines\\":[{\\"para\
meters\\":{\\"OutputBlobNameList\\":[\\"exampleoutput.csv\\"]},\\"pipelineReference\\":{\\"type\\":\\"PipelineReference\
\\",\\"referenceName\\":\\"examplePipeline\\"}}],\\"typeProperties\\":{\\"recurrence\\":{\\"endTime\\":\\"2018-06-16T00\
:55:14.905167Z\\",\\"frequency\\":\\"Minute\\",\\"interval\\":4,\\"startTime\\":\\"2018-06-16T00:39:14.905167Z\\",\\"ti\
meZone\\":\\"UTC\\"}}}" --name "exampleTrigger"
"""

helps['datafactory trigger update'] = """
    type: command
    short-summary: Creates or updates a trigger.
    examples:
      - name: Triggers_Create
        text: |-
               az datafactory trigger update --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup\
" --properties "{\\"type\\":\\"ScheduleTrigger\\",\\"pipelines\\":[{\\"parameters\\":{\\"OutputBlobNameList\\":[\\"exam\
pleoutput.csv\\"]},\\"pipelineReference\\":{\\"type\\":\\"PipelineReference\\",\\"referenceName\\":\\"examplePipeline\\\
"}}],\\"typeProperties\\":{\\"recurrence\\":{\\"endTime\\":\\"2018-06-16T00:55:13.8441801Z\\",\\"frequency\\":\\"Minute\
\\",\\"interval\\":4,\\"startTime\\":\\"2018-06-16T00:39:13.8441801Z\\",\\"timeZone\\":\\"UTC\\"}}}" --name "exampleTri\
gger"
      - name: Triggers_Update
        text: |-
               az datafactory trigger update --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup\
" --properties "{\\"type\\":\\"ScheduleTrigger\\",\\"description\\":\\"Example description\\",\\"pipelines\\":[{\\"para\
meters\\":{\\"OutputBlobNameList\\":[\\"exampleoutput.csv\\"]},\\"pipelineReference\\":{\\"type\\":\\"PipelineReference\
\\",\\"referenceName\\":\\"examplePipeline\\"}}],\\"typeProperties\\":{\\"recurrence\\":{\\"endTime\\":\\"2018-06-16T00\
:55:14.905167Z\\",\\"frequency\\":\\"Minute\\",\\"interval\\":4,\\"startTime\\":\\"2018-06-16T00:39:14.905167Z\\",\\"ti\
meZone\\":\\"UTC\\"}}}" --name "exampleTrigger"
"""

helps['datafactory trigger delete'] = """
    type: command
    short-summary: Deletes a trigger.
    examples:
      - name: Triggers_Delete
        text: |-
               az datafactory trigger delete --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup\
" --name "exampleTrigger"
"""

helps['datafactory trigger get-event-subscription-status'] = """
    type: command
    short-summary: Get a trigger's event subscription status.
    examples:
      - name: Triggers_GetEventSubscriptionStatus
        text: |-
               az datafactory trigger get-event-subscription-status --factory-name "exampleFactoryName" --resource-grou\
p "exampleResourceGroup" --name "exampleTrigger"
"""

helps['datafactory trigger query-by-factory'] = """
    type: command
    short-summary: Query triggers.
    examples:
      - name: Triggers_QueryByFactory
        text: |-
               az datafactory trigger query-by-factory --factory-name "exampleFactoryName" --parent-trigger-name "examp\
leTrigger" --resource-group "exampleResourceGroup"
"""

helps['datafactory trigger start'] = """
    type: command
    short-summary: Starts a trigger.
    examples:
      - name: Triggers_Start
        text: |-
               az datafactory trigger start --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup"\
 --name "exampleTrigger"
"""

helps['datafactory trigger stop'] = """
    type: command
    short-summary: Stops a trigger.
    examples:
      - name: Triggers_Stop
        text: |-
               az datafactory trigger stop --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup" \
--name "exampleTrigger"
"""

helps['datafactory trigger subscribe-to-event'] = """
    type: command
    short-summary: Subscribe event trigger to events.
    examples:
      - name: Triggers_SubscribeToEvents
        text: |-
               az datafactory trigger subscribe-to-event --factory-name "exampleFactoryName" --resource-group "exampleR\
esourceGroup" --name "exampleTrigger"
"""

helps['datafactory trigger unsubscribe-from-event'] = """
    type: command
    short-summary: Unsubscribe event trigger from events.
    examples:
      - name: Triggers_UnsubscribeFromEvents
        text: |-
               az datafactory trigger unsubscribe-from-event --factory-name "exampleFactoryName" --resource-group "exam\
pleResourceGroup" --name "exampleTrigger"
"""

helps['datafactory trigger wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datafactory trigger is met.
    examples:
      - name: Pause executing next line of CLI script until the datafactory trigger is successfully created.
        text: |-
               az datafactory trigger wait --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup" \
--name "exampleTrigger" --created
"""

helps['datafactory integration-runtime'] = """
    type: group
    short-summary: datafactory integration-runtime
"""

helps['datafactory integration-runtime list'] = """
    type: command
    short-summary: Lists integration runtimes.
    examples:
      - name: IntegrationRuntimes_ListByFactory
        text: |-
               az datafactory integration-runtime list --factory-name "exampleFactoryName" --resource-group "exampleRes\
ourceGroup"
"""

helps['datafactory integration-runtime show'] = """
    type: command
    short-summary: Gets an integration runtime.
    examples:
      - name: IntegrationRuntimes_Get
        text: |-
               az datafactory integration-runtime show --factory-name "exampleFactoryName" --name "exampleIntegrationRu\
ntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime create'] = """
    type: command
    short-summary: Creates or updates an integration runtime.
    examples:
      - name: IntegrationRuntimes_Create
        text: |-
               az datafactory integration-runtime create --factory-name "exampleFactoryName" --properties "{\\"type\\":\
\\"SelfHosted\\",\\"description\\":\\"A selfhosted integration runtime\\"}" --name "exampleIntegrationRuntime" --resour\
ce-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime linked-integration-runtime'] = """
    type: group
    short-summary: datafactory integration-runtime sub group linked-integration-runtime
"""

helps['datafactory integration-runtime linked-integration-runtime create'] = """
    type: command
    short-summary: Create a linked integration runtime entry in a shared integration runtime.
    examples:
      - name: IntegrationRuntimes_CreateLinkedIntegrationRuntime
        text: |-
               az datafactory integration-runtime linked-integration-runtime create --name "bfa92911-9fb6-4fbe-8f23-bea\
e87bc1c83" --data-factory-location "West US" --data-factory-name "e9955d6d-56ea-4be3-841c-52a12c1a9981" --subscription-\
id "061774c7-4b5a-4159-a55b-365581830283" --factory-name "exampleFactoryName" --integration-runtime-name "exampleIntegr\
ationRuntime" --resource-group "exampleResourceGroup" --subscription-id "12345678-1234-1234-1234-12345678abc"
"""

helps['datafactory integration-runtime update'] = """
    type: command
    short-summary: Updates an integration runtime.
    examples:
      - name: IntegrationRuntimes_Update
        text: |-
               az datafactory integration-runtime update --factory-name "exampleFactoryName" --name "exampleIntegration\
Runtime" --resource-group "exampleResourceGroup" --auto-update "Off" --update-delay-offset "\\"PT3H\\""
"""

helps['datafactory integration-runtime delete'] = """
    type: command
    short-summary: Deletes an integration runtime.
    examples:
      - name: IntegrationRuntimes_Delete
        text: |-
               az datafactory integration-runtime delete --factory-name "exampleFactoryName" --name "exampleIntegration\
Runtime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime get-connection-info'] = """
    type: command
    short-summary: Gets the on-premises integration runtime connection information for encrypting the on-premises data \
source credentials.
    examples:
      - name: IntegrationRuntimes_GetConnectionInfo
        text: |-
               az datafactory integration-runtime get-connection-info --factory-name "exampleFactoryName" --name "examp\
leIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime get-monitoring-data'] = """
    type: command
    short-summary: Get the integration runtime monitoring data, which includes the monitor data for all the nodes under\
 this integration runtime.
    examples:
      - name: IntegrationRuntimes_GetMonitoringData
        text: |-
               az datafactory integration-runtime get-monitoring-data --factory-name "exampleFactoryName" --name "examp\
leIntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime get-status'] = """
    type: command
    short-summary: Gets detailed status information for an integration runtime.
    examples:
      - name: IntegrationRuntimes_GetStatus
        text: |-
               az datafactory integration-runtime get-status --factory-name "exampleFactoryName" --name "exampleIntegra\
tionRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime list-auth-key'] = """
    type: command
    short-summary: Retrieves the authentication keys for an integration runtime.
    examples:
      - name: IntegrationRuntimes_ListAuthKeys
        text: |-
               az datafactory integration-runtime list-auth-key --factory-name "exampleFactoryName" --name "exampleInte\
grationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime regenerate-auth-key'] = """
    type: command
    short-summary: Regenerates the authentication key for an integration runtime.
    examples:
      - name: IntegrationRuntimes_RegenerateAuthKey
        text: |-
               az datafactory integration-runtime regenerate-auth-key --factory-name "exampleFactoryName" --name "examp\
leIntegrationRuntime" --regenerate-key-parameters "{\\"keyName\\":\\"authKey2\\"}" --resource-group "exampleResourceGro\
up"
"""

helps['datafactory integration-runtime remove-link'] = """
    type: command
    short-summary: Remove all linked integration runtimes under specific data factory in a self-hosted integration runt\
ime.
    examples:
      - name: IntegrationRuntimes_Upgrade
        text: |-
               az datafactory integration-runtime remove-link --factory-name "exampleFactoryName" --name "exampleIntegr\
ationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime start'] = """
    type: command
    short-summary: Starts a ManagedReserved type integration runtime.
    examples:
      - name: IntegrationRuntimes_Start
        text: |-
               az datafactory integration-runtime start --factory-name "exampleFactoryName" --name "exampleManagedInteg\
rationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime stop'] = """
    type: command
    short-summary: Stops a ManagedReserved type integration runtime.
    examples:
      - name: IntegrationRuntimes_Stop
        text: |-
               az datafactory integration-runtime stop --factory-name "exampleFactoryName" --name "exampleManagedIntegr\
ationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime sync-credentials'] = """
    type: command
    short-summary: Force the integration runtime to synchronize credentials across integration runtime nodes, and this \
will override the credentials across all worker nodes with those available on the dispatcher node. If you already have \
the latest credential backup file, you should manually import it (preferred) on any self-hosted integration runtime nod\
e than using this API directly.
    examples:
      - name: IntegrationRuntimes_SyncCredentials
        text: |-
               az datafactory integration-runtime sync-credentials --factory-name "exampleFactoryName" --name "exampleI\
ntegrationRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime upgrade'] = """
    type: command
    short-summary: Upgrade self-hosted integration runtime to latest version if availability.
    examples:
      - name: IntegrationRuntimes_Upgrade
        text: |-
               az datafactory integration-runtime upgrade --factory-name "exampleFactoryName" --name "exampleIntegratio\
nRuntime" --resource-group "exampleResourceGroup"
"""

helps['datafactory integration-runtime wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datafactory integration-runtime is met.
    examples:
      - name: Pause executing next line of CLI script until the datafactory integration-runtime is successfully created\
.
        text: |-
               az datafactory integration-runtime wait --factory-name "exampleFactoryName" --name "exampleIntegrationRu\
ntime" --resource-group "exampleResourceGroup" --created
"""
