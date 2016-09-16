from nipype.interfaces import io as nio
from nipype.interfaces import utility as niu
from nipype.pipeline import engine as pe


def generate_workflow(test_item, unique_name=False):
    if unique_name:
        workflow = pe.Workflow(name=test_item)
    else:
        workflow = pe.Workflow(name='not_unique_workflow_name')
    return workflow


test_items = ['1', '2', '3', '4']
test_nodes = []
workflow = pe.Workflow(name="outerworkflow")

for item in test_items:
    test_nodes.append(generate_workflow(item))

print(test_nodes)
workflow.add_nodes(test_nodes)
workflow.run()
