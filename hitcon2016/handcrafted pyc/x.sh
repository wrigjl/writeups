echo 'hello' | python foo.py > disassembly
PWD=`echo 'hello' | python vm.py | cut -f 2 -d \'`
echo "$PWD" | python vm.py
