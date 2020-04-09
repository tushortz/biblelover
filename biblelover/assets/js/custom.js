$(document).ready(function(){
  $("input#check-terms").change(function(){
    // On register page, disable/enable button depending on whether terms checkbox is checked
    $("input#signup-btn").attr('disabled', !$(this).prop("checked"));
  })
});
