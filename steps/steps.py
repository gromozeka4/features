import subprocess
import time
from behave import *

# ----------------------------------------------------------------------------
# BACKGROUND-STEPS: executed before the each scenario
# ----------------------------------------------------------------------------
@given(u'Start My Server')
def step_impl(context):
    time.sleep(1)
    my_server = subprocess.Popen('python .\server.py')
    try:
        context.proc = subprocess.Popen(my_server, stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
                                        universal_newlines=True)
        context.lines = []
        for line in context.proc.stdout:
            context.lines.append(line)
        context.proc.wait()
    except Exception as e:
        context.ex = e

# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
@given("Server address '{address}'")
def step_impl(context, address):
    context.address = str(address)

@given("Server port '{port}'")
def step_impl(context, port):
    context.port = str(port)

@given("Output file '{path}'")
def step_impl(context, path):
    context.path = path

@when(u'Start client')
def step_impl(context):
    try:
        context.proc = subprocess.Popen("python __main__.py -a " + context.address + " -p " + context.port + " -o \""+

                                        context.path + "\"", stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
                                        universal_newlines=True)
        context.lines = []
        for line in context.proc.stdout:
            context.lines.append(line)
        context.proc.wait()
    except Exception as e:
        context.ex = e

@when(u'No arguments entered')
def step_impl(context):
    try:
        context.proc = subprocess.Popen("python __main__.py", stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
                                        universal_newlines=True)
        context.lines = []
        for line in context.proc.stdout:
            context.lines.append(line)
        context.proc.wait()
    except Exception as e:
        context.ex = e

@then("There is some data in output file")
def step_impl(context):
    with open(context.path, "r") as file:
        lines = file.readlines()
        for data in lines:
            assert data != ''

@then("Error appears '{code}'")
def step_impl(context, code):
    error = context.lines.pop()
    assert code == error.split(' ')[1][:-1]

@then(u'Help is displayed')
def step_impl(context):
    help_part = context.lines.pop(0)
    assert "usage" == help_part.split(' ')[0][:-1]


