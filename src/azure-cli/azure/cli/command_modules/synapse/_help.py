# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['synapse'] = """
type: group
short-summary: Manage and operate Synapse Workspace, Spark Pool, SQL Pool.
"""

helps['synapse workspace'] = """
type: group
short-summary: Manage Synapse workspaces.
"""

helps['synapse workspace create'] = """
type: command
short-summary: Create a Synapse workspace.
examples:
  - name: Create a Synapse workspace
    text: |-
        az synapse workspace create --name fromcli4 --resource-group rg \\
          --storage-account testadlsgen2 --file-system testfilesystem \\
          --sql-admin-login-user cliuser1 --sql-admin-login-password Password123! --location "East US"
  - name: Create a Synapse workspace with storage resource id
    text: |-
        az synapse workspace create --name fromcli4 --resource-group rg \\
          --storage-account /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg/providers/Microsoft.Storage/storageAccounts/testadlsgen2 --file-system testfilesystem \\
          --sql-admin-login-user cliuser1 --sql-admin-login-password Password123! --location "East US"
"""

helps['synapse workspace list'] = """
type: command
short-summary: List all Synapse workspaces.
examples:
  - name: List all Synapse workspaces under a subscription
    text: |-
        az synapse workspace list
  - name: List all Synapse workspaces under a specific resource group
    text: |-
        az synapse workspace list --resource-group rg
"""

helps['synapse workspace show'] = """
type: command
short-summary: Get a Synapse workspace.
examples:
  - name: Get a Synapse workspace.
    text: |-
        az synapse workspace show --name testsynapseworkspace --resource-group rg
"""

helps['synapse workspace update'] = """
type: command
short-summary: Update a Synapse workspace.
examples:
  - name: Update a Synapse workspace
    text: |-
        az synapse workspace update --name fromcli4 --resource-group rg \\
          --tags key1=value1
"""

helps['synapse workspace delete'] = """
type: command
short-summary: Delete a Synapse workspace.
examples:
  - name: Delete a Synapse workspace.
    text: |-
        az synapse workspace delete --name testsynapseworkspace --resource-group rg
"""

helps['synapse workspace check-name'] = """
type: command
short-summary: Check if a Synapse workspace name is available or not.
examples:
  - name: Check if a Synapse workspace name is available or not.
    text: |-
        az synapse workspace check-name --name testsynapseworkspace
"""

helps['synapse workspace wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the workspace is met.
"""

helps['synapse spark'] = """
type: group
short-summary: Manage Spark pools and Spark jobs.
"""

helps['synapse spark pool'] = """
type: group
short-summary: Manage Spark pools.
"""

helps['synapse spark pool create'] = """
type: command
short-summary: Create a Spark pool.
examples:
  - name: Create a Spark pool.
    text: |-
        az synapse spark pool create --name testpool --workspace-name testsynapseworkspace --resource-group rg \\
        --spark-version 2.4 --node-count 3 --node-size Medium
"""

helps['synapse spark pool list'] = """
type: command
short-summary: List all Spark pools.
examples:
  - name: List all Spark pools.
    text: |-
        az synapse spark pool list --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse spark pool show'] = """
type: command
short-summary: Get a Spark pool.
examples:
  - name: Get a Spark pool.
    text: |-
        az synapse spark pool show --name testpool --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse spark pool update'] = """
type: command
short-summary: Update the Spark pool.
examples:
  - name: Update the Spark pool's tags.
    text: |-
        az synapse spark pool update --name testpool --workspace-name testsynapseworkspace --resource-group rg \\
        --tags key1=value1
  - name: Update the Spark pool's auto scale configuration.
    text: |-
        az synapse spark pool update --name testpool --workspace-name testsynapseworkspace --resource-group rg \\
        --enable-auto-scale --min-node-count 3 --max-node-count 100
"""

helps['synapse spark pool delete'] = """
type: command
short-summary: Delete a Spark pool.
examples:
  - name: Delete a Spark pool.
    text: |-
        az synapse spark pool delete --name testpool --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse spark pool wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of a Spark pool is met.
