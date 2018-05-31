/**
 * Created by Knight on 29.05.2018.
 */
$(document).ready(function () {
    console.log("Hello!")


    $("#loginButton").click(function () {
        $("#loginForm").modal();
        $("#btn-login-submit").click(function () {
            console.log($("#username").val())
            $.ajax({
                url:"/login",
                data: {
                    login: $("#username").val(),
                    password: $("#password").val()
                },
                type: "POST",
                succcess: function (res) {
                    console.log("some suc")
                }
            })
        })
    });


    $("#registerButton").click(function () {
        $("#registerForm").modal();
        $("#btn-register-submit").click(function (event) {
            event.preventDefault();
            let data = {
                    login: $("#username-reg").val(),
                    password: $("#password-reg").val()
                };
            $.post("/register", data)
        })
    })


});
