console.log("Script loaded successfully "); // console.log is used print messages to the console
Java.perform(function x() { 
    console.log("Inside java perform function");
    // Class the function belongs to.
    var my_class = Java.use("b3nac.injuredandroid.VGV4dEVuY3J5cHRpb25Ud28");
    // Hook the function with parameter string
    var string_class = Java.use("java.lang.String");
    my_class.decrypt.overload("java.lang.String").implementation = function (x) { //hooking the function
        console.log("*************************************")
        //Create a new String and call the function with our new input.
        var my_string = string_class.$new("k3FElEG9lnoWbOateGhj5pX6QsXRNJKh///8Jxi8KXW7iDpk2xRxhQ==");
        console.log("Original arg: " + x); // prints old argument to console
        var ret = this.decrypt(my_string); // returns result from decrypt()
        console.log("Return value: " + ret); // prints result to console
        console.log("*************************************")
        return ret;
    };
    //Find an instance of the class and call "decrypt" function.
    Java.choose("b3nac.injuredandroid", {
        onMatch: function (instance) {
            console.log("Found instance: " + instance);
            console.log("Result of decrypt func: " + instance.decrypt());
        },
        onComplete: function () { }
    });
});