"""

helps['synapse sql'] = """
type: group
short-summary: Manage SQL pools.
"""

helps['synapse sql pool'] = """
type: group
short-summary: Manage SQL pools.
"""

helps['synapse sql pool create'] = """
type: command
short-summary: Create a SQL pool.
examples:
  - name: Create a SQL pool.
    text: |-
        az synapse sql pool create --name sqlpoolcli1 --performance-level "DW1000c" \\
        --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse sql pool show'] = """
type: command
short-summary: Get a SQL pool.
examples:
  - name: Get a SQL pool.
    text: |-
        az synapse sql pool show --name sqlpoolcli1 --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse sql pool list'] = """
type: command
short-summary: List all SQL pools.
examples:
  - name: List SQL pools.
    text: |-
        az synapse sql pool list --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse sql pool update'] = """
type: command
short-summary: Update a SQL pool.
examples:
  - name: Update a SQL pool.
    text: |-
        az synapse sql pool update --name sqlpoolcli1 --workspace-name testsynapseworkspace --resource-group rg \\
        --tags key1=value1
"""

helps['synapse sql pool pause'] = """
type: command
short-summary: Pause a SQL pool.
examples:
  - name: Pause a SQL pool.
    text: |-
        az synapse sql pool pause --name sqlpoolcli1 --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse sql pool resume'] = """
type: command
short-summary: Resume a SQL pool.
examples:
  - name: Resume a SQL pool.
    text: |-
        az synapse sql pool resume --name sqlpoolcli1 --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse sql pool delete'] = """
type: command
short-summary: Delete a SQL pool.
examples:
  - name: Delete a SQL pool.
    text: |-
        az synapse sql pool delete --name sqlpoolcli1 --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse sql pool wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of a SQL pool is met.
"""

helps['synapse workspace firewall-rule'] = """
type: group
short-summary:  Manage a workspace's firewall rules.
"""

helps['synapse workspace firewall-rule create'] = """
type: command
short-summary: Create a firewall rule.
examples:
  - name: Create a firewall rule.
    text: |-
        az synapse workspace firewall-rule create --name allowAll --workspace-name testsynapseworkspace \\
        --resource-group rg --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255
"""

helps['synapse workspace firewall-rule show'] = """
type: command
short-summary: Get a firewall rule.
examples:
  - name: Get a firewall rule.
    text: |-
        az synapse workspace firewall-rule show --name rule1 --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse workspace firewall-rule list'] = """
type: command
short-summary: List all firewall rules.
examples:
  - name: List all firewall rules.
    text: |-
        az synapse workspace firewall-rule list --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse workspace firewall-rule delete'] = """
type: command
short-summary: Delete a firewall rule.
examples:
  - name: Delete a firewall rule.
    text: |-
        az synapse workspace firewall-rule delete --name rule1 --workspace-name testsynapseworkspace --resource-group rg
"""

helps['synapse workspace firewall-rule wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of a firewall rule is met.
"""

helps['synapse spark job'] = """
type: group
short-summary: Manage Synapse Spark batch jobs.
"""

helps['synapse spark job submit'] = """
type: command
short-summary: Submit a Spark job.
examples:
  - name: Submit a Java Spark job.
    text: |-
        az synapse spark job submit --name WordCount_Java --workspace-name testsynapseworkspace \\
        --spark-pool-name testsparkpool \\
        --main-definition-file abfss://testfilesystem@testadlsgen2.dfs.core.windows.net/samples/java/wordcount/wordcount.jar \\
        --main-class-name WordCount \\
        --arguments abfss://testfilesystem@testadlsgen2.dfs.core.windows.net/samples/java/wordcount/shakespeare.txt \\
        abfss://testfilesystem@testadlsgen2.dfs.core.windows.net/samples/java/wordcount/result/ \\
        --executors 2 --executor-size Small
"""

helps['synapse spark job list'] = """
type: command
short-summary: List all Spark jobs.
examples:
  - name: List all Spark jobs.
    text: |-
        az synapse spark job list --workspace-name testsynapseworkspace --spark-pool-name testsparkpool
"""

helps['synapse spark job show'] = """
type: command
short-summary: Get a Spark job.
examples:
  - name: Get a Spark job.
    text: |-
        az synapse spark job show --livy-id 1 --workspace-name testsynapseworkspace --spark-pool-name testsparkpool
"""

