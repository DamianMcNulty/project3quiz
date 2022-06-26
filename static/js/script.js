$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
    $('.leaderboard').DataTable( {
        searching: false,
        paging: false,
        info: false,
        fixedHeader: true,
        responsive: true,
        "iDisplayLength": 5,
        "aLengthMenu": [[5, 10, 15, -1], [5, 10, 15, "All"]],
        "order": [],
        "columnDefs": [ {
        "targets"  : 'no-sort',
        "orderable": false,
        }]
   });
});