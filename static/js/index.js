/**
 * Created by Knight on 29.05.2018.
 */
$(document).ready(function () {
    console.log("Hello!");


    $("#loginButton").click(function () {
        $("#loginForm").modal();
        $("#btn-login-submit").click(function () {
            console.log($("#username").val());
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
            });
        });
    });


    $("#registerButton").click(function () {
        $("#registerForm").modal();
        $("#btn-register-submit").click(function (event) {
            let data = {
                    login: $("#username-reg").val(),
                    password: $("#password-reg").val(),
                    confirm: $("#password-confirm").val()
                };
            $.post("/register", data, function (data) {
               $("#registration-result").html(data);
            }).fail(function (data) {
                $("#registration-result").html(data);
            });
        });
    });


});