helps['synapse spark job cancel'] = """
type: command
short-summary: Cancel a Spark job.
examples:
  - name: Cancel a Spark job.
    text: |-
        az synapse spark job cancel --livy-id 1 --workspace-name testsynapseworkspace --spark-pool-name testsparkpool
"""

helps['synapse spark session'] = """
type: group
short-summary: Manage Synapse Spark sessions.
"""

helps['synapse spark session create'] = """
type: command
short-summary: Create a Spark session.
examples:
  - name: Create a Spark session.
    text: |-
        az synapse spark session create --name testsession  --workspace-name testsynapseworkspace \\
        --spark-pool-name testsparkpool --executor-size Small --executors 4
"""

helps['synapse spark session list'] = """
type: command
short-summary: List all Spark sessions.
examples:
  - name: List all Spark sessions.
    text: |-
        az synapse spark session list --workspace-name testsynapseworkspace --spark-pool-name testsparkpool
"""

helps['synapse spark session show'] = """
type: command
short-summary: Get a Spark session.
examples:
  - name: Get a Spark session.
    text: |-
        az synapse spark session show --livy-id 1 --workspace-name testsynapseworkspace --spark-pool-name testsparkpool
"""

helps['synapse spark session cancel'] = """
type: command
short-summary: Cancel a Spark session.
examples:
  - name: Cancel a Spark session.
    text: |-
        az synapse spark session cancel  --livy-id 1 --workspace-name testsynapseworkspace --spark-pool-name testsparkpool
"""

helps['synapse spark session reset-timeout'] = """
type: command
short-summary: Reset a Spark session timeout time.
examples:
  - name: Reset a Spark session's timeout time.
    text: |-
        az synapse spark session reset-timeout --livy-id 1 --workspace-name testsynapseworkspace --spark-pool-name testsparkpool
"""

helps['synapse spark statement'] = """
type: group
short-summary: Manage Synapse Spark statements.
"""

helps['synapse spark statement invoke'] = """
type: command
short-summary: Invoke a Spark statement.
examples:
  - name: Invoke a Spark statement.
    text: |-
        az synapse spark statement invoke --session-id 1 --workspace-name testsynapseworkspace \\
        --spark-pool-name testsparkpool --code "print('hello, Azure CLI')" --language pyspark
  - name: Submit a Spark statement by reading code content from file.
    text: |-
        az synapse spark statement invoke --session-id 1 --workspace-name testsynapseworkspace \\
        --spark-pool-name testsparkpool --code @file-path --language pyspark
"""

helps['synapse spark statement show'] = """
type: command
short-summary: Get a Spark statement.
examples:
  - name: Get a Spark statement.
    text: |-
        az synapse spark statement show --livy-id 1 --session-id 11 --workspace-name testsynapseworkspace \\
        --spark-pool-name testsparkpool
"""

helps['synapse spark statement list'] = """
type: command
short-summary: List all Spark statements
examples:
  - name: List all Spark statements.
    text: |-
        az synapse spark statement list --session-id 11 --workspace-name testsynapseworkspace \\
        --spark-pool-name testsparkpool
"""

helps['synapse spark statement cancel'] = """
type: command
short-summary: Cancel a Spark statement.
examples:
  - name: Cancel a Spark statement.
    text: |-
        az synapse spark statement cancel --livy-id 1 --session-id 11 --workspace-name testsynapseworkspace \\
        --spark-pool-name testsparkpool
"""

helps['synapse role'] = """
type: group
short-summary: Manage Synapse's role assignments and definitions.
"""

helps['synapse role assignment'] = """
type: group
short-summary: Manage Synapse's role assignments.
"""

helps['synapse role assignment show'] = """
type: command
short-summary: Get a role assignment by id.
examples:
  - name: Get a role assignment by id.
    text: |-
        az synapse role assignment show --workspace-name testsynapseworkspace \\
        --id 00000000-0000-0000-0000-000000000000
"""

