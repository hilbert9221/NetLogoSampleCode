package com.test;
import org.nlogo.headless.HeadlessWorkspace;

public class Test {
	public static void main (String[] args) {
		System.out.println("Testing the headless mode...");
        // path for model.nlogo
		String model = args[0];
		try {
            // initialization
			HeadlessWorkspace workspace = HeadlessWorkspace.newInstance();
            // open the model file
			workspace.open(model);
            // execute NetLogo commands
			workspace.command("setup");
            workspace.command("repeat 1 [ go ]");
            // close the model file
            workspace.dispose();
		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}
}