
function buyProductCb(month,user,product_name){
    console.log(month)
    if(user === "True"){
      window.location.href = "/payments?month="+month+"&product_name="+product_name;
    }
    else{
      window.location.href = "/register";
    }
}
function alterProductCb(month,email,paid_date,product_name){
    console.log(month,paid_date)
    window.location.href = "/payments?month="+month+"&product_name="+product_name+"&email="+product_name
    +"&flag="+'True'+"&paid_date="+paid_date;
}