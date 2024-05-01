console.log("Script loaded successfully ");
Java.perform(function x() { 
    console.log("Inside java perform function");
    // Class the function belongs to.
    var my_class = Java.use("b3nac.injuredandroid.FlagsOverview");
    
    console.log("########### Old Boolean Values ###########")
    console.log("Flag One: " + my_class.flagOneButtonColor.value);
    console.log("Flag Two: " + my_class.flagTwoButtonColor.value)
    console.log("Flag Three: " + my_class.flagThreeButtonColor.value)
    console.log("Flag Four: " + my_class.flagFourButtonColor.value)
    console.log("Flag Five: " + my_class.flagFiveButtonColor.value)
    console.log("Flag Six: " + my_class.flagSixButtonColor.value)
    
    // Sets boolean variables from false to true.
    my_class.flagFiveButtonColor.value = true;
    my_class.flagFourButtonColor.value = true;
    my_class.flagOneButtonColor.value = true;
    my_class.flagSixButtonColor.value = true;
    my_class.flagThreeButtonColor.value = true;
    my_class.flagTwoButtonColor.value = true;

    console.log("########### New Boolean Values ###########")
    console.log("Flag One: " + my_class.flagOneButtonColor.value)
    console.log("Flag Two: " + my_class.flagTwoButtonColor.value)
    console.log("Flag Three: " + my_class.flagThreeButtonColor.value)
    console.log("Flag Four: " + my_class.flagFourButtonColor.value)
    console.log("Flag Five: " + my_class.flagFiveButtonColor.value)
    console.log("Flag Six: " + my_class.flagSixButtonColor.value);
});
