console.log("Script loaded successfully "); // console.log is used print messages to the console
Java.perform(function x() { 
    console.log("Inside java perform function");
    // Class the function belongs to.
    var my_class = Java.use("com.android.insecurebankv2.CryptoClass");
    // Hook the function with parameter string
    var string_class = Java.use("java.lang.String");
    my_class.aesDeccryptedString.overload("java.lang.String").implementation = function (x) { //hooking the function
        console.log("*************************************")
        //Create a new String and call the function with our new input.
        var my_string = string_class.$new("v/sJpihDCo2ckDmLW5Uwiw==");
        console.log("Original arg: " + x); // prints old argument to console
        var ret = this.aesDeccryptedString(my_string); // returns result from decrypt()
        console.log("Return value: " + ret); // prints result to console
        console.log("*************************************")
        return ret;
    };
    //Find an instance of the class and call "aesDeccryptedString" function.
    Java.choose("com.android.insecurebankv2", {
        onMatch: function (instance) {
            console.log("Found instance: " + instance);
            console.log("Result of aesDeccryptedString func: " + instance.aesDeccryptedString();
        },
        onComplete: function () { }
    });
});
