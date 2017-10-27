
# Read a python disassembly (2.7-ish) and execute it.  This is not
# complete interpreter... Just enough to run the 'Handcrafted pyc'
# challenge from Hitcon CTF 2016.

import re
import pprint
import marshal
import dis

co_vars = {}
stack = []
with open('vars.marshal') as f:
    co_names = marshal.load(f)
    co_consts = marshal.load(f)
    co_varnames = marshal.load(f)

prog = []
disass = False
with open('disassembly') as f:
    for line in f:
        if re.match('^START DIS', line):
            disass = True
            continue
        if not disass:
            continue
        byteno = int(line[11:15].strip())
        funname = line[16:38].strip()
        rest = line[38:].strip()
        t = (byteno, funname, rest)
        prog.append(t)

# find index with the corresponding byte number
def jump(prog, s):
    """find the index in program with corresponding byte number"""
    npc = int(s)
    i = 0
    while i < len(prog):
        if prog[i][0] == npc:
            break
        i += 1
    assert i != len(prog)
    return i

# Execute the program, starting with pc=0
pc = 0
while True:
    (_, fun, rest) = prog[pc]
    pc += 1

    if fun == "LOAD_GLOBAL":
        m = re.match('^([0-9]+) .*', rest)
        assert m is not None, "bad rest: %s" % rest
        stack.append(co_names[int(m.group(1))])
        continue

    if fun == "LOAD_CONST":
        m = re.match('^([0-9]+) \((.*)\)$', rest)
        assert m is not None, "bad rest: %s" % rest
        stack.append(co_consts[int(m.group(1))])
        continue

    if fun == "CALL_FUNCTION":
        arg = stack.pop()
        name = eval(stack.pop())
        stack.append(name(arg))
        continue

    if fun == "ROT_TWO":
        arg1 = stack.pop()
        arg2 = stack.pop()
        stack.append(arg1)
        stack.append(arg2)
        continue

    if fun == "BINARY_ADD":
        stack.append(stack.pop() + stack.pop())
        continue

    if fun == "NOP":
        continue

    if fun == "JUMP_ABSOLUTE":
        pc = jump(prog, rest)
        continue

    if fun == "STORE_FAST":
        m = re.match('^([0-9]+) \((.*)\)$', rest)
        assert m is not None, "bad rest: %s" % rest
        varname = co_varnames[int(m.group(1))]
        co_vars[varname] = stack.pop()
        continue

    if fun == "POP_TOP":
        stack.pop()
        continue

    if fun == "LOAD_FAST":
        m = re.match('^([0-9]+) \((.*)\)$', rest)
        assert m is not None, "bad rest: %s" % rest
        varname = co_varnames[int(m.group(1))]
        stack.append(co_vars[varname])
        continue

    if fun == "COMPARE_OP":
        a = stack.pop()
        b = stack.pop()
        m = re.match('^([0-9]+) \((.*)\)$', rest)
        assert m is not None, "bad rest: %s" % rest
        print "compare('%s', '%s')" % (a, b)
        op = dis.cmp_op[int(m.group(1))]
        if op == '==':
            if a == b:
                stack.append(True)
            else:
                stack.append(False)
            continue
        assert False, "unhandled compare_op: %s" % op


    if fun == "POP_JUMP_IF_FALSE":
        if not stack.pop():
            pc = jump(prog, rest)
        continue

    if fun == "PRINT_ITEM":
        print stack.pop()[::-1]
        continue

    if fun == "PRINT_NEWLINE":
        print ""
        continue

    if fun == "RETURN_VALUE":
        break

    assert False, "Unhandled fun: %s" % fun