helps['synapse role assignment list'] = """
type: command
short-summary: List role assignments.
examples:
  - name: List role assignments.
    text: |-
        az synapse role assignment list --workspace-name testsynapseworkspace
  - name: List role assignments by role id/name.
    text: |-
        az synapse role assignment list --workspace-name testsynapseworkspace \\
        --role "Sql Admin"
  - name: List role assignments by assignee.
    text: |-
        az synapse role assignment list --workspace-name testsynapseworkspace \\
        --assignee sp_name
  - name: List role assignments by objectId of the User, Group or Service Principal.
    text: |-
        az synapse role assignment list --workspace-name testsynapseworkspace \\
        --assignee 00000000-0000-0000-0000-000000000000
"""

helps['synapse role assignment create'] = """
type: command
short-summary: Create a role assignment.
examples:
  - name: Create a role assignment using service principal name.
    text: |-
        az synapse role assignment create --workspace-name testsynapseworkspace \\
        --role "Sql Admin" --assignee sp_name
  - name: Create a role assignment using user principal name.
    text: |-
        az synapse role assignment create --workspace-name testsynapseworkspace \\
        --role "Sql Admin" --assignee username@contoso.com
  - name: Create a role assignment using objectId of the User, Group or Service Principal.
    text: |-
        az synapse role assignment create --workspace-name testsynapseworkspace \\
        --role "Sql Admin" --assignee 00000000-0000-0000-0000-000000000000
"""

helps['synapse role assignment delete'] = """
type: command
short-summary: Delete role assignments of workspace.
examples:
  - name: Delete role assignments by role and assignee.
    text: |-
        az synapse role assignment delete --workspace-name testsynapseworkspace \\
        --role "Sql Admin" --assignee sp_name
  - name: Delete role assignments by role id/name.
    text: |-
        az synapse role assignment delete --workspace-name testsynapseworkspace \\
        --role "Sql Admin"
  - name: Delete role assignments by service principal name.
    text: |-
        az synapse role assignment delete --workspace-name testsynapseworkspace \\
        --assignee sp_name
  - name: Delete role assignments by user principal name.
    text: |-
        az synapse role assignment delete --workspace-name testsynapseworkspace \\
        --assignee username@contoso.com
  - name: Delete role assignments by objectId of the User, Group or Service Principal.
    text: |-
        az synapse role assignment delete --workspace-name testsynapseworkspace \\
        --assignee 00000000-0000-0000-0000-000000000001
  - name: Delete role assignments by ids.
    text: |-
        az synapse role assignment delete --workspace-name testsynapseworkspace \\
        --ids 10000000-0000-0000-0000-10000000-10000000-0000-0000-0000-10000000
"""

helps['synapse role definition'] = """
type: group
short-summary:  Manage Synapse's role definitions.
"""

helps['synapse role definition list'] = """
type: command
short-summary: List role definitions.
examples:
  - name: List role definitions.
    text: |-
        az synapse role definition list --workspace-name testsynapseworkspace
"""

helps['synapse role definition show'] = """
type: command
short-summary: Get role definition by role id/name.
examples:
  - name: Get role definition by role id.
    text: |-
        az synapse role definition show --workspace-name testsynapseworkspace \\
        --role 00000000-0000-0000-0000-000000000000
"""

helps['synapse linked-service'] = """
type: group
short-summary: Manage Synapse's linked services.
"""

helps['synapse linked-service create'] = """
type: command
short-summary: Create a linked service.
examples:
  - name: Create a linked service.
    text: |-
        az synapse linked-service create --workspace-name testsynapseworkspace \\
          --name testlinkedservice --file @path/linkedservice.json
"""

helps['synapse linked-service update'] = """
type: command
short-summary: Update an exist linked service.
examples:
  - name: Update an exist linked service.
    text: |-
        az synapse linked-service update --workspace-name testsynapseworkspace \\
          --name testlinkedservice --file @path/linkedservice.json
"""

helps['synapse linked-service show'] = """
type: command
short-summary: Get a linked service.
examples:
  - name: Get a linked service.
    text: |-
        az synapse linked-service show --workspace-name testsynapseworkspace \\
          --name testlinkedservice
"""

