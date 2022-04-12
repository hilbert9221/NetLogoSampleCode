This repository provides a showcase for including NetLogo source files (`.nls`) and running NetLogo model in a headless mode. The code was tested wih NetLogo 6.2.1. For other versions of NetLogo, re-editing the `.nlogo` file and re-setting the path for NetLogo should work.

#### Include NetLogo source files
Simple codes for printing "Hello World!" are provided at the directory `netlogo`. Simply run `netlogo/model.nlogo` and `netlogo/split_model.nlogo` separately to check if they work the same.

#### Run NetLogo model in the headless mode from Java
Check the Java source code [here](src/com/test/Test.java) and follow the two steps.

1. Replace the path `directory/*.jar` with your own path of NetLogo in file [compile.sh](compile.sh) and [MANIFEST.MF](MANIFEST.MF).
2. Compile and run.
```bash
bash compile.sh
bash run.sh
```

#### Reference
[Usage of __includes](https://ccl.northwestern.edu/netlogo/docs/codetab.html#included-files-menu)

[NetLogo Controlling API](https://github.com/NetLogo/NetLogo/wiki/Controlling-API)