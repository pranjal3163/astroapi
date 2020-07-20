var url;
var sign;
var day;
var tz;

$( function() {
    $("#tabs").tabs({
        active: 1,
    });
    $("#tabid").on('click','li',function (){
        day = $(this).text();
        sign = $("#signname").val();
        tz = "";
        // $.ajax({
        //      url: '/api/forecastdetails?sign='+sign+'&day='+day+'&tz='+tz,
        //      type: 'GET',
        //      success: loadDetailSuccess,
        //      error: loadfailed,
        // })
        $.ajax({
            url: '/api/forecastdetails',
            type: 'POST',
            data: {
                'url': url,
                'sign':sign,
                'day':day,
                'tz':tz
            },
            success: loadDetailSuccess,
            error: loadfailed,
        })
    });

});

function loadDetailSuccess(data){
    var html = '<table>';
    $.each(data, function (k, v) {
        html += `
                <tr>
                  <th>`+ k +`</th>
                   <td>`+ v +`</td>
                </tr>
            `;
    });
    html += '</table>';
    $("#tabsd").html(html);
}

function loadfailed(data){
    alert(data);
}