helps['synapse linked-service list'] = """
type: command
short-summary: List linked services.
examples:
  - name: List linked services.
    text: |-
        az synapse linked-service list --workspace-name testsynapseworkspace
"""

helps['synapse linked-service delete'] = """
type: command
short-summary: Delete a linked service.
examples:
  - name: Delete a linked service.
    text: |-
        az synapse linked-service delete --workspace-name testsynapseworkspace \\
          --name testlinkedservice
"""

helps['synapse dataset'] = """
type: group
short-summary: Manage Synapse's datasets.
"""

helps['synapse dataset create'] = """
type: command
short-summary: Create a dataset.
examples:
  - name: Create a dataset.
    text: |-
        az synapse dataset create --workspace-name testsynapseworkspace \\
          --name testdataset --file @path/dataset.json
"""

helps['synapse dataset update'] = """
type: command
short-summary: Update an exist dataset.
examples:
  - name: Update an exist dataset.
    text: |-
        az synapse dataset update --workspace-name testsynapseworkspace \\
          --name testdataset --file @path/dataset.json
"""

helps['synapse dataset show'] = """
type: command
short-summary: Get a dataset.
examples:
  - name: Get a dataset.
    text: |-
        az synapse dataset show --workspace-name testsynapseworkspace \\
          --name testdataset
"""

helps['synapse dataset list'] = """
type: command
short-summary: List datasets.
examples:
  - name: List datasets.
    text: |-
        az synapse dataset list --workspace-name testsynapseworkspace
"""

helps['synapse dataset delete'] = """
type: command
short-summary: Delete a dataset.
examples:
  - name: Delete a dataset.
    text: |-
        az synapse dataset delete --workspace-name testsynapseworkspace \\
          --name testdataset
"""

helps['synapse pipeline'] = """
type: group
short-summary: Manage Synapse's pipelines.
"""

helps['synapse pipeline create'] = """
type: command
short-summary: Create a pipeline.
examples:
  - name: Create a pipeline.
    text: |-
        az synapse pipeline create --workspace-name testsynapseworkspace \\
          --name testpipeline --file @path/pipeline.json
"""

helps['synapse pipeline update'] = """
type: command
short-summary: Update an exist pipeline.
examples:
  - name: Update an exist pipeline.
    text: |-
        az synapse pipeline update --workspace-name testsynapseworkspace \\
          --name testpipeline --file @path/pipeline.json
"""

helps['synapse pipeline show'] = """
type: command
short-summary: Get a pipeline.
examples:
  - name: Get a pipeline.
    text: |-
        az synapse pipeline show --workspace-name testsynapseworkspace \\
          --name testpipeline
"""

helps['synapse pipeline list'] = """
type: command
short-summary: List pipelines.
examples:
  - name: List pipelines.
    text: |-
        az synapse pipeline list --workspace-name testsynapseworkspace
"""

helps['synapse pipeline delete'] = """
type: command
short-summary: Delete a pipeline.
examples:
  - name: Delete a pipeline.
    text: |-
        az synapse pipeline delete --workspace-name testsynapseworkspace \\
          --name testpipeline
"""

helps['synapse pipeline create-run'] = """
type: command
short-summary: Creates a run of a pipeline.
examples:
  - name: Pipelines_CreateRun
    text: |-
        az synapse pipeline create-run --workspace-name testsynapseworkspace --name "myPipeline" \\
          --parameters "{\\"OutputBlobNameList\\":[\\"exampleoutput.csv\\"]}"
"""

helps['synapse pipeline-run'] = """
type: group
short-summary: Manage Synapse's pipeline run.
"""

helps['synapse pipeline-run show'] = """
type: command
short-summary: Get a pipeline run by its run ID.
examples:
  - name: Get a pipeline run by its run ID.
    text: |-
        az synapse pipeline-run show --workspace-name testsynapseworkspace \\
          --run-id "2f7fdb90-5df1-4b8e-ac2f-064cfa58202b"
"""

helps['synapse pipeline-run cancel'] = """
type: command
short-summary: Cancel a pipeline run by its run ID.
examples:
  - name: Cancel a pipeline run by its run ID.
    text: |-
        az synapse pipeline-run cancel --workspace-name testsynapseworkspace \\
          --run-id "16ac5348-ff82-4f95-a80d-638c1d47b721"
"""

