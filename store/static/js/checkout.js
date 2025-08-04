$(document).ready(function () {
    $('.paywithrazorpay').click(function (e) {
        e.preventDefault();

        var firstname = $("[name='firstname']").val();
        var lastname = $("[name='lastname']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='phone']").val();
        var address = $("[name='Address']").val();
        var city = $("[name='City']").val();
        var state = $("[name='State']").val();
        var country = $("[name='Country']").val();
        var pinCode = $("[name='PinCode']").val();
        var token =$("[name='csrfmiddlewaretoken']").val();

        // Validate if any field is empty
        if (firstname === "" || lastname === "" || email === "" || phone === "" || address === "" || city === "" || state === "" || country === "" || pinCode === "") {
            swal("Alert!", "All fields are mandatory!", "error");
            return false;
        } else {
            $.ajax({
                type: "GET",
                url: "/razorpaycheck/", // Ensure this URL matches your Django URL
                success: function(response) {
                    var options = {
                        "key": "rzp_test_bvs9fcMzpUjePo", // Replace with your Razorpay key
                        "amount": response.total_price * 100,
                        "currency": "INR",
                        "name": "Amritha_Madampully",
                        "description": "Thank you for buying from us",
                        "image": "https://example.com/your_logo", // Replace with your logo URL
                        "handler": function (responseb) {
                            // Handle the response here, maybe save the order
                            alert(responseb.razorpay_payment_id);
                            data= {
                            "firstname":firstname,
                            "lastname":lastname,
                            "email":email,
                            "phone":phone,
                            "address":address,
                            "city":city,
                            "state":state,
                            "country":country,
                            "pinCode":pinCode,
                            "payment_mode":"Paid by Razorpay",
                            "payment_id":responseb.razorpay_payment_id,
                            csrfmiddlewaretoken:token

                        }
                        $.ajax({
                                method : "POST",
                                url :"/place-order",
                                data:data,
                                success:function (responsec){
                                    swal("Congratulation!",responsec.status,"success").then((value) => {
                                        window.location.href = '/my-orders'
                                    });
                                }

                            });
                        },
                        "prefill": {
                            "name": firstname + " " + lastname,
                            "email": email,
                            "contact": phone
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };

                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                },
                error: function(xhr, status, error) {
                    console.error(xhr.responseText);
                    swal("Error!", "Could not proceed to payment.", "error");
                }
            });
        }
    });
});