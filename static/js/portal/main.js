(function() {
	'use strict';
    $('.addTask').on('submit', function(e) {
        var data = Utils.getFormData('.addTask');
        Utils.submitForm(e, data, '/home/add/task/');
        return false;
    });

    $('.update-task').on('submit', function(e) {
        var data = Utils.getFormData('.update-task'),
            id = $('.task-id').val(),
            url = '/home/edit/task/'+id+'/';
        Utils.submitForm(e, data, url);
        return false;
    })
    

})();

// When the document is ready
$(document).ready(function () {
    var nowDate = new Date();
    var today = new Date(nowDate.getFullYear(), nowDate.getMonth(), nowDate.getDate(), 0, 0, 0, 0);
    $('#due-date').datepicker({
        format: "yyyy-mm-dd",
        startDate: today 
    });  

});