helps['synapse pipeline-run query-by-workspace'] = """
type: command
short-summary: Query pipeline runs in the workspace based on input filter conditions.
examples:
  - name: Query pipeline runs in the workspace based on input filter conditions.
    text: |-
        az synapse pipeline-run query-by-workspace --workspace-name testsynapseworkspace --filters \\
          operand="PipelineName" operator="Equals" values="testpipeline" --last-updated-after "2020-09-03T00:36:44.3345758Z" \\
          --last-updated-before "2020-09-03T00:49:48.3686473Z"
"""

helps['synapse activity-run'] = """
type: group
short-summary: synapse activity-run
"""

helps['synapse activity-run query-by-pipeline-run'] = """
type: command
short-summary: Query activity runs based on input filter conditions.
examples:
  - name: Query activity runs based on input filter conditions.
    text: |-
        az synapse activity-run query-by-pipeline-run --workspace-name testsynapseworkspace \\
          --last-updated-after "2020-09-03T00:36:44.3345758Z" --last-updated-before "2020-09-03T00:49:48.3686473Z" \\
          --name testpipeline --run-id "53eeed66-ec46-11ea-8bd5-448500a5b1ac"
"""

helps['synapse trigger'] = """
type: group
short-summary: Manage Synapse's triggers.
"""

helps['synapse trigger create'] = """
type: command
short-summary: Create a trigger.
examples:
  - name: Create a trigger.
    text: |-
        az synapse trigger create --workspace-name testsynapseworkspace \\
          --name testtrigger --file @path/trigger.json
"""

helps['synapse trigger update'] = """
type: command
short-summary: Update an exist trigger.
examples:
  - name: Update an exist trigger.
    text: |-
        az synapse trigger update --workspace-name testsynapseworkspace \\
          --name testtrigger --file @path/trigger.json
"""

helps['synapse trigger show'] = """
type: command
short-summary: Get a trigger.
examples:
  - name: Get a trigger.
    text: |-
        az synapse trigger show --workspace-name testsynapseworkspace \\
          --name testtrigger
"""

helps['synapse trigger list'] = """
type: command
short-summary: List triggers.
examples:
  - name: List triggers.
    text: |-
        az synapse trigger list --workspace-name testsynapseworkspace
"""

helps['synapse trigger delete'] = """
type: command
short-summary: Delete a trigger.
examples:
  - name: Delete a trigger.
    text: |-
        az synapse trigger delete --workspace-name testsynapseworkspace \\
          --name testtrigger
"""

helps['synapse trigger subscribe-to-event'] = """
type: command
short-summary: Subscribe event trigger to events.
examples:
  - name: Subscribe event trigger to events.
    text: |-
        az synapse trigger subscribe-to-event --workspace-name testsynapseworkspace \\
          --name eventtrigger
"""

helps['synapse trigger get-event-subscription-status'] = """
type: command
short-summary: Get a trigger's event subscription status.
examples:
  - name:  Get a trigger's event subscription status.
    text: |-
        az synapse trigger get-event-subscription-status --workspace-name testsynapseworkspace \\
          --name eventtrigger
"""

helps['synapse trigger unsubscribe-from-event'] = """
type: command
short-summary: Unsubscribe event trigger from events.
examples:
  - name: Unsubscribe event trigger from events.
    text: |-
        az synapse trigger unsubscribe-from-event --workspace-name testsynapseworkspace \\
          --name eventtrigger
"""

helps['synapse trigger start'] = """
type: command
short-summary: Starts a trigger.
examples:
  - name: Starts a trigger.
    text: |-
        az synapse trigger start --workspace-name testsynapseworkspace \\
          --name testtrigger
"""

helps['synapse trigger stop'] = """
type: command
short-summary: Stops a trigger.
examples:
  - name: Stops a trigger.
    text: |-
        az synapse trigger stop --workspace-name testsynapseworkspace \\
          --name testtrigger
"""

helps['synapse trigger-run'] = """
    type: group
    short-summary: synapse trigger-run
"""

