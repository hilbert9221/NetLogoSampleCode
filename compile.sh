if [ ! -d "classes" ];
then
    mkdir classes
fi

javac -classpath "/home/rotopia/Downloads/NetLogo-6.2.1/app/netlogo-6.2.1.jar" -d classes src/com/test/*.java

jar cvfm test.jar MANIFEST.MF -C classes .