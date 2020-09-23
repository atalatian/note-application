$(document).ready(function () {
    $(".ADD").click(function () {
        window.location.pathname = "/app/main/" + "add";
    });

    $(".EDIT").click(function () {
        window.location.pathname = "/app/main/update/" + this.childNodes[1].innerText;
    });

    $(".DELETE").click(function () {
        window.location.pathname = "/app/main/delete/" + this.childNodes[1].innerText;
    });
});