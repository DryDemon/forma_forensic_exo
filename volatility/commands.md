Prise d'information : 

./volatility_2.6_lin64_standalone  -f ~/Desktop/vol/ch2/ch2.dmp imageinfo
ou
vol -f ch2.dmp windows.info
vol -f ch2.dmp hivelist
vol -f ch2.dmp windows.pslist
vol -f ch2.dmp windows.pstree

Exo 2 :
vol -f ch2.dmp windows.registry.printkey --key 'ControlSet001\Control\ComputerName\ComputerName'
ou 
vol -f ../ch2.dmp windows.envars.Envars  
ou
vol -f ch2.dmp --profile=Win7SP0x86 hivelist
Choppe l'offset -> 0x8b21c008 0x039ef008 \REGISTRY\MACHINE\SYSTEM
vol -f ch2.dmp --profile=Win7SP0x86 printkey -o 0x8b21c008 -K 'ControlSet001\Control\ComputerName\ComputerName'
ref https://www.aldeid.com/wiki/Volatility/Retrieve-hostname

ou
./volatility_2 -f ch2.dmp --profile=Win7SP0x86 hivelist


Exo 5 :

./volatility_2.6_lin64_standalone --profile=Win7SP1x86 -f ../ch2.dmp hashdump

Puis crack station

Exo 3 : 

./volatility_2.6_lin64_standalone  -f ~/Desktop/vol/ch2/ch2.dmp --profile=Win7SP0x86 memdump -p 1616 --dump-dir ./

./volatility_2.6_lin64_standalone -f ../ch2.dmp --profile=Win7SP0x86 cmdline --pid 2772
Volatility Foundation Volatility Framework 2.6
************************************************************************
iexplore.exe pid:   2772
Command line : "C:\Users\John Doe\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\iexplore.exe" 
                                                                                                                                                                                                                  
printf '%s' 'C:\Users\John Doe\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\iexplore.exe' | md5sum
49979149632639432397b3a1df8cb43d  -


Exo 4 :

vol -f ch2.dmp windows.pslist.PsList --pid 1616 --dump
vol -f ch2.dmp windows.pslist.PsList --pid 2772 --dump
strings 2772.iexplore.exe.0x400000.dmp
strings 1616.cmd.exe.0x4a330000.dmp -el -n 16




Exo 4 :





tips : 

Avoir le screenshot
./volatility_2.6_lin64_standalone -f ../../../Desktop/forensic/ch2.dmp --profile=Win7SP0x86 screenshot -D ./


!!!! Pour la mem du process
vol.py -f dump windows.memmap.Memmap --pid 1470 --dump
