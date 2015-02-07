$(document).ready(function(){
  $("#y").click(function(){
    $("#y").addClass("active");
    $("#x").removeClass("active");
    $("#z").removeClass("active");

  });
    $("#z").click(function(){
    $("#z").addClass("active");
    $("#x").removeClass("active");
    $("#y").removeClass("active");

  });
      $("#x").click(function(){
    $("#x").addClass("active");
    $("#y").removeClass("active");
    $("#z").removeClass("active");

  });
});