helps['synapse trigger-run rerun'] = """
type: command
short-summary: Rerun single trigger instance by runId.
examples:
  - name: Rerun single trigger instance by runId.
    text: |-
        az synapse trigger-run rerun --workspace-name testsynapseworkspace \\
          --name testtrigger --run-id 08586024068106001417583731803CU31
"""

helps['synapse trigger-run query-by-workspace'] = """
type: command
short-summary: Query trigger runs in the workspace based on input filter conditions.
examples:
  - name: Query trigger runs in the workspace based on input filter conditions.
    text: |-
        az synapse trigger-run query-by-workspace --workspace-name testsynapseworkspace --filters \\
          operand="TriggerName" operator="Equals" values="testtrigger" --last-updated-after "2020-09-03T00:36:44.3345758Z" \\
          --last-updated-before "2020-09-03T00:49:48.3686473Z"
"""

helps['synapse data-flow'] = """
type: group
short-summary: Manage Synapse's data flows.
"""

helps['synapse data-flow create'] = """
type: command
short-summary: Create a data flow.
examples:
  - name: Create a data flow.
    text: |-
        az synapse data-flow create --workspace-name testsynapseworkspace \\
          --name testdataflow --file @path/dataflow.json
"""

helps['synapse data-flow update'] = """
type: command
short-summary: Update an exist data flow.
examples:
  - name: Update an exist data flow.
    text: |-
        az synapse data-flow update --workspace-name testsynapseworkspace \\
          --name testdataflow --file @path/dataflow.json
"""

helps['synapse data-flow show'] = """
type: command
short-summary: Get a data flow.
examples:
  - name: Get a data flow.
    text: |-
        az synapse data-flow show --workspace-name testsynapseworkspace \\
          --name testdataflow
"""

helps['synapse data-flow list'] = """
type: command
short-summary: List data flows.
examples:
  - name: List data flows.
    text: |-
        az synapse data-flow list --workspace-name testsynapseworkspace
"""

helps['synapse data-flow delete'] = """
type: command
short-summary: Delete a data flow.
examples:
  - name: Delete a data flow.
    text: |-
        az synapse data-flow delete --workspace-name testsynapseworkspace \\
          --name testdataflow
"""

helps['synapse notebook'] = """
type: group
short-summary: Manage Synapse's notebooks.
"""

helps['synapse notebook create'] = """
type: command
short-summary: Create a notebook.
examples:
  - name: Create a notebook.
    text: |-
        az synapse notebook create --workspace-name testsynapseworkspace \\
          --name testnotebook --file @path/notebook.json
"""

helps['synapse notebook update'] = """
type: command
short-summary: Update an exist notebook.
examples:
  - name: Update an exist notebook.
    text: |-
        az synapse notebook update --workspace-name testsynapseworkspace \\
          --name testnotebook --file @path/notebook.json
"""

helps['synapse notebook import'] = """
type: command
short-summary: Import a notebook.
examples:
  - name: Import a notebook.
    text: |-
        az synapse notebook import --workspace-name testsynapseworkspace \\
          --name testnotebook --file @path/notebook.json
"""

helps['synapse notebook show'] = """
type: command
short-summary: Get a notebook.
examples:
  - name: Get a notebook.
    text: |-
        az synapse notebook show --workspace-name testsynapseworkspace \\
          --name testnotebook
"""

helps['synapse notebook list'] = """
type: command
short-summary: List notebooks.
examples:
  - name: List notebooks.
    text: |-
        az synapse notebook list --workspace-name testsynapseworkspace
"""

helps['synapse notebook export'] = """
type: command
short-summary: Export notebooks.
examples:
  - name: Export a notebook.
    text: |-
        az synapse notebook export --workspace-name testsynapseworkspace \\
          --name testnotebook --output-folder C:/output
  - name: Export all notebooks under a workspace.
    text: |-
        az synapse notebook export --workspace-name testsynapseworkspace \\
          --output-folder C:/output
"""

helps['synapse notebook delete'] = """
type: command
short-summary: Delete a notebook.
examples:
  - name: Delete a notebook.
    text: |-
        az synapse notebook delete --workspace-name testsynapseworkspace \\
          --name testnotebook
"""
