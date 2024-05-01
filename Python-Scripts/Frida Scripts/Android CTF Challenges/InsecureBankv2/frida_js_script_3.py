console.log("Script loaded successfully "); // console.log is used print messages to the console
Java.perform(function x() { 
    console.log("Inside java perform function");
    // Class the function belongs to.
    var my_class = Java.use("com.android.insecurebankv2.PostLogin");
    
    my_class.doesSUexist.implementation = function (x) { //hooking the function
        console.log("*************SU Root Check Bypassed************************")
        return false
    };

    my_class.doesSuperuserApkExist.implementation = function (x) { //hooking the function
        console.log("*************SuperuserAPK Root Check Bypassed************************")
        return false
    };
});
