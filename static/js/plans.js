function alterCb(flag,email,paid_date,product_name){
    console.log(flag,email)
    window.location.href = "/plans?email="+email+"&products="+product_name+"&paid_date="+paid_date
    +"&flag="+flag;
}
function pauseCb(obj){
    parent_div = obj.parentElement;
    parent_div = parent_div.lastElementChild;
    parent_div.style.display = 'block';
}

function updateCb(obj,email,product_name){
    temp1 = obj.parentElement;
    temp2 =temp1.children[0]
    pause_month = temp2.children[1].value
    $.ajax({
   url:"/userplans",
   data: {'data':[email,product_name,pause_month]},
   type: 'POST',

   success: function (res, status) {
        location.reload();

      },

   error: function (res) {

   }
});
}